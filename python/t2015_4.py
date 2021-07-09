from manim import *

class Thumbnail(Scene):
	def construct(self):
		t1 = Tex('IMO 2015 ', 'Problema 4')
		t2 = Tex(r"Soluci\'on con \textsc{Manim}")

		t1[0].set_color_by_gradient(BLUE_A, BLUE)
		t1[1].set_color_by_gradient(RED_A, RED)
		t2.set_color_by_gradient(GOLD_A, GOLD)
		
		txt = [t1, t2]
		for i in txt:
			i.scale(2.8)
		VGroup(*txt).arrange(DOWN, buff=1)

		self.add(*txt)
