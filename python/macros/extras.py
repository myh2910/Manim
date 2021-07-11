from manim import *

linebreak = r' \\ \hphantom{} \\ '
qquad = r'\qquad'
qqquad = r'\qquad\qquad'
iff = r'\iff &'
angle = r'\angle '

is_cyclic = r"\text{ es c\'iclico}"
are_collinear = r'\text{ son colineales}'
prove_that = r'\text{Demostrar que }'

def item(style='square'):
	if style == 'square':
		bullet = r'\text{\tiny $\blacksquare\,$ }&'
	else:
		bullet = r'$\bullet\,$ '
	return bullet

def belongs_to(sth=None, of=None):
	text = r'\text{ pertenece a '
	if sth:
		text += sth + ' '
	if of:
		text += of + ' '
	text += '}'
	return text

def tex_template(paperwidth='500pt', linespread='1', fontsize='12pt'):
    documentclass = r'\documentclass[' + fontsize + r', preview]{standalone}'
    preamble = r'''\usepackage{amsmath, amssymb}
\usepackage[margin=0pt, paperwidth=''' + paperwidth + r''']{geometry}
\linespread{''' + linespread + '}'
    return TexTemplate(documentclass=documentclass, preamble=preamble)
