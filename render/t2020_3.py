from manim import *

class Thumbnail(Scene):
	def construct(self):
		logo = ImageMobject('assets/2020.png').scale(1.5).shift(.8*UP)
		problem = Tex(r'\textsf{Problema 3:}').set_color(GOLD_A).scale(2.2)
		solution = Tex(r"\emph{Soluci\'on}").set_color(TEAL_A).scale(2.1)
		VGroup(problem, solution).arrange(RIGHT, .8).shift(1.8*DOWN)

		self.add(logo, problem, solution)
