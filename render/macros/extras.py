from manim import *
from .constants import *

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