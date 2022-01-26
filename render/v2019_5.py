from render.macros import *

class Video(ThreeDScene):
	def construct(self):
		#self.set_camera_orientation(phi=-25 * DEGREES, theta=70 * DEGREES)
		# 1. Solución del problema 3 de la IMO 2020

		logo = ImageMobject('assets/2019.png').scale(1).shift(2*LEFT)
		problem = Tex(r'\textsf{Problema 5}').set_color(GOLD_B).scale(2.2)
		solution = Tex(r"\emph{Solución}").set_color(TEAL_A).scale(2.1)
		VGroup(problem, solution).arrange(DOWN, .7)
		Group(logo, VGroup(problem, solution)).arrange(RIGHT, .9)
		problem.c1 = problem.copy().set_y(0)

		self.play(AnimationGroup(
			FadeIn(logo, shift=LEFT), Write(problem.c1),
			lag_ratio=SMALL_LAG_RATIO
		))
		self.wait()
		self.play(AnimationGroup(
			ReplacementTransform(problem.c1, problem), FadeIn(solution, shift=RIGHT),
			lag_ratio=.1
		))
		self.wait(1.5)
		self.wait(4)

		# 2. Enunciado del problema

		problem_statement = Tex(
				r'\textbf{Problema 5.} ',
			r'''El Banco de Bath emite monedas con una $H$ en una cara y una $T$ en la otra. Harry tiene $n$ monedas de este tipo alineadas de izquierda a derecha. \'El realiza repetidamente la siguiente operación: si hay exactamente $k>0$ monedas con la $H$ hacia arriba, Harry voltea la $k$-ésima moneda contando desde la izquierda; en caso contrario, todas las monedas tienen la $T$ hacia arriba y él se detiene. Por ejemplo, si $n=3$ y la configuración inicial es $THT$, el proceso sería $THT\to HHT\to HTT\to TTT$, que se detiene después de tres operaciones.
\begin{enumerate}[label=(\alph*)]
	\item Demostrar que para cualquier configuración inicial que tenga Harry, el proceso se detiene después de un número finito de operaciones.
	\item Para cada configuración inicial $C$, sea $L(C)$ el número de operaciones que se realizan hasta que Harry se detiene. Por ejemplo, $L(THT)=3$ y $L(TTT)=0$. Determinar el valor promedio de $L(C)$ sobre todas las $2^n$ posibles configuraciones iniciales de $C$.
\end{enumerate}''',
			tex_environment=None,
			tex_template=tex_template('510pt', extra=r'''\usepackage{enumitem}
		\setlist[itemize]{label=\rule[.2ex]{.7ex}{.7ex}\,}''')
		)
		problem_statement[0].set_color(GOLD_B)
		problem_statement.scale(.5)

		self.play(
			FadeOut(logo, problem, solution),
			AnimationGroup(FadeIn(problem_statement, shift=UP), run_time=1.5),
		)
		self.wait(3)
