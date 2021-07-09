from asymptote import *

class Video(Scene):
	def construct(self):
		t1 = Tex('IMO 2015, ', 'Problema 4')
		t1.set_color_by_tex_to_color_map({'IMO 2015, ': BLUE, 'Problema 4': RED})
		t1.scale(1.6)

		linebreak = r' \\ \hphantom{} \\ '
		isquare = r'\text{\tiny $\blacksquare\,$ }&'
		#ii = r'$\bullet\,$ '
		iff = r'\iff &'

		t2 = Tex(
			r'\textbf{Problema 4.} ',
			r"El tri\'angulo $ABC$ tiene circunferencia circunscrita $\Omega$ y circuncentro $O$. Una circunferencia $\Gamma$ de centro $A$ corta al segmento $BC$ en los puntos $D$ y $E$ tales que $B$, $D$, $E$ y $C$ son todos diferentes y est\'an en la recta $BC$ en este orden. Sean $F$ y $G$ los puntos de intersecci\'on de $\Gamma$ y $\Omega$, tales que $A$, $F$, $B$, $C$ y $G$ est\'an sobre $\Omega$ en este orden. Sea $K$ el segundo punto de intersecci\'on de la circunferencia circunscrita al tri\'angulo $BDF$ y el segmento $AB$. Sea $L$ el segundo punto de intersecci\'on de la circunferencia circunscrita al tri\'angulo $CGE$ y el segmento $CA$." + linebreak + \
			r"Supongamos que las rectas $FK$ y $GL$ son distintas y se cortan en el punto $X$. Demostrar que $X$ est\'a en la recta $AO$.",
			tex_environment=None,
			tex_template=TexTemplateLibrary.simple
		)
		t2.set_color_by_tex('Problema', RED)
		
		t3 = Tex(
			r"\hphantom{\textbf{Problema 4.} }El tri\'angulo $ABC$ tiene circunferencia circunscrita $\Omega$ y circuncentro $O$. Una circunferencia $\Gamma$ de centro $A$ corta al segmento $BC$ en los puntos $D$ y $E$ tales que $B$, $D$, $E$ y $C$ son todos diferentes y est\'an en la recta $BC$ en este orden. Sean $F$ y $G$ los puntos de intersecci\'on de $\Gamma$ y $\Omega$, tales que $A$, $F$, $B$, $C$ y $G$ est\'an sobre $\Omega$ en este orden. Sea $K$ el segundo punto de intersecci\'on de la circunferencia circunscrita al tri\'angulo $BDF$ y el segmento $AB$. Sea $L$ el segundo punto de intersecci\'on de la circunferencia circunscrita al tri\'angulo $CGE$ y el segmento $CA$." + linebreak + \
			r"Supongamos que las rectas $FK$ y $GL$ son distintas y se cortan en el punto $X$. Demostrar que $X$ est\'a en la recta $AO$.",
			tex_environment=None,
			tex_template=TexTemplateLibrary.simple
		)
		for item in [t2, t3]:
			item.scale(.7).to_corner(UP)

		t4 = VGroup(t2[0], t3)

		t5 = MathTex(
			#    0    1    2    3    4    5    6    7    8    9   10   11
			isquare, 'A', 'D', '=', 'A', 'E', '=', 'A', 'F', '=', 'A', 'G' + linebreak,
			#   12   13   14   15   16   17
			isquare, 'B', 'D', 'K', 'F', r"\text{ es c\'iclico}" + linebreak,
			#   18   19   20   21   22   23
			isquare, 'C', 'G', 'L', 'E', r"\text{ es c\'iclico}" + linebreak,
			#                              24   25   26   27   28   29   30
			isquare + r'\text{Demostrar que }', 'A', ',', 'X', ',', 'O', r'\text{ son colineales}',
			tex_environment='align*',
			tex_template=TexTemplateLibrary.simple
		)
		t6 = MathTex(
			# 0    1    2    3    4    5
			'&A', ',', 'X', ',', 'O', r'\text{ son colineales}' + linebreak,
			#6    7                                        8    9   10
			iff, 'X', r'\text{ pertenece a la mediatriz de }', 'F', 'G' + linebreak,
			#11         12   13   14   15   16          17   18   19   20
			iff, r'\angle ', 'K', 'F', 'G', '=', r'\angle ', 'L', 'G', 'F',
			tex_environment='align*',
			tex_template=TexTemplateLibrary.simple
		)
		t7 = MathTex(
			isquare + 'AD=AE=AF=AG' + linebreak + \
			isquare + r"BDKF\text{ es c\'iclico}" + linebreak + \
			isquare + r"CGLE\text{ es c\'iclico}" + linebreak + \
			#                               0    1           2    3    4    5           6    7    8    9
			isquare + r'\text{Demostrar que }', r'\angle ', 'K', 'F', 'G', '=', r'\angle ', 'L', 'G', 'F',
			tex_environment='align*',
			tex_template=TexTemplateLibrary.simple
		)
		t8 = MathTex(
			isquare + 'AD=AE=AF=AG' + linebreak + \
			isquare + r"BDKF\text{ es c\'iclico}" + linebreak + \
			isquare + r"CGLE\text{ es c\'iclico}" + linebreak + \
			#                               0    1    2    3
			isquare + r'\text{Demostrar que }', 'x', '=', 'y',
			tex_environment='align*',
			tex_template=TexTemplateLibrary.simple
		)
		t9 = MathTex(
			#0    1    2     3    4    5    6
			'C', '-', 'x', '&=', 'C', '-', r'y \\ ',
			#7     8    9
			'x', '&=', 'y',
			tex_environment='align*',
			tex_template=TexTemplateLibrary.simple
		)
		for item in [t5, t6, t7, t8]:
			item.set_color(WHITE).scale(.6)
		t5.shift(4*RIGHT)
		for item in [t6, t7, t8]:
			item.move_to(t5, aligned_edge=LEFT)
		t9.move_to(t5)

		k = 3.3
		A, B, C = k*dir(110), k*dir(200), k*dir(340)

		HA = extension(A+B+C, A, B, C)
		s = .3
		D, E = (1-s)*HA + s*B, (1+s)*HA - s*B

		r = distance(A, D)
		l = dir(2*degrees(np.arcsin(r/(2*k))))
		F, G = A*l, A/l

		O1 = circumcenter(B, D, F)
		O2 = circumcenter(C, G, E)
		K = 2*foot(O1, A, B) - B
		L = 2*foot(O2, A, C) - C

		X = extension(F, K, G, L)

		dot_O = DOT(origin)
		dot_A = DOT(A)
		dot_B = DOT(B)
		dot_C = DOT(C)
		dot_D = DOT(D)
		dot_E = DOT(E)
		dot_F = DOT(F)
		dot_G = DOT(G)
		dot_K = DOT(K)
		dot_L = DOT(L)
		dot_X = DOT(X)

		circle_omega = CR(k, c=BLUE)
		circle_BDF = CP(B, O1, GREEN)
		circle_CGE = CP(C, O2, GREEN)
		circle_gamma = CP(D, A, GREEN)

		line_FX = LINE(F, X, GREEN)
		line_GX = LINE(G, X, GREEN)
		line_AF = LINE(A, F, PURPLE)
		line_AG = LINE(A, G, PURPLE)
		line_AB = LINE(A, B, RED)
		line_BC = LINE(B, C, RED)
		line_CA = LINE(C, A, RED)

		dashed_FX = DashedVMobject(line_FX).set_color(GREEN)
		dashed_GX = DashedVMobject(line_GX).set_color(GREEN)

		r, l = 3.5, 3
		for item in [
			circle_omega,
			dot_O, dot_A, dot_B, dot_C,
			line_AB, line_BC, line_CA
		]: item.shift(r*RIGHT)
		for item in [
			dot_K, dot_L,
			circle_BDF, circle_CGE,
			dot_X,
			line_FX, line_GX, dashed_FX, dashed_GX, line_AF, line_AG
		]: item.shift(l*LEFT)

		f = .5
		label_omega = MP(r'$\Omega$', circle_omega, UP, f)
		label_gamma = MP(r'$\Gamma$', circle_gamma, RIGHT, f)
		label_O = MP('$O$', dot_O, DOWN, f)
		label_A = MP('$A$', dot_A, UP, f)
		label_B = MP('$B$', dot_B, B, f)
		label_C = MP('$C$', dot_C, C, f)
		label_D = MP('$D$', dot_D, DOWN, f)
		label_E = MP('$E$', dot_E, DOWN, f)
		label_F = MP('$F$', dot_F, LEFT, f)
		label_G = MP('$G$', dot_G, RIGHT, f)
		label_K = MP('$K$', dot_K, K, f)
		label_L = MP('$L$', dot_L, L, f)
		label_X = MP('$X$', dot_X, DOWN, f)

		dots_ABC = VGroup(dot_A, dot_B, dot_C)
		dots_FDEG = VGroup(dot_F, dot_D, dot_E, dot_G)
		dots_KBDF = VGroup(dot_K, dot_B, dot_D, dot_F)
		dots_LCGE = VGroup(dot_L, dot_C, dot_G, dot_E)
		dots_AXO = VGroup(dot_A, dot_X, dot_O)

		lines_ABC = VGroup(line_AB, line_BC, line_CA)
		lines_FX_GX = VGroup(line_FX, line_GX)
		lines_AF_AG = VGroup(line_AF, line_AG)
		
		dashed_FX_GX = VGroup(dashed_FX, dashed_GX)

		labels_ABC = [label_A, label_B, label_C]
		labels_FDEG = [label_F, label_D, label_E, label_G]
		
		self.add_sound('assets/2015_4.mp3')

		self.play(Write(t1), run_time=4)
		self.wait()
		self.play(FadeOut(t1), TransformFromCopy(t1[1], t2[0]))
		self.play(Create(t3), run_time=4)
		self.wait(4)
		self.play(t4.animate.scale(.5).shift(UP + 3.5*LEFT))

		for i in [dot_O, label_O]:
			self.play(GrowFromCenter(i))
		self.add_foreground_mobjects(dot_O, label_O)
		for i in [circle_omega, label_omega]:
			self.play(GrowFromCenter(i))
		self.add_foreground_mobject(label_omega)

		self.play(GrowFromCenter(dots_ABC))
		self.play(*[GrowFromCenter(i) for i in labels_ABC])
		self.add_foreground_mobjects(*dots_ABC, *labels_ABC)
		self.play(Create(lines_ABC))

		change_1 = VGroup(
			circle_omega,
			*lines_ABC,
			dot_O, *dots_ABC,
			label_O, label_omega, *labels_ABC
		)
		self.play(FadeOut(t4))
		self.play(change_1.animate.shift(r*LEFT), run_time=2)

		for i in [circle_gamma, label_gamma, dots_FDEG]:
			self.play(GrowFromCenter(i))
		self.play(*[GrowFromCenter(i) for i in labels_FDEG])
		self.add_foreground_mobjects(*dots_FDEG, *labels_FDEG)

		self.play(
			VGroup(
				change_1, circle_gamma, *dots_FDEG, label_gamma, *labels_FDEG
			).animate.shift(l*LEFT)
		)
		self.play(*COL(dots_FDEG, c=ORANGE))

		for idx, mobj in enumerate([label_D, label_E, label_F, label_G]):
			j = 3*idx
			self.play(
				Write(t5[j]),
				*[TransformFromCopy(obj, t5[j+i]) for i, obj in [(1, label_A), (2, mobj)]],
				run_time=2
			)
		self.play(FadeOut(circle_gamma, label_gamma), *COL(t5[:12], dots_FDEG))
		for i in [circle_BDF, dot_K, label_K]:
			self.play(GrowFromCenter(i))
		self.add_foreground_mobjects(dot_K, label_K)

		self.play(*COL(dots_KBDF, c=ORANGE))
		self.play(
			Write(t5[12]),
			*[TransformFromCopy(obj, t5[i+13]) for i, obj in enumerate(
				[label_B, label_D, label_K, label_F]
			)], run_time=2
		)
		self.play(Write(t5[17]))
		self.play(FadeOut(circle_BDF))
		self.play(*COL(t5[12:18], dots_KBDF))

		for i in [circle_CGE, dot_L, label_L]:
			self.play(GrowFromCenter(i))
		self.add_foreground_mobjects(dot_L, label_L)

		self.play(*COL(dots_LCGE, c=ORANGE))
		self.play(
			Write(t5[18]),
			*[TransformFromCopy(obj, t5[i+19]) for i, obj in enumerate(
				[label_C, label_G, label_L, label_E]
			)], run_time=2
		)
		self.play(Write(t5[23]))
		self.play(FadeOut(circle_CGE))
		self.play(*COL(t5[18:24], dots_LCGE))

		self.play(Create(lines_FX_GX), run_time=2)
		for i in [dot_X, label_X]:
			self.play(GrowFromCenter(i))
		self.add_foreground_mobjects(dot_X, label_X)
		self.play(ReplacementTransform(lines_FX_GX, dashed_FX_GX))
	
		self.play(*COL(dots_AXO, c=ORANGE))
		self.play(
			Write(t5[24]),
			*[anim for i, obj in enumerate([label_A, label_X, label_O]) for anim in [
				TransformFromCopy(obj, t5[2*i+25]), Write(t5[2*i+26])
			]], run_time=2
		)
		self.play(*COL(t5[24:], dots_AXO))
		self.wait()
		self.play(Create(lines_AF_AG))

		change_2 = [
			lines_ABC,
			dot_B, dot_C, dot_D, dot_E,
			label_B, label_C, label_D, label_E
		]
		self.play(*[FadeOut(i) for i in [*change_2, label_omega]])

		t = arg(G-F)
		buff = .25
		self.play(
			Rotate(
				VGroup(
					*dashed_FX_GX, *lines_AF_AG,
					dot_A, dot_F, dot_G, dot_X, dot_K, dot_L
				), t, IN, nparray(dot_O)
			),
			UpdateFromFunc(label_A, lambda m: m.next_to(dot_A, UP, buff*f)),
			UpdateFromFunc(label_F, lambda m: m.next_to(dot_F, LEFT, buff*f)),
			UpdateFromFunc(label_G, lambda m: m.next_to(dot_G, RIGHT, buff*f)),
			UpdateFromFunc(label_K, lambda m: m.next_to(dot_K, dir(comp(dot_K) - comp(dot_O)), buff*f)),
			UpdateFromFunc(label_L, lambda m: m.next_to(dot_L, dir(comp(dot_L) - comp(dot_O)), buff*f)),
			UpdateFromFunc(label_X, lambda m: m.next_to(dot_X, DOWN, buff*f)),
			run_time=2
		)
		line_OF = LINE(dot_O, dot_F, RED)
		line_OG = LINE(dot_O, dot_G, RED)
		lines_OF_OG = VGroup(line_OF, line_OG)
		self.play(Create(lines_OF_OG))

		self.play(FadeOut(circle_omega))

		arrow_OA = DA(dot_O, dot_A, .26, BLUE, stroke_width=4, tip_length=.2)
		new_label_A = MP('$A$', dot_A, dir(135), f)
		new_label_O = MP('$O$', dot_O, dir(225), f)
		new_label_X = MP('$X$', dot_X, dir(267), f)

		repl_rad = .01
		self.play(
			CounterclockwiseTransform(label_A, new_label_A, float=repl_rad),
			*[ClockwiseTransform(*args, float=repl_rad) for args in [
				(label_O, new_label_O), (label_X, new_label_X)
			]]
		)
		self.play(Create(arrow_OA), run_time=2)

		text_FG = Tex('Mediatriz de $FG$').scale(.5).next_to(nparray(dot_O) + .1*RIGHT + .3*DOWN)
		self.play(Write(text_FG))
		self.wait()

		self.play(FadeOut(t5), *[TransformFromCopy(t5[i+25], t6[i]) for i in range(6)])
		self.play(Write(t6[6]))
		self.play(
			*[TransformFromCopy(obj, t6[i]) for obj, i in [
				(label_X, 7), (label_F, 9), (label_G, 10)
			]], Write(t6[8]), run_time=2
		)
		new_label_A = MP('$A$', dot_A, UP, f)
		new_label_O = MP('$O$', dot_O, DOWN, f)
		new_label_X = MP('$X$', dot_X, DOWN, f)

		self.play(FadeOut(arrow_OA, text_FG))
		self.play(
			ClockwiseTransform(label_A, new_label_A, float=repl_rad),
			*[CounterclockwiseTransform(*args, float=repl_rad) for args in [
				(label_O, new_label_O), (label_X, new_label_X)
			]]
		)
		self.play(*[FadeOut(i) for i in [
			label_A, label_O, dot_A, dot_O, lines_AF_AG, lines_OF_OG
		]])
		line_FG = LINE(dot_F, dot_G, GREEN)
		self.play(Create(line_FG))

		arc_GFK = MA(dot_G, dot_F, dot_K, .5, 2, color=PURPLE)
		arc_LGF = MA(dot_L, dot_G, dot_F, .5, 2, color=PURPLE)
		self.bring_to_back(arc_GFK, arc_LGF)
		self.play(Create(arc_GFK), Create(arc_LGF))

		line_FK = LINE(dot_F, dot_K, GREEN)
		line_GL = LINE(dot_G, dot_L, GREEN)
		lines_FK_GL = VGroup(line_FK, line_GL)

		self.play(Write(t6[11]))
		self.play(
			Write(t6[12]),
			*[TransformFromCopy(obj, t6[i+13]) for i, obj in enumerate(
				[label_K, label_F, label_G]
			)], run_time=2
		)
		self.play(
			Write(t6[16:18]),
			*[TransformFromCopy(obj, t6[i+18]) for i, obj in enumerate(
				[label_L, label_G, label_F]
			)], run_time=2
		)
		self.play(
			*[ReplacementTransform(*args) for args in [
				(dashed_FX, line_FK), (dashed_GX, line_GL)
			]], FadeOut(dot_X), FadeOut(label_X), run_time=2
		)
		self.play(FadeOut(t6[:12]))
		self.play(
			Write(t7[0]), *[ReplacementTransform(t6[i+12], t7[i+1]) for i in range(9)],
			run_time=2
		)
		self.play(
			Rotate(
				VGroup(
					arc_GFK, arc_LGF,
					line_FG, lines_FK_GL,
					dot_K, dot_L, dot_F, dot_G
				), t, OUT, nparray(dot_O)
			),
			UpdateFromFunc(label_F, lambda m: m.next_to(dot_F, LEFT, buff*f)),
			UpdateFromFunc(label_G, lambda m: m.next_to(dot_G, RIGHT, buff*f)),
			UpdateFromFunc(label_K, lambda m: m.next_to(dot_K, dir(comp(dot_K) - comp(dot_O)), buff*f)),
			UpdateFromFunc(label_L, lambda m: m.next_to(dot_L, dir(comp(dot_L) - comp(dot_O)), buff*f))
		)
		VGroup(dot_A, arrow_OA).rotate(t, about_point=nparray(dot_O))
		label_A.next_to(dot_A, UP, buff*f)

		self.add_foreground_mobjects(
			arc_GFK, arc_LGF,
			line_FG, lines_FK_GL,
			dot_K, dot_L, dot_F, dot_G, dot_A, dot_B, dot_O,
			*change_2[3:]
		)
		self.play(*[FadeIn(i) for i in [
			dot_O, label_O, dot_A, label_A,
			circle_omega, label_omega,
			*change_2
		]])
		self.wait()
		self.play(*[ReplacementTransform(obj, t8[i+1]) for i, obj in enumerate(
			[t7[1:5], t7[5], t7[6:]]
		)])
		line_GF = LINE(dot_G, dot_F)
		text_x = Tex('$x$').scale(f).move_to(Angle(line_FG, line_FK, .7))
		text_y = Tex('$y$').scale(f).move_to(Angle(line_GL, line_GF, .7))

		self.play(
			*[Transform(i, MA(*args, .5)) for i, args in [
				(arc_GFK, [dot_G, dot_F, dot_K]), (arc_LGF, [dot_L, dot_G, dot_F])
			]],
			*[TransformFromCopy(t8[i], obj) for i, obj in [(1, text_x), (3, text_y)]],
			run_time=2
		)
		text_FG.shift(.42*DOWN + .05*RIGHT)

		new_label_A = MP('$A$', dot_A, dir(159 + degrees(t)), f)
		new_label_O = MP('$O$', dot_O, dir(225 + degrees(t)), f)
		self.play(
			CounterclockwiseTransform(label_A, new_label_A, float=repl_rad),
			ClockwiseTransform(label_O, new_label_O, float=repl_rad)
		)
		self.play(Create(arrow_OA), run_time=2)
		self.play(Write(text_FG))

		new_label_A = MP('$A$', dot_A, UP, f)
		new_label_O = MP('$O$', dot_O, DOWN, f)
		line_OA = LINE(dot_O, dot_A, PURPLE)

		arc_OA_GF = RightAngle(line_OA, line_GF, .2)
		self.bring_to_back(arc_OA_GF)
		self.play(Create(arc_OA_GF))
		self.wait()

		self.play(FadeOut(text_FG), ReplacementTransform(arrow_OA, line_OA))
		self.play(
			ClockwiseTransform(label_A, new_label_A, float=repl_rad),
			CounterclockwiseTransform(label_O, new_label_O, float=repl_rad)
		)
		text_C = Tex('$C$').scale(f).move_to(Angle(line_CA, line_BC, .8, (1, -1)))

		arc_ACB = MA(dot_A, dot_C, dot_B, .5)
		self.bring_to_back(arc_ACB)
		self.play(Create(arc_ACB), TransformFromCopy(label_C, text_C), run_time=2)
		change_3 = [
			arc_GFK, arc_LGF, arc_OA_GF,
			lines_FK_GL, line_FG,
			text_x, text_y,
			dot_D, dot_E, dot_F, dot_K, dot_G, dot_L,
			label_D, label_E, label_F, label_K, label_G, label_L
		]
		line_OB = LINE(dot_O, dot_B, PURPLE)
		self.play(*[FadeOut(i) for i in change_3], Create(line_OB))
		arc_AOB = Angle(line_OA, line_OB, .35)
		self.bring_to_back(arc_AOB)

		text_2C = Tex('$2C$').scale(f).move_to(Angle(line_OA, line_OB, .9))
		self.play(Create(arc_AOB), TransformFromCopy(text_C, text_2C), run_time=2)

		arc_BAO = MA(dot_B, dot_A, dot_O, .5)
		arc_OBA = MA(dot_O, dot_B, dot_A, .5)
		self.bring_to_back(arc_BAO, arc_OBA)

		text_C_1 = Tex('$90-C$').scale(f).move_to(Angle(line_AB, line_OA, 1.4, (1, -1)))
		text_C_2 = Tex('$90-C$').scale(f).move_to(Angle(line_OB, line_AB, 1.4, (-1, -1)))
		self.play(
			Create(arc_BAO), Create(arc_OBA),
			*[TransformFromCopy(text_2C, i) for i in [text_C_1, text_C_2]],
			run_time=2
		)
		self.play(FadeOut(arc_AOB, arc_OBA, line_OB, text_2C, text_C_2))
		self.wait()

		self.bring_to_back(arc_OA_GF)
		self.play(*[FadeIn(i) for i in change_3])

		arc_FG_AB = Angle(line_FG, line_AB, .85, (1, -1))
		text_C_3 = Tex('$C$').scale(f).move_to(Angle(line_FG, line_AB, 1.2, (1, -1)))
		self.bring_to_back(arc_FG_AB)
		self.play(TransformFromCopy(text_C_1, text_C_3), Create(arc_FG_AB), run_time=2)
		self.wait()

		circle_BDF.set_color(ORANGE)
		self.bring_to_back(circle_BDF)
		self.play(GrowFromCenter(circle_BDF))

		F1 = k*dir(degrees(arg(F-O1))) + comp((-l, 0))
		K1 = k*dir(degrees(arg(K-O1))) + comp((-l, 0))
		D1 = k*dir(degrees(arg(D-O1))) + comp((-l, 0))
		B1 = k*dir(degrees(arg(B-O1))) + comp((-l, 0))
		ref1 = k*dir(degrees(arg(2*foot(O1, F, G)-F-O1))) + comp((-l, 0))

		circle_BDF1 = circle_omega.copy().set_color(ORANGE)

		dot_F1 = DOT(F1)
		dot_K1 = DOT(K1)
		dot_D1 = DOT(D1)
		dot_B1 = DOT(B1)
		ref_dot1 = DOT(ref1)

		label_F1 = MP('$F$', dot_F1, LEFT, f)
		label_K1 = MP('$K$', dot_K1, UP, f)
		label_D1 = MP('$D$', dot_D1, D-O1, f)
		label_B1 = MP('$B$', dot_B1, B-O1, f)

		line_KB1 = LINE(K1, B1, RED)
		line_BD1 = LINE(B1, D1, RED)
		line_FK1 = LINE(F1, K1, GREEN)
		line_FG1 = LINE(F1, ref1, GREEN)

		arc_FG_AB1 = Angle(line_FG1, line_KB1, .5, (1, -1))
		arc_GFK1 = Angle(line_FG1, line_FK1, .5)

		text_C1 = Tex('$C$').scale(f).move_to(Angle(line_FG1, line_KB1, .9, (1, -1)))
		text_x1 = Tex('$x$').scale(f).move_to(Angle(line_FG1, line_FK1, .9))

		self.add_foreground_mobjects(dot_F1, dot_K1, dot_D1, dot_B1, ref_dot1)
		self.play(
			*[FadeOut(i) for i in [
				arc_LGF, arc_ACB, arc_BAO, arc_OA_GF, arc_FG_AB, arc_GFK,
				circle_omega,
				line_AB, line_BC, line_CA, line_OA, line_FK, line_GL, line_FG,
				dot_O, dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G, dot_K, dot_L,
				label_O, label_omega, label_A, label_B, label_C, label_D, label_E, label_F, label_G, label_K, label_L,
				text_y, text_C, text_C_1, text_C_3, text_x
			]],
			ReplacementTransform(circle_BDF, circle_BDF1),
			*[TransformFromCopy(*args) for args in [
				(arc_FG_AB, arc_FG_AB1), (arc_GFK, arc_GFK1),
				(line_AB, line_KB1), (line_BC, line_BD1), (line_FK, line_FK1), (line_FG, line_FG1),
				(dot_F, dot_F1), (dot_K, dot_K1), (dot_D, dot_D1), (dot_B, dot_B1),
				(label_F, label_F1), (label_K, label_K1), (label_D, label_D1), (label_B, label_B1),
				(text_C_3, text_C1), (text_x, text_x1)
			]],
			GrowFromCenter(ref_dot1)
		)
		arc_FKB1 = MA(dot_F1, dot_K1, dot_B1, .5)
		text_Cx = MathTex('C', '-', 'x').scale(f).move_to(Angle(line_FK1, line_KB1, .9, (-1, 1)))
		self.bring_to_back(arc_FKB1)
		self.play(
			*[TransformFromCopy(i, text_Cx[2*idx]) for idx, i in enumerate(
				[text_C1, text_x1]
			)], Write(text_Cx[1]), Create(arc_FKB1), run_time=2
		)
		self.play(FadeOut(arc_FG_AB1, arc_GFK1, text_C1, text_x1, label_K1, line_FG1), FadeOut(ref_dot1))

		alpha = degrees(arg((K-O1)/(D-O1)))
		new_text_Cx = text_Cx.copy().move_to(Angle(LINE(D1, F1), LINE(D1, B1), 1.2))
		self.add_foreground_mobjects(dot_F1, dot_B1, dot_D1, dot_K1)
		self.bring_to_back(arc_FKB1)

		alpha_tracker = ValueTracker(alpha)
		dot_K1.add_updater(lambda m: m.become(
			dot_D1.copy().rotate(radians(alpha_tracker.get_value()), about_point=nparray(dot_O))
		))
		arc_FKB1.add_updater(lambda m: m.become(
			MA(dot_F1, dot_D1.copy().rotate(radians(alpha_tracker.get_value()), about_point=nparray(dot_O)), dot_B1, .5)
		))
		line_FK1.add_updater(lambda m: m.become(
			LINE(dot_F1, dot_D1.copy().rotate(radians(alpha_tracker.get_value()), about_point=nparray(dot_O)), GREEN)
		))
		line_KB1.add_updater(lambda m: m.become(
			LINE(dot_D1.copy().rotate(radians(alpha_tracker.get_value()), about_point=nparray(dot_O)), dot_B1, RED)
		))

		self.play(
			alpha_tracker.animate.set_value(0),
			ClockwiseTransform(text_Cx, new_text_Cx, path_arc=-radians(alpha)),
			run_time=2
		)
		for i in [dot_K1, arc_FKB1, line_FK1, line_KB1]:
			i.clear_updaters()
		self.remove(line_KB1, dot_K1)
		self.add_foreground_mobjects(dot_C, dot_E)

		beta = 120
		beta_tracker = ValueTracker(0)
		arc_FKB1.add_updater(lambda m: m.become(MA(dot_F1, dot_D1, dot_B1, .5)))
		line_FK1.add_updater(lambda m: m.become(LINE(dot_F1, dot_D1, GREEN)))
		text_Cx.add_updater(lambda m: m.move_to(MA(dot_F1, dot_D1, dot_B1, 1.2 - beta_tracker.get_value()*(.15)/beta)))

		self.play(
			*[ReplacementTransform(*args) for args in [
				(line_BD1, line_BC),
				(dot_F1, dot_F), (dot_D1, dot_D), (dot_B1, dot_B),
				(label_F1, label_F), (label_D1, label_D), (label_B1, label_B)
			]],
			FadeOut(circle_BDF1),
			FadeIn(
				arc_LGF, arc_ACB,
				circle_omega,
				line_CA, line_GL, line_FG,
				dot_A, dot_C, dot_E, dot_G, dot_L,
				label_omega, label_A, label_C, label_E, label_G, label_L,
				text_y, text_C
			),
			beta_tracker.animate.set_value(beta)
		)
		self.wait()

		for i in [arc_FKB1, line_FK1, text_Cx]:
			i.clear_updaters()

		circle_CGE.set_color(ORANGE)
		self.bring_to_back(circle_CGE)
		self.play(GrowFromCenter(circle_CGE))

		E2 = k*dir(degrees(arg(E-O2))) + comp((-l, 0))
		L2 = k*dir(degrees(arg(L-O2))) + comp((-l, 0))
		G2 = k*dir(degrees(arg(G-O2))) + comp((-l, 0))
		C2 = k*dir(degrees(arg(C-O2))) + comp((-l, 0))
		ref2 = k*dir(degrees(arg(2*foot(O2, G, F)-G-O2))) + comp((-l, 0))

		circle_CGE2 = circle_omega.copy().set_color(ORANGE)

		dot_G2 = DOT(G2)
		dot_L2 = DOT(L2)
		dot_E2 = DOT(E2)
		dot_C2 = DOT(C2)
		ref_dot2 = DOT(ref2)

		label_G2 = MP('$G$', dot_G2, G-O2, f)
		label_L2 = MP('$L$', dot_L2, L-O2, f)
		label_E2 = MP('$E$', dot_E2, E-O2, f)
		label_C2 = MP('$C$', dot_C2, C-O2, f)

		line_CL2 = LINE(C2, L2, RED)
		line_EC2 = LINE(E2, C2, RED)
		line_GL2 = LINE(G2, L2, GREEN)
		line_FG2 = LINE(ref2, G2, GREEN)

		arc_ACB2 = Angle(line_CL2, line_EC2, .5, (1, -1))
		arc_LGF2 = Angle(line_GL2, line_FG2, .5, (1, -1))

		text_C2 = Tex('$C$').scale(f).move_to(Angle(line_CL2, line_EC2, .9, (1, -1)))
		text_y2 = Tex('$y$').scale(f).move_to(Angle(line_GL2, line_FG2, .8, (1, -1)))

		self.add_foreground_mobjects(ref_dot2, dot_A, dot_B, dot_F, dot_D)
		self.play(
			*[FadeOut(i) for i in [
				arc_FKB1, arc_ACB, arc_LGF,
				circle_omega,
				line_BC, line_CA, line_GL, line_FG, line_FK1,
				dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G, dot_L,
				label_omega, label_A, label_B, label_C, label_D, label_E, label_F, label_G, label_L,
				text_y, text_C, text_Cx
			]],
			ReplacementTransform(circle_CGE, circle_CGE2),
			*[TransformFromCopy(*args) for args in [
				(arc_ACB, arc_ACB2), (arc_LGF, arc_LGF2),
				(line_CA, line_CL2), (line_BC, line_EC2), (line_GL, line_GL2), (line_FG, line_FG2),
				(dot_G, dot_G2), (dot_L, dot_L2), (dot_E, dot_E2), (dot_C, dot_C2),
				(label_G, label_G2), (label_L, label_L2), (label_E, label_E2), (label_C, label_C2),
				(text_C, text_C2), (text_y, text_y2)
			]],
			GrowFromCenter(ref_dot2)
		)
		theta = degrees(arg((G-O2)/(C-O2)))
		new_text_C2 = text_C2.copy().move_to(Angle(line_GL2, line_FG2, 1.5, (1, -1)))
		self.add_foreground_mobjects(dot_G2, dot_C2, dot_E2, dot_L2)
		self.bring_to_back(arc_ACB2)

		theta_tracker = ValueTracker(theta)
		dot_C2.add_updater(lambda m: m.become(
			dot_G2.copy().rotate(radians(theta_tracker.get_value()), IN, about_point=nparray(dot_O))
		))
		arc_ACB2.add_updater(lambda m: m.become(
			MA(dot_L2, dot_G2.copy().rotate(
				radians(theta_tracker.get_value()), IN, about_point=nparray(dot_O)
			), dot_E2, .5+.7*(1-theta_tracker.get_value()/theta))
		))
		line_CL2.add_updater(lambda m: m.become(
			LINE(dot_G2.copy().rotate(radians(theta_tracker.get_value()), IN, about_point=nparray(dot_O)), L2, RED)
		))
		line_EC2.add_updater(lambda m: m.become(
			LINE(dot_E2, dot_G2.copy().rotate(radians(theta_tracker.get_value()), IN, about_point=nparray(dot_O)), RED)
		))

		self.play(FadeOut(label_C2))
		self.play(
			theta_tracker.animate.set_value(0),
			CounterclockwiseTransform(text_C2, new_text_C2, path_arc=radians(theta)),
			run_time=2
		)
		for i in [dot_C2, arc_ACB2, line_CL2, line_EC2]:
			i.clear_updaters()
		self.remove(line_CL2, dot_C2)

		arc_FGE2 = MA(ref_dot2, dot_G2, dot_E2, 1.9)
		text_Cy = MathTex('C', '-', 'y').scale(f).move_to(Angle(line_FG2, line_EC2, 2.4, (-1, -1)))
		self.bring_to_back(arc_FGE2)

		self.play(
			*[TransformFromCopy(i, text_Cy[2*idx]) for idx, i in enumerate([text_C2, text_y2])],
			Write(text_Cy[1]), Create(arc_FGE2),
			run_time=2
		)
		self.play(FadeOut(arc_ACB2, arc_LGF2, text_C2, text_y2, label_L2, line_GL2), FadeOut(dot_L2))

		arc_FGE = MA(dot_F, dot_G, dot_E, .7)
		line_EG = LINE(dot_E, dot_G, GREEN)
		self.add_foreground_mobjects(text_Cy, dot_F)

		self.play(
			*[ReplacementTransform(*args) for args in [
				(arc_FGE2, arc_FGE),
				(line_FG2, line_FG), (line_EC2, line_EG),
				(dot_G2, dot_G), (dot_E2, dot_E),
				(label_G2, label_G), (label_E2, label_E)
			]],
			text_Cy.animate.move_to(Angle(line_FG, line_EG, 1.8, (-1, -1))),
			FadeOut(circle_CGE2), FadeOut(ref_dot2),
			FadeIn(
				arc_FKB1,
				line_BC, line_FK1,
				dot_A, dot_B, dot_C, dot_D, dot_F,
				label_A, label_B, label_C, label_D, label_F,
				text_Cx
			)
		)
		self.wait()

		circle_gamma.set_color(BLUE)
		self.add_foreground_mobjects(dot_D, dot_E, dot_G, text_Cx)
		for i, j in [(circle_gamma, 2), (label_gamma, 1)]:
			self.play(GrowFromCenter(i), run_time=j)

		self.play(FadeOut(t7, t8))
		self.play(
			*[TransformFromCopy(txt[i], t9[4*idx+i]) for idx, txt in enumerate([
				text_Cx, text_Cy
			]) for i in range(3)], Write(t9[3]), run_time=2
		)
		self.wait()

		self.play(*[i.animate.set_color(DARK_GRAY) for i in [t9[:2], t9[4:6]]])
		self.play(
			*[TransformFromCopy(t9[i], t9[j]) for i, j in [(2, 7), (6, 9)]], Write(t9[8]),
			run_time=2
		)
		for color in [YELLOW, WHITE]:
			self.play(Circumscribe(t9[7:10]), t9[7:10].animate.set_color(color))
		self.wait()

		self.play(*[FadeOut(i, shift=DOWN) for i in self.mobjects])

		ending_credit = Tex('Video hecho con ', r'\textsc{Manim}')
		ending_credit.scale(1.5)
		ending_credit[1].set_color_by_gradient(BLUE_B, BLUE_E)
		for i in range(2):
			self.play(Write(ending_credit[i]))
		self.wait()
		self.play(FadeOut(ending_credit, shift=DOWN))
		self.wait()
