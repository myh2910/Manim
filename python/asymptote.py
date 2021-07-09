from manim import *
import cmath
from pydub.audio_segment import AudioSegment

"""https://docs.manim.community/en/stable/
Current version: Manim Community v0.8.0

Some command line flags:
 -a : renders multiple Scene classes
 -ql : low quality
 -qm : medium quality
 -qh : high quality
 -qk : 4k quality
 -p : plays the animation once it is rendered
 -f : opens the file browser at the location of the animation
 -i : .gif format"""

##-------------------------------------------------------------------------------------------------##

def degrees(t):
    """Converts t in radians into degrees."""
    return t/DEGREES

def radians(t):
    """Converts t in degrees into radians."""
    return t*DEGREES

def coord(P) -> tuple:
    """Returns the coordinates of the point P."""
    t = type(P)
    if t == complex:
        return P.real, P.imag
    elif t == Dot:
        return P.get_center()[0], P.get_center()[1]
    else:
        return P[0], P[1]

def comp(P) -> complex:
    """Returns a complex number with the same coordinates as P."""
    x, y = coord(P)
    return complex(x, y)

def nparray(P) -> np.ndarray:
    """Returns an array with the same coordinates as P."""
    x, y = coord(P)
    return np.array((x, y, 0))

def distance(A, B) -> float:
    """Returns the length of the segment AB."""
    x1, y1 = coord(A)
    x2, y2 = coord(B)
    x, y = x1-x2, y1-y2
    return (x**2+y**2)**(1/2)

def arg(P) -> float:
    """Returns the angle between the vector P and the real axis in radians."""
    return cmath.phase(comp(P))

def dir(P):
    """Returns a vector with modulus 1 with its direction equal to P."""
    t = type(P)
    if t == Dot or t == complex or t == np.ndarray:
        d = distance((0, 0), P)
        if d == 0:
            return ORIGIN
        else:
            x, y = coord(P)
            return np.array((x/d, y/d, 0))
    else:
        return complex(np.cos(radians(P)), np.sin(radians(P)))

##-------------------------------------------------------------------------------------------------##

origin = complex(0, 0)

def extension(A, B, C, D) -> complex:
    """Returns the intersection point between lines AB and CD."""
    try:
        return ((A.conjugate()*B-A*B.conjugate())*(C-D)-(A-B)*(C.conjugate()*D-C*D.conjugate()))/((A.conjugate()-B.conjugate())*(C-D)-(A-B)*(C.conjugate()-D.conjugate()))
    except:
        return extension(comp(A), comp(B), comp(C), comp(D))

def foot(P, A, B) -> complex:
    """Returns the foot of the perpendicular from P to the line AB."""
    try:
        return ((P-A)/(B-A)).real*(B-A)+A
    except:
        return foot(comp(P), comp(A), comp(B))

def sim(B, C, A1, B1, C1) -> complex:
    """returns the complex coordinates of the point A, such that triangles ABC and A1B1C1 are similar."""
    try:
        return B-(B1-A1)*(B-C)/(B1-C1)
    except:
        return sim(comp(B), comp(C), comp(A1), comp(B1), comp(C1))

def circumcenter(A, B, C) -> complex:
    """Returns the circumcenter of triangle ABC."""
    try:
        M, N = (A+B)/2, (B+C)/2
        P, Q = M + complex(0, 1)*(A-M), N + complex(0, 1)*(B-N)
        return extension(M, P, N, Q)
    except:
        return circumcenter(comp(A), comp(B), comp(C))

##-------------------------------------------------------------------------------------------------##

def DOT(P, c=WHITE, s=ORIGIN, **kwargs) -> Dot:
    """Returns a Dot element shifted by s colored with c."""
    x, y = coord(P)
    return Dot(np.array((x, y, 0)), color=c, **kwargs).shift(s)

def POLY(*vertices, **kwargs):
    return Polygon(*[nparray(vertex) for vertex in vertices], **kwargs)

def CR(r=1, O=ORIGIN, c=WHITE, **kwargs) -> Circle:
    """Returns the circle centered at O with radius r."""
    return Circle(radius=r, color=c, **kwargs).move_to(nparray(O))

def CP(P, O=ORIGIN, c=WHITE, **kwargs) -> Circle:
    """Returns the circle centered at O with radius OP."""
    return CR(distance(O, P), nparray(O), c, **kwargs)

