from render.macros import *

class Video(Scene):
	def construct(self):
		logo = ImageMobject('assets/2021.png').scale(.5)
		# Hola a todos!
		self.play(FadeIn(logo, shift=UP))

		problem = Tex(r'\textsf{Problema 1}').set_color_by_gradient(TEAL_E, TEAL_A).scale(2.2)
		solution = Tex(r"\emph{Solución}").set_color(YELLOW_B).scale(2.1).next_to(problem, DOWN, .1)
		VGroup(problem, solution).shift(3.6*RIGHT + .1*UP)

		# Vamos a resolver
		self.play(AnimationGroup(logo.animate.shift(3*LEFT), Write(problem), lag_ratio=MED_LAG_RATIO))
		# el problema 1
		self.play(problem.animate.shift(.6*UP), FadeIn(solution, shift=UP), lag_ratio=.1, float=linear)
		# de la IMO 2021, que dice así:
		self.wait(1.5)

		problem_statement = Tex(
			r'\textbf{Problema 1.} \ \,\! ',
			r'''Sea $n\geqslant 100$ un entero. Iván escribe cada uno de los números $n,n+1,\dots,2n$ en un \linebreak
naipe diferente. Después de barajar estos $n+1$ naipes, los divide en dos pilas distintas. Probar que \linebreak
al menos una de esas pilas contiene dos naipes tales que la suma de sus números es un cuadrado \linebreak
perfecto.''',
			tex_environment=None,
			tex_template=tex_template('510pt')
		)
		problem_statement[0].set_color_by_gradient(TEAL_E, TEAL_A)
		problem_statement.scale(.5).to_corner(UP)

		shifting_factor = 12
		self.play(
			*[FadeOut(item, shift=shifting_factor*LEFT) for item in [logo, solution]],
			ReplacementTransform(problem[0], problem_statement[0]),
			FadeIn(problem_statement[1], shift=shifting_factor*LEFT)
		)
		# Sea n mayor o igual que 100 un entero. Iván escribe cada uno de los números
		self.wait()

		def naipe(i):
			h, w, r = 2.4, 1.8, .1
			card = Rectangle(BLACK, h, w, stroke_width=1, fill_color=WHITE, fill_opacity=1).round_corners(radius=r)
			border = Rectangle(PURE_BLUE, h, w, stroke_width=2).round_corners(radius=r).scale(.85)
			text = Tex(i).set_color(BLACK).scale(.8)
			return VGroup(card, border, text)

		n1, n2, n3 = naipe('n'), naipe('n+1'), naipe('2n')
		dots = MathTex(r'\ldots')
		VGroup(n1, n2, dots, n3).arrange(RIGHT, .6).shift(.5*DOWN)
		shifting_factor = 2*RIGHT
		self.play(AnimationGroup(
			FadeIn(n1, shift=shifting_factor), # n
			FadeIn(n2, shift=shifting_factor), # n+1
			Write(dots), # hasta
			FadeIn(n3, shift=shifting_factor), # 2n
			lag_ratio=.5, run_time=1
		))
		# en un naipe diferente.
		self.wait()
		self.play(*[FadeOut(obj) for obj in [n1, n2, dots, n3]])

		naipes = [naipe('').shift((i*.1 - .8)*RIGHT + .5*DOWN) for i in range(8)]
		# Después de barajar estos n+1 naipes,
		self.play(AnimationGroup(
			*[FadeIn(obj, shift=shifting_factor) for obj in naipes],
			lag_ratio=.5, run_time=1.2
		))
		self.wait()
