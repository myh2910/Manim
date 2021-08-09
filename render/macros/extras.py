from manim.utils.tex import TexTemplate
from .constants import *

def BELONGS_TO(sth=None):
	text = r'\text{ pertenece a '
	if sth:
		text += sth + ' '
	text += '}'
	return text

def tex_template(paperwidth='500pt', linespread='1', fontsize='12pt', extra=None):
	'''My custom TexTemplate.'''
	documentclass = r'\documentclass[' + fontsize + r', preview]{standalone}'
	preamble = r'''\usepackage{amsmath, amssymb}
\usepackage[margin=0pt, paperwidth=''' + paperwidth + r''']{geometry}
\linespread{''' + linespread + '}'
	if extra:
		preamble += '\n' + extra
	return TexTemplate(documentclass=documentclass, preamble=preamble)