def MP(label, P, array=UP, s=1, **kwargs) -> Tex:
    """Returns the label of an object."""
    return Tex(label).scale(s).next_to(P, dir(nparray(array)), 0.25*s, **kwargs)

def MASS(*args):
    lst = make_lst(args)
    return center_of_mass([nparray(item) for item in lst])

def MID(A, B):
    """Returns the midpoint of the segment AB."""
    return MASS(A, B)

def LINE(A, B, c=WHITE, **kwargs) -> Line:
    """Returns the line AB."""
    return Line(nparray(A), nparray(B), **kwargs).set_color(c)

def DA(A, B, k=0, c=WHITE, **kwargs) -> DoubleArrow:
    """Returns the DoubleArrow AB."""
    A, B = nparray(A), nparray(B)
    return DoubleArrow((k+1)*A-k*B, (k+1)*B-k*A, **kwargs).set_color(c)

def MA(A, B, C, l=0.25, settings=None, **kwargs):
    """Returns the arc of the angle ABC. The number of arcs depends on settings."""
    if type(settings) == int and settings > 0:
            limit = .15
            if l/(settings+2) > limit:
                e = limit
            else:
                e = 1/(settings+2)
            arcs = [MA(A, B, C, l*(1-i*e), **kwargs) for i in range(0, settings)]
            return VGroup(*arcs)
    else:
        return Angle(LINE(B, A), LINE(B, C), l, **kwargs)

##-------------------------------------------------------------------------------------------------##

def make_lst(args):
    lst = []
    for item in args:
        if type(item) == list or type(item) == tuple:
            lst2 = item
        else:
            lst2 = [item]
        for elem in lst2:
            lst.append(elem)
    return lst

def COL(*args, c=WHITE):
    """Color items in args with color c."""
    lst = make_lst(args)
    return [item.animate.set_color(c) for item in lst]

##-------------------------------------------------------------------------------------------------##

def REPEATED_LST(string: str) -> list[str]: 
    lst = []
    if len(string) == 0:
        lst = ['']
    elif string[0] != ' ':
        for i, item in enumerate(string):
            if item != ' ' and i < len(string)-1:
                if string[i+1] != ' ':
                    lst.append(item)
                elif string[i+1] == ' ':
                    j = i+1
                    while True:
                        if j == len(string):
                            break
                        elif string[j] != ' ':
                            break
                        else:
                            j += 1
                    lst.append(string[i:j])
            elif item != ' ' and i == len(string)-1:
                lst.append(item)
    else:
        j = 0
        while True:
            if j == len(string):
                lst.append(' '*len(string))
                break
            elif string[j] != ' ':
                for idx, item in enumerate(REPEATED_LST(string[j:])):
                    if idx == 0:
                        lst.append(' '*j + item)
                    else:
                        lst.append(item)
                break
            else:
                j += 1
    return lst
    
def REPEAT(to_repeat: str, string: str) -> list[str]:
    final_lst = []
    string = REPEATED_LST(string)
    if len(string) == 0:
        final_lst = ['']
    for item in string:
         final_lst.append('\\' + to_repeat + '{' + item + '}')
    return final_lst

def AUDIO(s, audios, intervals, times, gain=None, epsilon=.4):
    for idx, audio in enumerate(audios):
        if idx == 0:
            a = AudioSegment.from_mp3(audio)[1000*intervals[idx][0]:1000*(intervals[idx][1] + epsilon)]
            s.renderer.file_writer.add_audio_segment(a, times[idx])
        else:
            a = AudioSegment.from_mp3(audio)[1000*intervals[idx][0]:1000*(intervals[idx][1] + epsilon)]
            s.renderer.file_writer.add_audio_segment(a, times[idx], gain)

def TEX_TEMPLATE(paperwidth='500pt', linespread='1', fontsize='12pt'):
    documentclass = r"\documentclass[" + fontsize + r", preview]{standalone}"
    preamble = r"\usepackage{amsmath, amssymb}" + "\n" + r"\usepackage[margin=0pt, paperwidth=" + paperwidth + r"]{geometry}" + "\n" + r"\linespread{" + linespread + "}"
    return TexTemplate(documentclass=documentclass, preamble=preamble)
