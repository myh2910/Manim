from manim import *

class Thumbnail(Scene):
	def construct(self):
		logo = ImageMobject('assets/2021.png').scale(.5).shift(3*LEFT)
		problem = Tex(r'\textsf{Problema 1}').set_color(GOLD_A).scale(2.2).shift(.6*UP)
		solution = Tex(r"\emph{Soluci\'on}").set_color(TEAL_A).scale(2.1).next_to(problem, DOWN, .7)
		VGroup(problem, solution).shift(3.6*RIGHT + .1*UP)

		self.add(logo, problem, solution)
