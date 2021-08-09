from render.macros import *

class Video(Scene):
	def construct(self):
		# 1. Solución del problema 3 de la IMO 2020

		logo = ImageMobject('assets/2020.png').scale(1.5).shift(.8*UP)
		problem = Tex(r'\textsf{Problema 3:}').set_color(GOLD_A).scale(2.2)
		solution = Tex(r"\emph{Soluci\'on}").set_color(TEAL_A).scale(2.1)
		VGroup(problem, solution).arrange(RIGHT, .8).shift(1.8*DOWN)
		problem.c1 = problem.copy().set_x(0)

		def get_subtitle(text):
			print(text)
			return Tex(text, tex_template=TexFontTemplates.palatino).scale(.9).to_edge(DOWN, .4)

		def get_background():
			return Rectangle(BLACK, height=.7, width=15, fill_opacity=1).to_edge(DOWN, .4)

		def add_subtitle(text):
			subtitle = get_subtitle(text)
			background = get_background()
			self.add(VGroup(background, subtitle))

		self.play(
			AnimationGroup(FadeIn(logo, shift=UP), Write(problem.c1), lag_ratio=SMALL_LAG_RATIO),
			FadeIn(get_subtitle('Hola a todos! Soy Yohan Min :)')),
			run_time=2
		)
		self.wait()
		add_subtitle('Vamos a resolver el problema 3')
		self.play(AnimationGroup(
			ReplacementTransform(problem.c1, problem), FadeIn(solution, shift=RIGHT),
			lag_ratio=.1, run_time=1
		))
		self.wait(1.5)
		add_subtitle(r"de la IMO 2020, que dice as\'i:")
		self.wait(4)

		# 2. Enunciado del problema

		problem_statement = Tex(
			r'\textbf{Problema 3.} \ \ ',
			r'''Hay $4n$ piedritas de pesos $1,2,3,\dots,4n$. Cada piedrita se colorea de uno de $n$ colores de manera que hay cuatro piedritas de cada color. Demuestre que podemos colocar las piedritas en dos montones de tal forma que las siguientes dos condiciones se satisfacen:
		\begin{itemize}
		\item Los pesos totales de ambos montones son iguales.
		\item Cada mont\'on contiene dos piedritas de cada color.
		\end{itemize}''',
			tex_environment=None,
			tex_template=tex_template('512.34pt', extra=r'''\usepackage{enumitem}
		\setlist[itemize]{label=\rule[.2ex]{.7ex}{.7ex}\,}''')
		)
		problem_statement[0].set_color(TEAL)
		problem_statement.scale(.5).to_corner(UP)
		separator = Line(stroke_width=1).set_length(15).next_to(problem_statement, DOWN, .5)

		add_subtitle('Hay $4n$ piedritas de pesos')
		self.play(
			FadeOut(logo, problem, solution),
			AnimationGroup(FadeIn(problem_statement, shift=UP), run_time=1.5),
			AnimationGroup(Create(separator), run_time=2)
		)
		def pebble(i, radius=.6, scale=1, color=GRAY):
			pebble = Circle(radius, color=color, fill_opacity=1)
			text = Tex(i).scale(scale)
			return VGroup(pebble, text)

		pebbles = [pebble(i) for i in ['1', '2', '3', '4n']]
		cdots = MathTex('\cdots').scale(1.2)
		VGroup(*pebbles[:-1], cdots, pebbles[3]).arrange(RIGHT, .6).next_to(separator, DOWN, .5)
		brace = Brace(VGroup(*pebbles))
		piedritas = Tex('$4n$ piedritas').next_to(brace, DOWN)

		add_subtitle(r'$1,2,3,\dots,4n$.')
		self.play(AnimationGroup(
			*[FadeIn(obj, shift=.5*UP) for obj in pebbles[:-1]],
			Write(cdots),
			FadeIn(pebbles[3], shift=UP),
			lag_ratio=SMALL_LAG_RATIO, run_time=2
		))
		self.play(GrowFromCenter(brace), Write(piedritas))
		self.wait(.5)

		add_subtitle('Cada piedrita se colorea de uno de $n$ colores')
		self.play(AnimationGroup(
			*[AnimationGroup(*[pebbles[i][j].animate.set_color(k) for j, k in [(0, c), (1, WHITE)]])
				for i, c in enumerate([GREEN, ORANGE, TEAL, PURPLE])
			], lag_ratio=MED_LAG_RATIO, run_time=2
		))
		self.wait(.5)
		add_subtitle('de manera que hay cuatro piedritas de cada color.')
		self.wait(2.5)
		add_subtitle('Demuestre que podemos colocar las piedritas')
		self.wait(2)
		add_subtitle('en dos montones de tal forma que')
		self.wait(2)
		add_subtitle('los pesos totales de ambos montones son iguales')
		self.wait(2.5)
		add_subtitle(r"y cada mont\'on contiene dos piedritas de cada color.")
		self.wait(4)

		# 3. Solución oficial (usando ciclos eulerianos)

		add_subtitle("Vamos a presentar una de las soluciones oficiales,")
		self.wait(2.5)
		add_subtitle(r"(mi soluci\'on durante la prueba fue muy similar a la oficial)")
		self.wait(1.5)
		add_subtitle('en donde usaremos los ciclos eulerianos.')
		self.wait(4)

		# 4. La idea principal y el conjunto S

		self.play(VGroup(*pebbles, cdots).animate.scale(.6).next_to(separator, DOWN, .5), FadeOut(brace, piedritas, shift=.5*DOWN))
		add_subtitle('La idea principal es notar lo siguiente:')
		self.wait(2)

		# idea principal
		key_idea = MathTex(
			'1', '+', '4n', #0, 1, 2
			'=', #3
			'2', '+', '(4n-1)', #4, 5, 6
			'=', #7
			r'\dots', #8
			'=', #9
			'2n', '+', '(2n+1)' #10, 11, 12
		).next_to(VGroup(*pebbles), DOWN, .5)
		add_subtitle(r'$1+4n=2+(4n-1)=\dots=2n+(2n+1)$.')
		self.play(AnimationGroup(
			Write(key_idea[:3]),
			Write(key_idea[3]),
			Write(key_idea[4:7]),
			*[Write(key_idea[i]) for i in [7, 8, 9]],
			Write(key_idea[10:]),
			lag_ratio=MED_LAG_RATIO, run_time=4
		))
		self.wait(3)

		# conjunto S
		set_S = MathTex(
			r'\{', '1', ',', '4n', r'\}', #0, 1, 2, 3, 4
			',', #5
			r'\{', '2', ',', '4n-1', r'\}', #6, 7, 8, 9, 10
			',', #11
			r'\dots', #12
			',', #13
			r'\{', '2n', ',', '2n+1', r'\}', #14, 15, 16, 17, 18
			r'\,\rightarrow\,', #19
			'S' #20
		).move_to(key_idea, UP)
		add_subtitle('Sea $S$ el conjunto de los $2n$ pares de piedritas')
		self.wait(2.5)
		add_subtitle('cuyos pesos suman $4n+1$.')
		self.play(AnimationGroup(
			AnimationGroup(*[ReplacementTransform(key_idea[i], set_S[j]) for i, j in enumerate(
				[1, 2, 3, 5, 7, 8, 9, 11, 12, 13, 15, 16, 17]
			)]),
			AnimationGroup(*[FadeIn(set_S[i]) for i in [0, 4, 6, 10, 14, 18, 19, 20]]),
			lag_ratio=.5
		))
		self.wait(2)

		add_subtitle('Nos basta dividir $S$ en dos conjuntos,')
		self.wait(2)
		add_subtitle('cada uno con $n$ pares de piedritas,')
		self.wait(2)
		add_subtitle('de modo que cada conjunto contenga dos piedritas de cada color.')
		self.wait(4)

		# 5. Multigrafo G

		self.play(FadeOut(*pebbles, cdots, shift=.5*UP), set_S.animate.next_to(separator, DOWN, .5))
		multigraph = Tex('$G=$ ', 'multigrafo', r' con $n$ v\'ertices').next_to(set_S, DOWN, .5)
		brace = Brace(multigraph[1], buff=0)
		definition = Tex(r'grafo que permite\\ aristas m\'ultiples').scale(.8).next_to(brace, DOWN, SMALL_BUFF)
		loop = VGroup(CubicBezier(ORIGIN, 1.5*UP, 1.5*RIGHT, ORIGIN), Dot(color=GREEN))
		multiple_edges = VGroup(
			CubicBezier(ORIGIN, [.2, .5, 0], [1.3, .7, 0], [1.5, .5, 0]),
			CubicBezier(ORIGIN, [.3, -.2, 0], [1.5, .2, 0], [1.5, .5, 0]),
			Dot(color=ORANGE),
			Dot([1.5, .5, 0], color=TEAL)
		).shift(.8*DR)
		arrow = CurvedArrow(2*LEFT, RIGHT, radius=4, tip_length=.2).shift(1.1*RIGHT + 2*DOWN)
		VGroup(loop, multiple_edges).move_to(3.8*RIGHT + 1.8*DOWN)

		add_subtitle(r"Sea $G$ un multigrafo con $n$ v\'ertices")
		self.play(AnimationGroup(*[Write(i) for i in multigraph], lag_ratio=MED_LAG_RATIO))
		self.wait(.5)
		add_subtitle(r"(es decir, un grafo que permite aristas m\'ultiples),")
		self.play(GrowFromCenter(brace), Write(definition))

		self.play(VGroup(multigraph, brace, definition).animate.shift(1.8*LEFT))
		self.play(Create(arrow), run_time=.7)
		add_subtitle(r"de modo que cada v\'ertice corresponde a un color.")
	
		self.add_foreground_mobjects(loop[1])
		self.play(GrowFromCenter(loop[1]), run_time=.7)
		self.play(Create(loop[0]), run_time=.8)
		
		self.add_foreground_mobjects(multiple_edges[2], multiple_edges[3])
		self.play(*[GrowFromCenter(multiple_edges[i]) for i in [2, 3]], run_time=.7)
		self.play(AnimationGroup(*[Create(multiple_edges[i]) for i in [0, 1]], lag_ratio=.5, run_time=.8))
		self.wait(2)

		add_subtitle('Para cada par de piedritas en $S$,')
		self.play(
			FadeOut(set_S, shift=.5*UP),
			multigraph.animate.next_to(separator, DOWN, .5),
			FadeOut(brace, definition, arrow, loop[0], multiple_edges[:2], shift=.5*DOWN),
			*[FadeOut(dot, shift=.5*DOWN) for dot in [loop[1], *multiple_edges[2:]]]
		)
		self.wait()
		add_subtitle(r"agregamos una arista entre los v\'ertices")
		self.wait(2.5)
		add_subtitle('que corresponden a los colores de esas piedritas.')
		self.wait(4)

		# 6. Estrategia

		rojas = Tex('$2$ rojas').set_color(RED)
		azules = Tex('$2$ azules').set_color(BLUE)
		VGroup(rojas, azules).arrange(DOWN, aligned_edge=LEFT)
		brace = Brace(VGroup(rojas, azules), LEFT)
		aristas = MathTex(r'4\text{ aristas}=').next_to(brace, LEFT).shift(.05*UP)
		coloring = VGroup(rojas, azules, brace, aristas).next_to(multigraph, DOWN, .5).set_x(0)
		add_subtitle(r"Note que cada v\'ertice tiene grado $4$.")
		self.play(AnimationGroup(Write(aristas), GrowFromCenter(brace), Write(rojas), Write(azules), lag_ratio=MED_LAG_RATIO), run_time=2)
		self.wait()
		add_subtitle(r"Nos bastar\'ia pintar cada arista de $G$ de rojo o azul")
		self.wait(3)
		add_subtitle(r"de modo que cada v\'ertice tenga")
		self.wait(2)
		add_subtitle('grado $2$ de aristas rojas y $2$ de aristas azules.')
		self.wait(4)
		self.play(FadeOut(multigraph, shift=.5*UP), coloring.animate.next_to(separator, DOWN, .5))
	
		# 7. La componente conexa G' de G y el ciclo euleriano C en G'

		component = MathTex("G'", '=', r'\text{componente conexa de }G').next_to(coloring, DOWN, .5)
		add_subtitle("Sea $G'$ una componente conexa de $G$.")
		self.play(AnimationGroup(*[Write(i) for i in component], lag_ratio=MED_LAG_RATIO))
		self.wait(2)

		eulerian_path_theorem = Tex(
			r'\begin{theorem}[Ciclo Euleriano] Sea $G$ un grafo conexo con todos sus v\'ertices de grados pares. Entonces, existe un ciclo que pasa por cada arista de $G$ exactamente una vez.\end{theorem}',
			tex_environment=None,
			tex_template=tex_template(
				'512.34pt',
				extra=r'''\usepackage{amsthm,thmtools}
		\declaretheoremstyle[
		headfont=\sffamily\bfseries,
		headpunct={\\[3pt]},
		postheadspace={0pt}
		]{thmbox}
		\declaretheorem[style=thmbox,name=Teorema,numbered=no]{theorem}'''
			)
		).scale(.5).next_to(separator, DOWN, .5)

		add_subtitle(r"Como cada v\'ertice tiene grado par,")
		self.play(FadeOut(coloring, component, shift=.5*UP), FadeIn(eulerian_path_theorem, shift=.5*UP))
		self.wait()
		add_subtitle("existe un ciclo euleriano $C$ en $G'$.")
		self.wait()

		circuit_C = MathTex('C', '=', r"\text{ciclo euleriano en }G'").next_to(eulerian_path_theorem, DOWN, .5)
		self.play(AnimationGroup(*[Write(i) for i in circuit_C], lag_ratio=MED_LAG_RATIO))
		self.wait(1.5)

		# 8. El número de aristas de G' es par

		handshaking_lemma = Tex(
			r'\begin{lemma} Dado un grafo $G=(V,E)$: \[\sum_{v\in V}\deg{v}=2\left|E\right|.\]\end{lemma}',
			tex_environment=None,
			tex_template=tex_template(
				'512.34pt',
				extra=r'''\usepackage{amsthm,thmtools}
		\declaretheoremstyle[
		headfont=\sffamily\bfseries,
		bodyfont=\normalfont,
		spaceabove=2pt,
		spacebelow=1pt,
		headpunct={ --- }
		]{thmbox}
		\declaretheorem[style=thmbox,name=Lema,numbered=no]{lemma}'''
			)
		).scale(.5).next_to(eulerian_path_theorem, DOWN, .3, aligned_edge=LEFT)
		add_subtitle(r"Sabemos que el doble del n\'umero de aristas de $G'$")
		self.play(FadeOut(circuit_C, shift=.5*UP), FadeIn(handshaking_lemma, shift=.5*UP))
		self.wait(2)
		add_subtitle(r"es igual a la suma de los grados de los v\'ertices de $G'$,")
		self.wait(3.5)
		add_subtitle(r"y cada v\'ertice de $G'$ tiene grado $4$,")
		self.wait(3)
		add_subtitle(r"entonces el n\'umero de aristas de $G'$ es par.")
		self.wait(4)

		# 9. Fin

		add_subtitle('Luego, podemos pintar las aristas de $C$')
		self.wait(2.5)
		add_subtitle('de rojo y azul alternadamente,')
		self.wait(2)
		add_subtitle('de modo que cualesquiera dos aristas adyacentes en $C$')
		self.wait(3)
		add_subtitle('tenga diferentes colores.')
		self.wait(4)

		add_subtitle(r"Entonces en $G'$, cada v\'ertice tiene")
		self.wait(2)
		add_subtitle(r"igual grado de aristas rojas y azules.")
		self.wait(3)

		add_subtitle(r"Por lo tanto, podemos lograr que cada v\'ertice de $G$")
		self.wait(3)
		add_subtitle('tenga grado $2$ de aristas rojas y $2$ de aristas azules,')
		self.wait(3.5)
		add_subtitle(r"que es lo que quer\'iamos probar.")
		self.wait(4)

		# 10. Ejemplo con n=5

		add_subtitle(r'Terminaremos mostrando un ejemplo con $n=5$.')
		self.play(*[FadeOut(obj, shift=DOWN) for obj in [eulerian_path_theorem, handshaking_lemma]])
		self.wait(2)
		self.add(get_background())
		self.wait()

		# 4*5=20 piedritas
		vertices = [
			{'color': GREEN},
			{'color': ORANGE},
			{'color': TEAL},
			{'color': MAROON},
			{'color': PURPLE}
		]
		pebble_lst = [
			{'color': 0},
			{'color': 3},
			{'color': 0},
			{'color': 0},
			{'color': 1},
			{'color': 2},
			{'color': 2},
			{'color': 1},
			{'color': 4},
			{'color': 2},
			{'color': 1},
			{'color': 3},
			{'color': 4},
			{'color': 3},
			{'color': 4},
			{'color': 4},
			{'color': 1},
			{'color': 3},
			{'color': 2},
			{'color': 0}
		]
		for i in range(20):
			obj = pebble_lst[i]
			obj['dot'] = pebble(str(i+1), .2, .5, vertices[obj['color']]['color'])
			self.add_foreground_mobject(obj['dot'])

		pebbles = [obj['dot'] for obj in pebble_lst]
		VGroup(*pebbles).arrange(RIGHT, .2).next_to(separator, DOWN, .5)

		self.play(AnimationGroup(
			*[FadeIn(obj, shift=.5*UP) for obj in pebbles],
			lag_ratio=.1, run_time=1.5
		))

		# vértices del multigrafo G
		circle = Circle(1).shift(2.2*DOWN)
		for i, j in enumerate([.5, .9, 1.3, 1.7, .1]):
			obj = vertices[i]
			dot = Dot(circle.point_at_angle(j*PI), .09, color=obj['color'])
			self.add_foreground_mobject(dot)
			obj['dot'] = dot
		dots = [obj['dot'] for obj in vertices]
		self.play(FadeIn(VGroup(*dots), shift=.5*UP))

		# aristas de G
		pebble_1 = pebbles[0].copy().scale(2.5)
		pebble_2 = pebbles[19].copy().scale(2.5)
		pebble_3 = pebbles[1].copy().scale(1.2)
		pebble_4 = pebbles[18].copy().scale(1.2)
		for obj in [pebble_3, pebble_4]:
			obj[0].set_color(DARK_GRAY)
			obj[1].set_color(GRAY)
		arrow_1 = Arrow(ORIGIN, UP, color=BLUE_E).next_to(pebbles[0], DOWN, SMALL_BUFF)
		arrow_2 = arrow_1.copy().next_to(pebbles[19], DOWN, SMALL_BUFF)

		VGroup(pebble_1, pebble_2).arrange(RIGHT, .5).move_to(2.5*LEFT + 2*DOWN)
		VGroup(pebble_3, pebble_4).arrange(RIGHT, .4).move_to(2.5*LEFT + 3*DOWN)
		self.play(
			VGroup(*dots).animate.shift(2.5*RIGHT),
			*[FadeIn(obj, shift=.5*UP) for obj in [
				arrow_1, arrow_2, pebble_1, pebble_2, pebble_3, pebble_4
			]]
		)
		self.wait(.5)

		edges = []
		coords = [obj.get_center() for obj in dots]
		for obj in [
			CubicBezier(coords[0], coords[0]+[-.4, .6, 0], coords[0]+[.4, .6, 0], coords[0]),
			CubicBezier(coords[3], coords[3]+[-.2, .15, 0], coords[2]+[.2, .15, 0], coords[2]),
			Line(coords[3], coords[0]),
			Line(coords[0], coords[1]),
			CubicBezier(coords[1], coords[1]+[.3, -.2, 0], coords[4]+[-.3, -.2, 0], coords[4]),
			Line(coords[4], coords[2]),
			CubicBezier(coords[2], coords[2]+[.2, -.15, 0], coords[3]+[-.2, -.15, 0], coords[3]),
			CubicBezier(coords[1], coords[1]+[.3, .2, 0], coords[4]+[-.3, .2, 0], coords[4]),
			Line(coords[4], coords[3]),
			Line(coords[2], coords[1])
		]:
			edges.append(obj)

		running, i = True, 0
		duration = .75
		while running:
			if i == 7:
				running = False
			d1, d2 = dots[pebble_lst[i]['color']], dots[pebble_lst[19-i]['color']]
			p1, p2 = pebbles[i+1].copy().scale(2.5), pebbles[18-i].copy().scale(2.5)
			p3, p4 = pebbles[i+2].copy().scale(1.2), pebbles[17-i].copy().scale(1.2)
			for obj in [p3, p4]:
				obj[0].set_color(DARK_GRAY)
				obj[1].set_color(GRAY)
			VGroup(p1, p2).arrange(RIGHT, .5).move_to(2.5*LEFT + 2*DOWN)
			VGroup(p3, p4).arrange(RIGHT, .4).move_to(2.5*LEFT + 3*DOWN)

			self.play(
				ReplacementTransform(pebble_1.copy(), d1),
				ReplacementTransform(pebble_2.copy(), d2),
				run_time=duration
			)
			self.play(Create(edges[i]), run_time=duration)
			self.play(
                arrow_1.animate.next_to(pebbles[i+1], DOWN, SMALL_BUFF),
                arrow_2.animate.next_to(pebbles[18-i], DOWN, SMALL_BUFF),
                ReplacementTransform(pebble_3, p1),
                ReplacementTransform(pebble_4, p2),
                *[FadeOut(obj) for obj in [pebble_1, pebble_2]],
                *[FadeIn(obj, shift=.5*UP) for obj in [p3, p4]],
                run_time=duration
            )
			pebble_1, pebble_2, pebble_3, pebble_4 = p1, p2, p3, p4
			i += 1

		d1, d2 = dots[pebble_lst[8]['color']], dots[pebble_lst[11]['color']]
		p1, p2 = pebbles[9].copy().scale(2.5), pebbles[10].copy().scale(2.5)
		VGroup(p1, p2).arrange(RIGHT, .5).move_to(2.5*LEFT + 2*DOWN)
		self.play(
			ReplacementTransform(pebble_1.copy(), d1),
			ReplacementTransform(pebble_2.copy(), d2),
			run_time=duration
		)
		self.play(Create(edges[8]), run_time=duration)
		self.play(
            arrow_1.animate.next_to(pebbles[9], DOWN, SMALL_BUFF),
            arrow_2.animate.next_to(pebbles[10], DOWN, SMALL_BUFF),
            ReplacementTransform(pebble_3, p1),
            ReplacementTransform(pebble_4, p2),
            *[FadeOut(obj) for obj in [pebble_1, pebble_2]],
            run_time=duration
        )
		d1, d2 = dots[pebble_lst[9]['color']], dots[pebble_lst[10]['color']]
		self.play(
			ReplacementTransform(p1, d1),
			ReplacementTransform(p2, d2),
			run_time=duration
		)
		self.play(Create(edges[9]), run_time=duration)
		self.play(
			FadeOut(arrow_1, arrow_2, shift=.5*DOWN),
			VGroup(*edges, *dots).animate.shift(2.5*LEFT)
		)

		# ciclo euleriano
		colored_edges = [edges[i].copy().set_color([RED, BLUE][j]) for i, j in enumerate([
			0, 0, 1, 1, 0, 1, 0, 0, 1, 1
		])]
		self.play(AnimationGroup(
			*[Create(colored_edges[i]) for i in [0, 3, 4, 8, 1, 9, 7, 5, 6, 2]],
			lag_ratio=SMALL_LAG_RATIO
		))
		self.remove(*edges)
		self.wait()

		# agrupamiento
		rearrange = []
		for idx, i in enumerate([0, 0, 1, 0, 0, 1, 0, 0, 0, 0]):
			objs = [pebbles[k].copy() for k in [idx, 19-idx]]
			VGroup(*objs).arrange(RIGHT, .6)
			if i == 0:
				line = Line(*[obj.get_center() for obj in objs])
			else:
				line = Line(*[obj.get_center() for obj in objs[::-1]])
			rearrange.append([line, *objs])

		for j, lst in enumerate([[0, 1, 4, 6, 7], [2, 3, 5, 8, 9]]):
			for i in lst:
				rearrange[i][0].set_color([RED, BLUE][j])
			p = [VGroup(*objs) for objs in [rearrange[i] for i in lst]]
			VGroup(*p).arrange(DOWN, .15).shift(2.1*DOWN + 3.6*LEFT*(-1)**j)

		for i in range(10):
			edge = colored_edges[i]
			vertex = [dots[pebble_lst[k]['color']].copy() for k in [i, 19-i]]
			objs = rearrange[i]
			self.play(ReplacementTransform(VGroup(edge, *vertex), VGroup(*objs)))

		shift = [[obj[1].copy(), obj[2].copy()] for obj in rearrange]
		for idx, i in enumerate([0, 0, 1, 1, 0, 1, 0, 0, 1, 1]):
			[x, y] = shift[idx]
			lst = [2.6, 2.2]
			x.shift(lst[i]*RIGHT*(-1)**i)
			y.shift(lst[1-i]*RIGHT*(-1)**i)

		self.play(
			*[FadeOut(obj, shift=.5*DOWN) for obj in dots],
			*[FadeOut(obj[0]) for obj in rearrange]
		)
		self.play(ReplacementTransform(
			VGroup(*[i for obj in rearrange for i in obj[1:]]),
			VGroup(*[i for obj in shift for i in obj])
		))
		surround = [
			SurroundingRectangle(
				VGroup(*[i for idx in lst for i in shift[idx]]), c, .2
			).round_corners(.3) for lst, c in [([0, 1, 4, 6, 7], RED), ([2, 3, 5, 8, 9], BLUE)]
		]
		self.play(AnimationGroup(*[Create(i) for i in surround], lag_ratio=SMALL_LAG_RATIO))
		self.wait(3)

		self.play(*[FadeOut(obj, shift=DOWN) for obj in [
			problem_statement, separator, *pebbles, *[i for obj in shift for i in obj], *surround
		]])
		self.wait()