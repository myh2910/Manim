from render.macros.extras import *
from render.macros.asymptote import *

class Video(Scene):
	def construct(self):
		self.add_sound('assets/2018_1.mp3')

		logo = ImageMobject('assets/2018.png')
		self.play(FadeIn(logo, shift=UP))

		t1 = Tex(r'\textsf{Problema 1}').set_color_by_gradient(TEAL_E, TEAL_A)
		t1.scale(2.6).shift(2.7*RIGHT + .2*DOWN)

		t2 = Tex(r"\emph{Solución}").set_color(YELLOW_B)
		t2.scale(2).shift(2.7*RIGHT + .9*DOWN)

		self.play(AnimationGroup(logo.animate.shift(3.7*LEFT), Write(t1), lag_ratio=MED_LAG_RATIO))
		self.play(t1.animate.shift(.6*UP), FadeIn(t2, shift=UP), lag_ratio=.1, float=linear)
		self.wait(1.5)

		t3 = Tex(
			r'\textbf{Problema 1.}\ \ ',
			r"Sea $\Gamma$ la circunferencia circunscrita al triángulo acutángulo $ABC$. Los puntos $D$ y $E$ están en los segmentos $AB$ y $AC$, respectivamente, y son tales que $AD=AE$. Las mediatrices de $BD$ y $CE$ cortan a los arcos menores $AB$ y $AC$ de $\Gamma$ en los puntos $F$ y $G$, respectivamente. Demostrar que las rectas $DE$ y $FG$ son paralelas (o son la misma recta).",
			tex_environment=None,
			tex_template=tex_template('512.34pt')
		)
		t3[0].set_color_by_gradient(TEAL_E, TEAL_A)
		t3.scale(.5).to_corner(UP)

		shifting_factor = 12
		self.play(
			*[FadeOut(item, shift=shifting_factor*LEFT) for item in [logo, t2]],
			ReplacementTransform(t1[0], t3[0]),
			FadeIn(t3[1], shift=shifting_factor*LEFT)
		)
		self.wait()

		A, B, C = dir(120), dir(210), dir(330)
		r = .5
		D, E = A + r*(B-A)/distance(A, B), A + r*(C-A)/distance(C, A)
		l = dir(2*np.arcsin(r/2)/DEGREES)
		X, Y = A/l, A*l
		F, G = 2*foot(origin, D, X) - X, 2*foot(origin, E, Y) - Y

		scale_factor = 2.7
		A *= scale_factor
		B *= scale_factor
		C *= scale_factor
		D *= scale_factor
		E *= scale_factor
		X *= scale_factor
		Y *= scale_factor
		F *= scale_factor
		G *= scale_factor

		dot_A = DOT(A)
		dot_B = DOT(B)
		dot_C = DOT(C)
		dot_D = DOT(D)
		dot_E = DOT(E)
		dot_F = DOT(F)
		dot_G = DOT(G)
		dot_X = DOT(X)
		dot_Y = DOT(Y)

		label_scale_factor = .5
		label_A = MP('$A$', dot_A, A, label_scale_factor)
		label_B = MP('$B$', dot_B, B, label_scale_factor)
		label_C = MP('$C$', dot_C, C, label_scale_factor)
		label_D = MP('$D$', dot_D, dir(179), label_scale_factor)
		label_E = MP('$E$', dot_E, dir(82), label_scale_factor)
		label_F = MP('$F$', dot_F, F, label_scale_factor)
		label_G = MP('$G$', dot_G, G, label_scale_factor)
		label_X = MP('$X$', dot_X, UP, label_scale_factor)
		label_Y = MP('$Y$', dot_Y, Y, label_scale_factor)

		c1, c2, c3, c4, c5, c6 = GREEN_A, YELLOW_A, TEAL_A, PURPLE_A, RED_A, BLUE_A
		line_FX = LINE(F, X, c1)
		line_GY = LINE(G, Y, c1)
		line_AD = LINE(A, D, c2)
		line_AE = LINE(A, E, c2)
		line_AX = LINE(A, X, c2)
		line_AY = LINE(A, Y, c2)
		line_FB = LINE(F, B, c3)
		line_FD = LINE(F, D, c3)
		line_GC = LINE(G, C, c4)
		line_GE = LINE(G, E, c4)
		line_XY = LINE(X, Y, c5)
		line_DE = LINE(D, E, c5)
		line_FG = LINE(F, G, c5)

		angle_radius, stroke_width, dot_radius = .29, 8, 0.03
		angle_DBF = MA(D, B, F, angle_radius, color=c3, stroke_width=stroke_width)
		angle_FDB = MA(F, D, B, angle_radius, color=c3, stroke_width=stroke_width)
		angle_XDA = MA(X, D, A, angle_radius, color=c3, stroke_width=stroke_width)
		angle_AXD = MA(A, X, D, angle_radius, color=c3, stroke_width=stroke_width)
		angle_GCE = MA(G, C, E, angle_radius, color=c4, dot=True, dot_color=c4, dot_radius=dot_radius)
		angle_CEG = MA(C, E, G, angle_radius, color=c4, dot=True, dot_color=c4, dot_radius=dot_radius)
		angle_AEY = MA(A, E, Y, angle_radius, color=c4, dot=True, dot_color=c4, dot_radius=dot_radius)
		angle_EYA = MA(E, Y, A, angle_radius, color=c4, dot=True, dot_color=c4, dot_radius=dot_radius)
		angle_EYX = MA(E, Y, X, angle_radius, color=c5)
		angle_EDX = MA(E, D, X, angle_radius, color=c5)
		angle_GFX = MA(G, F, X, angle_radius, color=c5)

		triangle_ABC = POLY(A, B, C, color=RED_A).set_fill(color=RED_A, opacity=.1)
		circle_ABC = CR(scale_factor, c=c6).set_fill(color=c6, opacity=.07)
		label_gamma = MP(r'$\Gamma$', DOT(scale_factor*dir(60)), dir(60), label_scale_factor)
		circle_Ar = CR(r*scale_factor, A, c2).set_fill(color=c2, opacity=.07)

		shifting_left_factor = 2.8
		for item in [
			circle_ABC,
			angle_DBF, angle_FDB, angle_XDA, angle_AXD, angle_GCE, angle_CEG, angle_AEY, angle_EYA, angle_EYX, angle_EDX, angle_GFX,
			triangle_ABC,
			line_FX, line_GY,
			circle_Ar,
			line_AD, line_AE, line_AX, line_AY, line_FB, line_FD, line_GC, line_GE, line_XY, line_DE, line_FG,
			dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
			label_gamma, label_A, label_B, label_C, label_D, label_E, label_F, label_G, label_X, label_Y
		]: item.shift(shifting_left_factor*LEFT + .9*DOWN)

		self.add_foreground_mobjects(dot_A, dot_B, dot_C, label_A, label_B, label_C)
		self.play(
			t3.animate.scale(.88).to_corner(UP).shift(.2*UP),
			*[FadeIn(item, shift=shifting_left_factor*LEFT) for item in [
				circle_ABC, triangle_ABC,
				dot_A, dot_B, dot_C,
				label_gamma, label_A, label_B, label_C
			]]
		)
		self.wait(.5)

		t4 = MathTex(
			#0    1    2    3    4
			'A', 'D', '=', 'A', 'E'
		)
		t4.scale(label_scale_factor).shift(3.5*RIGHT+1.2*UP)
		for i in [0, 1, 3, 4]:
			t4[i].set_color(c2)
		ref_line = t4.copy()

		self.add_foreground_mobjects(dot_D, dot_E, label_D, label_E)
		self.play(AnimationGroup(
			AnimationGroup(Create(line_AD), Write(t4[0])), GrowFromCenter(dot_D),
			AnimationGroup(GrowFromCenter(label_D), Write(t4[1])), Write(t4[2]),
			AnimationGroup(Create(line_AE), Write(t4[3])), GrowFromCenter(dot_E),
			AnimationGroup(GrowFromCenter(label_E),  Write(t4[4])),
			lag_ratio=.4
		))
		t5 = MathTex(
			#0    1                              2    3
			'F', BELONGS_TO('la mediatriz de'), 'B', 'D'
		)
		t6 = MathTex(
			#0    1                              2    3
			'G', BELONGS_TO('la mediatriz de'), 'C', 'E'
		)
		t7 =  MathTex(
			#0    1    2    3    4
			'F', 'B', '=', 'F', 'D'
		)
		t8 = MathTex(
			#0    1    2    3    4
			'G', 'C', '=', 'G', 'E'
		)
		t9 = MathTex(
			#  0    1    2    3    4      5    6    7    8
			ANGLE, 'D', 'B', 'F', '=', ANGLE, 'F', 'D', 'B'
		)
		t10 = MathTex(
			#  0    1    2    3    4      5    6    7    8
			ANGLE, 'G', 'C', 'E', '=', ANGLE, 'C', 'E', 'G'
		)
		for i in [0, 2, 3]:
			t5[i].set_color(c3)
			t6[i].set_color(c4)
		for i in [0, 1, 3, 4]:
			t7[i].set_color(c3)
			t8[i].set_color(c4)
		for i in [*range(4), *range(5, 9)]:
			t9[i].set_color(c3)
			t10[i].set_color(c4)

		y_buff = .3
		for i in [t5, t7, t9]:
			i.scale(label_scale_factor).next_to(ref_line, DOWN, y_buff)
		for i in [t6, t8, t10]:
			i.scale(label_scale_factor).next_to(t5, DOWN, y_buff)

		for args, txt in [([dot_F, label_F], t5), ([dot_G, label_G], t6)]:
			self.add_foreground_mobjects(*args)
			self.play(AnimationGroup(
				GrowFromCenter(args[0]),
				AnimationGroup(GrowFromCenter(args[1]), Write(txt[0])),
				Write(txt[1:]),
				lag_ratio=SMALL_LAG_RATIO
			))
		self.wait(2)

		for args, txt1, txt2 in [([line_FB, line_FD], t5, t7), ([line_GC, line_GE], t6, t8)]:
			self.play(
				*[Create(i) for i in args],
				FadeOut(txt1[:2]),
				*[TransformFromCopy(txt1[0], txt2[i]) for i in [0, 3]],
				*[ReplacementTransform(txt1[i], txt2[j]) for i, j in [(2, 1), (3, 4)]],
				Write(txt2[2])
			)
		self.wait(2)

		self.add_foreground_mobjects(
			circle_ABC,
			angle_DBF, angle_FDB,
			triangle_ABC,
			line_AD, line_AE, line_FB, line_FD, line_GC, line_GE,
			dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G,
			label_gamma, label_A, label_B, label_C, label_D, label_E, label_F, label_G
		)
		self.play(
			*[Create(i) for i in [angle_DBF, angle_FDB]],
			FadeOut(t7[1], t7[4]),
			*[Write(t9[i]) for i in [0, 5]],
			*[TransformFromCopy(t7[i], t9[j]) for i, j in [(4, 1), (1, 2), (4, 7), (1, 8)]],
			*[ReplacementTransform(t7[i], t9[j]) for i, j in [(0, 3), (2, 4), (3, 6)]]
		)
		self.add_foreground_mobjects(
			circle_ABC,
			angle_DBF, angle_FDB, angle_GCE, angle_CEG,
			triangle_ABC,
			line_AD, line_AE, line_FB, line_FD, line_GC, line_GE,
			dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G,
			label_gamma, label_A, label_B, label_C, label_D, label_E, label_F, label_G
		)
		self.play(
			*[Create(i) for i in [angle_GCE, angle_CEG]],
			FadeOut(t8[1], t8[4]),
			*[Write(t10[i]) for i in [0, 5]],
			*[TransformFromCopy(t8[i], t10[j]) for i, j in [(1, 2), (4, 3), (1, 6), (4, 7)]],
			*[ReplacementTransform(t8[i], t10[j]) for i, j in [(0, 1), (2, 4), (3, 8)]]
		)
		self.wait(2)

		t11 = MathTex(
			#  0    1    2    3    4      5    6    7    8              9   10   11   12   13     14   15   16   17
			ANGLE, 'D', 'B', 'F', '=', ANGLE, 'F', 'D', 'B' + QQUAD, ANGLE, 'G', 'C', 'E', '=', ANGLE, 'C', 'E', 'G'
		)
		t11.scale(label_scale_factor).next_to(ref_line, DOWN, y_buff)
		for i in [*range(4), *range(5, 9)]:
			t11[i].set_color(c3)
			t11[i+9].set_color(c4)
		self.play(*[ReplacementTransform(*args) for args in [(t9, t11[:9]), (t10, t11[9:])]])

		self.add_foreground_mobjects(
			circle_ABC,
			angle_DBF, angle_FDB, angle_GCE, angle_CEG,
			triangle_ABC,
			line_GY, line_FX, line_AD, line_AE, line_FB, line_FD, line_GC, line_GE,
			dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
			label_gamma, label_A, label_B, label_C, label_D, label_E, label_F, label_G, label_X, label_Y
		)
		self.play(AnimationGroup(
			*[AnimationGroup(
				Create(i), *[GrowFromCenter(item) for item in args],
				lag_ratio=SMALL_LAG_RATIO
			) for i, args in [(line_FX, [dot_X, label_X]), (line_GY, [dot_Y, label_Y])]],
			lag_ratio=LARGE_LAG_RATIO
		))
		self.wait(2)

		t12 = MathTex(
			#  0    1    2    3    4      5    6    7    8              9   10   11   12   13     14   15   16   17
			ANGLE, 'X', 'D', 'A', '=', ANGLE, 'F', 'D', 'B' + QQUAD, ANGLE, 'A', 'E', 'Y', '=', ANGLE, 'C', 'E', 'G'
		)
		t12.scale(label_scale_factor).next_to(t11, DOWN, y_buff)
		for i in [*range(4), *range(5, 9)]:
			t12[i].set_color(c3)
			t12[i+9].set_color(c4)

		self.add_foreground_mobjects(
			circle_ABC,
			angle_DBF, angle_FDB, angle_GCE, angle_CEG,
			triangle_ABC,
			line_GY, angle_XDA, line_FX,
			line_AD, line_AE, line_FB, line_FD, line_GC, line_GE,
			dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
			label_gamma, label_A, label_B, label_C, label_D, label_E, label_F, label_G, label_X, label_Y
		)
		self.play(Write(t12[:9]), Create(angle_XDA))
		self.wait()
		self.play(Write(t12[9:]), Create(angle_AEY))
		self.wait(2)

		t13 = MathTex(
			#0    1    2    3    4                  5    6    7    8    9
			'A', 'F', 'B', 'X', IS_CYCLIC + QQUAD, 'A', 'G', 'C', 'Y', IS_CYCLIC
		)
		t13.scale(label_scale_factor).next_to(t12, DOWN, y_buff)
		for i in range(4):
			t13[i].set_color(c3)
			t13[i+5].set_color(c4)
		self.play(Write(t13[:5]))
		self.wait()
		self.play(Write(t13[5:]))
		self.wait(2)

		t14 = MathTex(
			#  0    1    2    3    4      5    6    7    8              9   10   11   12   13     14   15   16   17
			ANGLE, 'A', 'X', 'D', '=', ANGLE, 'D', 'B', 'F' + QQUAD, ANGLE, 'E', 'Y', 'A', '=', ANGLE, 'G', 'C', 'E'
		)
		t14.scale(label_scale_factor).next_to(t12, DOWN, y_buff)
		for i in [*range(4), *range(5, 9)]:
			t14[i].set_color(c3)
			t14[i+9].set_color(c4)

		self.add_foreground_mobjects(
			circle_ABC,
			angle_DBF, angle_FDB, angle_GCE, angle_CEG,
			triangle_ABC,
			line_GY, angle_XDA, line_FX,
			line_AD, line_AE, line_AX, line_AY, line_FB, line_FD, line_GC, line_GE,
			dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
			label_gamma, label_A, label_B, label_C, label_D, label_E, label_F, label_G, label_X, label_Y
		)
		self.play(AnimationGroup(
			Create(line_AX),
			AnimationGroup(
				Create(angle_AXD),
				FadeOut(t13[4]),
				Write(t14[0]), *[ReplacementTransform(t13[i], t14[j]) for i, j in [(0, 1), (3, 2)]],
				Write(t14[3:7]), *[ReplacementTransform(t13[i], t14[j]) for i, j in [(2, 7), (1, 8)]]
			),
			Create(line_AY),
			AnimationGroup(
				Create(angle_EYA),
				FadeOut(t13[9]),
				Write(t14[9:11]), *[ReplacementTransform(t13[i], t14[j]) for i, j in [(8, 11), (5, 12)]],
				Write(t14[13:15]), *[ReplacementTransform(t13[i], t14[j]) for i, j in [(6, 15), (7, 16)]],
				Write(t14[17])
			),
			lag_ratio=LARGE_LAG_RATIO
		))
		self.wait(2)

		t15 = MathTex(
			#  0    1    2    3    4      5    6    7    8              9   10   11   12   13     14   15   16   17
			ANGLE, 'A', 'X', 'D', '=', ANGLE, 'X', 'D', 'A' + QQUAD, ANGLE, 'E', 'Y', 'A', '=', ANGLE, 'A', 'E', 'Y'
		)
		t15.scale(label_scale_factor).next_to(ref_line, DOWN, y_buff)
		for i in [*range(4), *range(5, 9)]:
			t15[i].set_color(c3)
			t15[i+9].set_color(c4)

		self.play(
			*[Uncreate(item) for item in [angle_DBF, angle_FDB, line_FB]],
			FadeOut(t11[:4], t11[5:9], t12[4:9], t14[4:9]),
			*[ReplacementTransform(*args) for args in [
				(t14[:4], t15[:4]), (t11[4], t15[4]), (t12[:4], t15[5:9])
			]]
		)
		self.play(
			*[Uncreate(item) for item in [angle_GCE, angle_CEG, line_GC]],
			FadeOut(t11[9:13], t11[14:], t12[13:], t14[13:]),
			*[ReplacementTransform(*args) for args in [
				(t14[9:13], t15[9:13]), (t11[13], t15[13]), (t12[9:13], t15[14:])
			]]
		)
		self.wait(2)

		t16 = MathTex(
			#0    1    2    3    4            5    6    7    8    9
			'A', 'X', '=', 'A', 'D' + QQUAD, 'A', 'Y', '=', 'A', 'E'
		)
		t16.scale(label_scale_factor).next_to(ref_line, DOWN, y_buff)
		for i in [0, 1, 3, 4]:
			t16[i].set_color(c3)
			t16[i+5].set_color(c4)
		self.play(
			FadeOut(*[t15[i] for i in [0, 3, 5, 6]]),
			*[ReplacementTransform(t15[i], t16[idx]) for idx, i in enumerate([1, 2, 4, 8, 7])]
		)
		self.play(
			FadeOut(*[t15[i] for i in [9, 10, 14, 17]]),
			*[ReplacementTransform(t15[i], t16[idx+5]) for idx, i in enumerate([12, 11, 13, 15, 16])]
		)
		self.wait(2)

		t17 = MathTex(
			#0    1    2    3    4    5    6    7    8    9   10
			'A', 'X', '=', 'A', 'D', '=', 'A', 'E', '=', 'A', 'Y'
		)
		t17.scale(label_scale_factor).move_to(ref_line)
		for i in [0, 1, 3, 4, 6, 7, 9, 10]:
			t17[i].set_color(c2)

		self.play(
			*[FadeOut(item) for item in [
				triangle_ABC,
				dot_B, dot_C,
				label_B, label_C,
				t4[:2], t4[3:]
			]],
			*[ReplacementTransform(*args) for args in [
				(t16[:5], t17[:5]),
				(t4[2], t17[5]),
				(t16[8:], t17[6:8]),
				(t16[7], t17[8]),
				(t16[5:7], t17[9:])
			]]
		)
		self.wait()

		t18 = MathTex(
			#0    1    2    3    4
			'X', 'Y', 'D', 'E', IS_CYCLIC
		)
		t18.scale(label_scale_factor).move_to(ref_line)
		for i in range(4):
			t18[i].set_color(c2)

		new_label_X = MP('$X$', dot_X, dir(88), label_scale_factor)
		new_label_Y = MP('$Y$', dot_Y, LEFT, label_scale_factor)
		new_label_D = MP('$D$', dot_D, DOWN, label_scale_factor)
		new_label_E = MP('$E$', dot_E, DOWN, label_scale_factor)

		shifting_up_factor = .4
		for item in [
			circle_Ar,
			angle_EYX, angle_EDX, angle_GFX,
			line_XY, line_DE, line_FG,
			new_label_X, new_label_Y, new_label_D, new_label_E,
			ref_line, t18
		]: item.shift(shifting_up_factor*UP)

		self.play(
			FadeOut(t3, shift=2*UP),
			*[item.animate.shift(shifting_up_factor*UP) for item in [
				circle_ABC,
				line_GY, angle_XDA, line_FX, angle_AEY,
				angle_AXD, angle_EYA,
				line_AD, line_AE, line_AX, line_AY, line_FD, line_GE,
				dot_A, dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
				label_gamma, label_A, label_D, label_E, label_F, label_G, label_X, label_Y,
				t17
			]], run_time=.7
		)
		self.play(
			*[Uncreate(item) for item in [
				line_AD, line_AE, line_AX, line_AY,
				angle_AXD, angle_XDA, angle_AEY, angle_EYA
			]],
			*[FadeOut(item) for item in [dot_A, label_A]],
			*[ClockwiseTransform(*args, float=SMALL_RADIUS) for args in [
				(label_X, new_label_X), (label_E, new_label_E)
			]],
			*[CounterclockwiseTransform(*args, float=SMALL_RADIUS) for args in [
				(label_Y, new_label_Y), (label_D, new_label_D)
			]],
			GrowFromCenter(circle_Ar),
			FadeOut(*[t17[i] for i in [0, 2, 3, 5, 6, 8, 9]]),
			*[ReplacementTransform(t17[i], t18[idx]) for idx, i in enumerate([1, 10, 4, 7])],
			Write(t18[4])
		)
		self.wait()

		t19 = MathTex(
			#0    1    2    3    4                  5    6    7    8    9
			'X', 'Y', 'D', 'E', IS_CYCLIC + QQUAD, 'X', 'Y', 'F', 'G', IS_CYCLIC
		)
		t19.scale(label_scale_factor).move_to(ref_line)
		for i in range(4):
			t19[i].set_color(c2)
			t19[i+5].set_color(c6)
		self.play(AnimationGroup(
			ReplacementTransform(t18, t19[:5]), Write(t19[5:]),
			lag_ratio=LARGE_LAG_RATIO
		))
		self.wait()

		t20 = MathTex(
			#  0    1    2    3    4      5    6    7    8              9   10   11   12   13     14   15   16   17
			ANGLE, 'E', 'Y', 'X', '=', ANGLE, 'E', 'D', 'X' + QQUAD, ANGLE, 'G', 'Y', 'X', '=', ANGLE, 'G', 'F', 'X'
		)
		t20.scale(label_scale_factor).move_to(ref_line)
		for i in [*range(4), *range(5, 9)]:
			t20[i].set_color(c2)
			t20[i+9].set_color(c6)

		self.add_foreground_mobjects(
			circle_ABC, circle_Ar,
			angle_EYX, angle_EDX,
			line_XY, line_DE, line_GY, line_FX, line_FD, line_GE,
			dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
			label_gamma, label_D, label_E, label_F, label_G, label_X, label_Y
		)
		self.play(AnimationGroup(
			Create(line_XY),
			AnimationGroup(
				Create(angle_EYX),
				FadeOut(*[t19[i] for i in [2, 4]]),
				Write(t20[0]),
				*[ReplacementTransform(t19[i], t20[idx+1]) for idx, i in enumerate([3, 1, 0])]
			),
			Write(t20[4]),
			Create(line_DE),
			AnimationGroup(Create(angle_EDX), Write(t20[5:9])),
			lag_ratio=MED_LAG_RATIO
		))
		self.wait()

		self.add_foreground_mobjects(
			circle_ABC, circle_Ar,
			angle_EYX, angle_EDX, angle_GFX,
			line_XY, line_DE, line_FG, line_GY, line_FX, line_FD, line_GE,
			dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
			label_gamma, label_D, label_E, label_F, label_G, label_X, label_Y
		)
		self.play(AnimationGroup(
			AnimationGroup(
				FadeOut(*[t19[i] for i in [7, 9]]),
				Write(t20[9]),
				*[ReplacementTransform(t19[i], t20[idx+10]) for idx, i in enumerate([8, 6, 5])]
			),
			Write(t20[13]),
			Create(line_FG),
			AnimationGroup(Create(angle_GFX), Write(t20[14:])),
			lag_ratio=MED_LAG_RATIO
		))
		self.wait(2)

		t21 = MathTex(
			#  0    1    2    3    4      5    6    7    8    9     10   11   12   13   14     15   16   17   18
			ANGLE, 'E', 'D', 'X', '=', ANGLE, 'E', 'Y', 'X', '=', ANGLE, 'G', 'Y', 'X', '=', ANGLE, 'G', 'F', 'X'
		)
		t21.scale(label_scale_factor).move_to(ref_line)
		for i in [*range(4), *range(5, 9), *range(10, 14), *range(15, 19)]:
			t21[i].set_color(c5)
		self.play(*[ReplacementTransform(*args) for args in [
			(t20[5:9], t21[:4]), (t20[4], t21[4]), (t20[:4], t21[5:9]), (t20[9:], t21[10:])
		]], Write(t21[9]))
		self.wait()

		t22 = MathTex(
			#  0    1    2    3    4      5    6    7    8
			ANGLE, 'E', 'D', 'X', '=', ANGLE, 'G', 'F', 'X'
		)
		t22.scale(label_scale_factor).move_to(ref_line)
		for i in [*range(4), *range(5, 9)]:
			t22[i].set_color(c5)

		new_label_X = MP('$X$', dot_X, UP, label_scale_factor)
		new_label_Y = MP('$Y$', dot_Y, dir(Y), label_scale_factor)
		new_label_D = MP('$D$', dot_D, dir(179), label_scale_factor)
		new_label_E = MP('$E$', dot_E, dir(82), label_scale_factor)
		for item in [new_label_X, new_label_Y, new_label_D, new_label_E, t22, ref_line]:
			item.shift(shifting_up_factor*DOWN)

		self.play(
			FadeOut(circle_Ar),
			FadeIn(t3, shift=2*DOWN),
			*[item.animate.shift(shifting_up_factor*DOWN) for item in [
				circle_ABC,
				angle_EYX, angle_EDX, angle_GFX,
				line_XY, line_DE, line_FG, line_GY, line_FX, line_FD, line_GE,
				dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
				label_gamma, label_D, label_E, label_F, label_G, label_X, label_Y,
				t21
			]], run_time=.7
		)
		self.play(
			*[Uncreate(item) for item in [line_XY, angle_EYX]],
			*[CounterclockwiseTransform(*args, float=SMALL_RADIUS) for args in [
				(label_X, new_label_X), (label_E, new_label_E)
			]],
			*[ClockwiseTransform(*args, float=SMALL_RADIUS) for args in [
				(label_Y, new_label_Y), (label_D, new_label_D)
			]],
			*[FadeOut(t21[i+4]) for i in [*range(5), *range(6, 11)]],
			*[ReplacementTransform(*args) for args in [
				(t21[:4], t22[:4]), (t21[9], t22[4]), (t21[15:], t22[5:])
			]]
		)
		self.wait(2)

		t23 = MathTex(
			#0    1    2    3    4    5
			'D', 'E', AND, 'F', 'G', ARE_PARALLEL
		)
		t23.scale(.7).next_to(ref_line, DOWN, 1.5)
		for i in [0, 1, 3, 4]:
			t23[i].set_color(c5)
		self.play(
			FadeOut(*[t22[i] for i in [0, 3, 4, 5, 8]]),
			*[Write(t23[i]) for i in [2, 5]],
			*[ReplacementTransform(t22[i], t23[j]) for i, j in [(2, 0), (1, 1), (7, 3), (6, 4)]]
		)
		self.wait(2)

		for i in range(2):
			self.play(Circumscribe(t23))
		self.wait()

		self.play(*[FadeOut(item, shift=DOWN) for item in self.mobjects])

		ending_credit = Tex('Video hecho con ', r'\textsc{Manim}')
		ending_credit.scale(1.5)
		ending_credit[1].set_color_by_gradient(TEAL_E, TEAL_A)
		for i in range(2):
			self.play(Write(ending_credit[i]))
		self.wait()
		self.play(FadeOut(ending_credit, shift=DOWN))
		self.wait()
