from manim import *
from subprocess import run

## Thanks to the Manim Community: https://docs.manim.community/en/stable/
## Current manim version: Manim Community v0.5.0
## For more information, please visit:
## https://docs.manim.community/en/stable/tutorials/configuration.html#command-line-arguments
## https://docs.manim.community/en/stable/tutorials/configuration.html#a-list-of-all-cli-flags

## Some command line flags:
## -a : renders multiple Scene classes
## -ql : low quality
## -qm : medium quality
## -qh : high quality
## -qk : 4k quality
## -p : plays the animation once it is rendered
## -f : opens the file browser at the location of the animation
## -i : .gif format

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
    x, y = coord(P)
    if x == 0:
        if y > 0:
            return .5*PI
        elif y == 0:
            return 0
        else:
            return 1.5*PI
    elif y == 0:
        if x > 0:
            return 0 
        else:
            return PI
    elif x > 0:
        return np.arctan(y/x)
    else:
        return np.arctan(y/x) + PI

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

def CR(r=1, O=ORIGIN, c=WHITE, **kwargs) -> Circle:
    """Returns the circle centered at O with radius r."""
    return Circle(c, radius=r, **kwargs).move_to(nparray(O))

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

def WR(*args, settings=False):
    """Write items in args."""
    lst = make_lst(args)
    if settings:
        return [Write(item) for item in lst]
    else:
        return [Write(item) for item in args]

def MAKE(*args):
    """Create items in args."""
    lst = make_lst(args)
    return [Create(item) for item in lst]

def DEL(*args):
    """Uncreate items in args."""
    lst = make_lst(args)
    return [Uncreate(item) for item in lst]

def FO(*args):
    """FadeOut items in args."""
    lst = make_lst(args)
    return [FadeOut(item) for item in lst]

def FI(*args):
    """FadeIn items in args."""
    lst = make_lst(args)
    return [FadeIn(item) for item in lst]

def FIFP(X, P, **kwargs):
    """FadeInFromPoint X from point P."""
    return FadeInFromPoint(X, P, **kwargs)

def COL(*args, c=WHITE):
    """Color items in args with color c."""
    lst = make_lst(args)
    return [item.animate.set_color(c) for item in lst]

def TR(X, Y, settings=False, **kwargs):
    """Transform X by Y."""
    lst_X, lst_Y = make_lst(X), make_lst(Y)
    if settings:
        return [Transform(lst_X[i], lst_Y[i], **kwargs) for i in range(0, len(lst_X))]
    else:
        return [Transform(X, Y, **kwargs)]

def RT(X, Y, settings=False, **kwargs):
    """ReplacementTransform X by Y."""
    lst_X, lst_Y = make_lst(X), make_lst(Y)
    if settings:
        return [ReplacementTransform(lst_X[i], lst_Y[i], **kwargs) for i in range(0, len(lst_X))]
    else:
        return [ReplacementTransform(X, Y, **kwargs)]

def TC(X, Y, settings=False, **kwargs):
    """TransformFromCopy X by Y."""
    lst_X, lst_Y = make_lst(X), make_lst(Y)
    if settings:
        return [TransformFromCopy(lst_X[i], lst_Y[i], **kwargs) for i in range(0, len(lst_X))]
    else:
        return [TransformFromCopy(X, Y, **kwargs)]

def CCT(X, Y, settings=False, **kwargs):
    """CounterclockwiseTransform X by Y."""
    lst_X, lst_Y = make_lst(X), make_lst(Y)
    if settings:
        return [CounterclockwiseTransform(lst_X[i], lst_Y[i], **kwargs) for i in range(0, len(lst_X))]
    else:
        return [CounterclockwiseTransform(X, Y, **kwargs)]

def CT(X, Y, settings=False, **kwargs):
    """ClockwiseTransform X by Y."""
    lst_X, lst_Y = make_lst(X), make_lst(Y)
    if settings:
        return [ClockwiseTransform(lst_X[i], lst_Y[i], **kwargs) for i in range(0, len(lst_X))]
    else:
        return [ClockwiseTransform(X, Y, **kwargs)]

def GC(*args):
    """GrowFromCenter items in args."""
    lst = make_lst(args)
    return [GrowFromCenter(item) for item in lst]

def FORW(s, *args):
    """Bring Forward items in args."""
    lst = make_lst(args)
    if len(lst) > 1:
        s.add_foreground_mobjects(*lst)
    else:
        s.add_foreground_mobject(*lst)

def BACK(s, *args):
    """Bring to Back items in args."""
    lst = make_lst(args)
    s.bring_to_back(*lst)

def ANIM(X):
    """Animate X."""
    return X.animate

def UFF(X, f, **kwargs):
    return UpdateFromFunc(X, f, **kwargs)

def UFAF(X, f, **kwargs):
    return UpdateFromAlphaFunc(X, f, **kwargs)

##-------------------------------------------------------------------------------------------------##

def RUN(path, scene, arguments):
    run(f'manim {path} {scene} {arguments}')