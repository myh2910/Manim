from asymptote import *

class Video(Scene):
	def construct(self):
		self.add_sound("assets/2018_1.mp3")
		logo = ImageMobject('assets/2018.png')

		self.play(FadeInFrom(logo, DOWN))

		t1 = Tex(r"\textsf{Problema 1}").set_color_by_gradient(TEAL_E, TEAL_A)
		t1.scale(2.6).shift(2.7*RIGHT+.2*DOWN)
		t2 = Tex(r'\emph{Soluci\'on}').set_color(YELLOW_B)
		t2.scale(2).shift(2.7*RIGHT+.9*DOWN)
		short_lag_ratio, med_lag_ratio, long_lag_ratio = .5, .8, 1

		self.play(AnimationGroup(
			logo.animate.shift(3.7*LEFT),
			Write(t1),
			lag_ratio=med_lag_ratio
		))
		self.play(
			t1.animate.shift(.6*UP),
			FadeInFrom(t2, DOWN),
			lag_ratio=.1,
			float=linear
		)
		self.wait(1.5)

		t3 = Tex(
			r"\textbf{Problema 1.}\ \ ", #0
			r"Sea $\Gamma$ la circunferencia circunscrita al tri\'angulo acut\'angulo $ABC$. Los puntos $D$ y $E$ est\'an en los segmentos $AB$ y $AC$, respectivamente, y son tales que $AD=AE$. Las mediatrices de $BD$ y $CE$ cortan a los arcos menores $AB$ y $AC$ de $\Gamma$ en los puntos $F$ y $G$, respectivamente. Demostrar que las rectas $DE$ y $FG$ son paralelas (o son la misma recta).", #1
			tex_environment=None,
			tex_template=TEX_TEMPLATE('512.34pt')
		)
		t3[0].set_color_by_gradient(TEAL_E, TEAL_A)
		t3.scale(.5).to_corner(UP)
		shifting_factor = 12
		
		self.play(
			*[FadeOutAndShift(item, shifting_factor*LEFT) for item in [logo, t2]],
			ReplacementTransform(t1[0], t3[0]),
			FadeInFrom(t3[1], shifting_factor*RIGHT)
		)
		self.wait()

		A, B, C = dir(120), dir(210), dir(330)
		r = .5
		D, E = A + r*(B-A)/distance(A, B), A + r*(C-A)/distance(C, A)
		l = dir(2*degrees(np.arcsin(r/2)))
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
		label_A = MP("$A$", dot_A, A, label_scale_factor)
		label_B = MP("$B$", dot_B, B, label_scale_factor)
		label_C = MP("$C$", dot_C, C, label_scale_factor)
		label_D = MP("$D$", dot_D, dir(179), label_scale_factor)
		label_E = MP("$E$", dot_E, dir(82), label_scale_factor)
		label_F = MP("$F$", dot_F, F, label_scale_factor)
		label_G = MP("$G$", dot_G, G, label_scale_factor)
		label_X = MP("$X$", dot_X, UP, label_scale_factor)
		label_Y = MP("$Y$", dot_Y, Y, label_scale_factor)
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
		shifting_left_factor, shifting_down_factor =  2.8, .9
		for item in [
			circle_ABC,
			angle_DBF, angle_FDB, angle_XDA, angle_AXD,
			angle_GCE, angle_CEG, angle_AEY, angle_EYA,
			angle_EYX, angle_EDX, angle_GFX,
			triangle_ABC,
			line_FX, line_GY,
			circle_Ar,
			line_AD, line_AE, line_AX, line_AY,
			line_FB, line_FD,
			line_GC, line_GE,
			line_XY, line_DE, line_FG,
			dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
			label_gamma, label_A, label_B, label_C, label_D, label_E, label_F, label_G, label_X, label_Y
		]:
			item.shift(shifting_left_factor*LEFT+shifting_down_factor*DOWN)
		self.add_foreground_mobjects(
			dot_A, dot_B, dot_C,
			label_A, label_B, label_C
		)
		self.play(
			t3.animate.scale(.88).to_corner(UP).shift(.2*UP),
			*[FadeInFrom(item, shifting_left_factor*RIGHT) for item in [
				circle_ABC, triangle_ABC,
				dot_A, dot_B, dot_C,
				label_gamma, label_A, label_B, label_C
			]]
		)
		self.wait(.5)

		t4 = MathTex(
			"A", #0
			"D", #1
			"=", #2
			"A", #3
			"E" #4
		)
		t4.scale(label_scale_factor).shift(3.5*RIGHT+1.2*UP)
		for i in [0, 1, 3, 4]: t4[i].set_color(c2)
		ref_line = t4.copy()
		self.add_foreground_mobjects(
			dot_D, dot_E,
			label_D, label_E
		)
		self.play(AnimationGroup(
			AnimationGroup(Create(line_AD), Write(t4[0])),
			GrowFromCenter(dot_D),
			AnimationGroup(GrowFromCenter(label_D), Write(t4[1])),
			Write(t4[2]),
			AnimationGroup(Create(line_AE), Write(t4[3])),
			GrowFromCenter(dot_E),
			AnimationGroup(GrowFromCenter(label_E),  Write(t4[4])),
			lag_ratio=.4
		))
		y_buff = .3
		t5 = MathTex(
			"F", #0
			r"\text{ pertenece a la mediatriz de }", #1
			"B", #2
			"D" #3
		)
		t5.scale(label_scale_factor).next_to(ref_line, DOWN, y_buff)
		for i in [0, 2, 3]: t5[i].set_color(c3)
		t6 = MathTex(
			"G", #0
			r"\text{ pertenece a la mediatriz de }", #1
			"C", #2
			"E" #3
		)
		t6.scale(label_scale_factor).next_to(t5, DOWN, y_buff)
		for i in [0, 2, 3]: t6[i].set_color(c4)
		t7 = MathTex(
			"F", #0
			"B", #1
			"=", #2
			"F", #3
			"D" #4
		)
		t7.scale(label_scale_factor).next_to(ref_line, DOWN, y_buff)
		for i in [0, 1, 3, 4]: t7[i].set_color(c3)
		t8 = MathTex(
			"G", #0
			"C", #1
			"=", #2
			"G", #3
			"E" #4
		)
		t8.scale(label_scale_factor).next_to(t5, DOWN, y_buff)
		for i in [0, 1, 3, 4]: t8[i].set_color(c4)
		angle = r"\angle "
		t9 = MathTex(
			angle, #0
			"D", #1
			"B", #2
			"F", #3
			"=", #4
			angle, #5
			"F", #6
			"D", #7
			"B" #8
		)
		t9.scale(label_scale_factor).next_to(ref_line, DOWN, y_buff)
		for i in [*range(0, 4), *range(5, 9)]: t9[i].set_color(c3)
		t10 = MathTex(
			angle, #0
			"G", #1
			"C", #2
			"E", #3
			"=", #4
			angle, #5
			"C", #6
			"E", #7
			"G" #8
		)
		t10.scale(label_scale_factor).next_to(t5, DOWN, y_buff)
		for i in [*range(0, 4), *range(5, 9)]: t10[i].set_color(c4)
		self.add_foreground_mobjects(dot_F, label_F)

		self.play(AnimationGroup(
			GrowFromCenter(dot_F),
			AnimationGroup(GrowFromCenter(label_F), Write(t5[0])),
			Write(t5[1:]),
			lag_ratio=short_lag_ratio
		))
		self.add_foreground_mobjects(dot_G, label_G)

		self.play(AnimationGroup(
			GrowFromCenter(dot_G),
			AnimationGroup(GrowFromCenter(label_G), Write(t6[0])),
			Write(t6[1:]),
			lag_ratio=short_lag_ratio
		))
		self.wait(2)
		self.play(
			Create(line_FB),
			Create(line_FD),
			FadeOut(t5[0:2]),
			*TC(t5[0], t7[0]),
			ReplacementTransform(t5[2], t7[1]),
			Write(t7[2]),
			*TC(t5[0], t7[3]),
			ReplacementTransform(t5[3], t7[4])
		)
		self.play(
			Create(line_GC),
			Create(line_GE),
			FadeOut(t6[0:2]),
			*TC(t6[0], t8[0]),
			ReplacementTransform(t6[2], t8[1]),
			Write(t8[2]),
			*TC(t6[0], t8[3]),
			ReplacementTransform(t6[3], t8[4])
		)
		self.wait(2)

		self.add_foreground_mobjects(
			circle_ABC,
			angle_DBF, angle_FDB,
			triangle_ABC,
			line_AD, line_AE,
			line_FB, line_FD,
			line_GC, line_GE,
			dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G,
			label_gamma, label_A, label_B, label_C, label_D, label_E, label_F, label_G
		)
		self.play(
			Create(angle_DBF),
			Create(angle_FDB),
			FadeOut(t7[1]),
			FadeOut(t7[4]),
			Write(t9[0]),
			*TC(t7[4], t9[1]),
			*TC(t7[1], t9[2]),
			ReplacementTransform(t7[0], t9[3]),
			ReplacementTransform(t7[2], t9[4]),
			Write(t9[5]),
			ReplacementTransform(t7[3], t9[6]),
			*TC(t7[4], t9[7]),
			*TC(t7[1], t9[8])
		)
		self.add_foreground_mobjects(
			circle_ABC,
			angle_DBF, angle_FDB,
			angle_GCE, angle_CEG,
			triangle_ABC,
			line_AD, line_AE,
			line_FB, line_FD,
			line_GC, line_GE,
			dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G,
			label_gamma, label_A, label_B, label_C, label_D, label_E, label_F, label_G
		)
		self.play(
			Create(angle_GCE),
			Create(angle_CEG),
			FadeOut(t8[1]),
			FadeOut(t8[4]),
			Write(t10[0]),
			ReplacementTransform(t8[0], t10[1]),
			*TC(t8[1], t10[2]),
			*TC(t8[4], t10[3]),
			ReplacementTransform(t8[2], t10[4]),
			Write(t10[5]),
			*TC(t8[1], t10[6]),
			*TC(t8[4], t10[7]),
			ReplacementTransform(t8[3], t10[8])
		)
		self.wait(2)

		x_space = r"\qquad"
		t11 = MathTex(
			angle, #0
			"D", #1
			"B", #2
			"F", #3
			"=", #4
			angle, #5
			"F", #6
			"D", #7
			"B" + x_space, #8
			angle, #9
			"G", #10
			"C", #11
			"E", #12
			"=", #13
			angle, #14
			"C", #15
			"E", #16
			"G", #17
		)
		t11.scale(label_scale_factor).next_to(ref_line, DOWN, y_buff)
		for i in [*range(0, 4), *range(5, 9)]: t11[i].set_color(c3)
		for i in [*range(9, 13), *range(14, 18)]: t11[i].set_color(c4)

		self.play(
			ReplacementTransform(t9, t11[:9]),
			ReplacementTransform(t10, t11[9:])
		)
		self.add_foreground_mobjects(
			circle_ABC,
			angle_DBF, angle_FDB,
			angle_GCE, angle_CEG,
			triangle_ABC,
			line_GY, line_FX,
			line_AD, line_AE,
			line_FB, line_FD,
			line_GC, line_GE,
			dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
			label_gamma, label_A, label_B, label_C, label_D, label_E, label_F, label_G, label_X, label_Y
		)
		self.play(AnimationGroup(
			AnimationGroup(
				Create(line_FX),
				*[GrowFromCenter(item) for item in [dot_X, label_X]],
				lag_ratio=short_lag_ratio
			),
			AnimationGroup(
				Create(line_GY),
				*[GrowFromCenter(item) for item in [dot_Y, label_Y]],
				lag_ratio=short_lag_ratio
			),
			lag_ratio=long_lag_ratio
		))
		self.wait(2)

		t12 = MathTex(
			angle, #0
			"X", #1
			"D", #2
			"A", #3
			"=", #4
			angle, #5
			"F", #6
			"D", #7
			"B" + x_space, #8
			angle, #9
			"A", #10
			"E", #11
			"Y", #12
			"=", #13
			angle, #14
			"C", #15
			"E", #16
			"G" #17
		)
		t12.scale(label_scale_factor).next_to(t11, DOWN, y_buff)
		for i in [*range(0, 4), *range(5, 9)]: t12[i].set_color(c3)
		for i in [*range(9, 13), *range(14, 18)]: t12[i].set_color(c4)
		self.add_foreground_mobjects(
			circle_ABC,
			angle_DBF, angle_FDB,
			angle_GCE, angle_CEG,
			triangle_ABC,
			line_GY, angle_XDA, line_FX,
			line_AD, line_AE,
			line_FB, line_FD,
			line_GC, line_GE,
			dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
			label_gamma, label_A, label_B, label_C, label_D, label_E, label_F, label_G, label_X, label_Y
		)
		self.play(
			Write(t12[:9]),
			Create(angle_XDA)
		)
		self.wait()
		self.play(
			Write(t12[9:]),
			Create(angle_AEY)
		)
		self.wait(2)

		is_cyclic = r"\text{ es c\'iclico}"
		t13 = MathTex(
			"A", #0
			"F", #1
			"B", #2
			"X", #3
			is_cyclic + x_space, #4
			"A", #5
			"G", #6
			"C", #7
			"Y", #8
			is_cyclic #9
		)
		t13.scale(label_scale_factor).next_to(t12, DOWN, y_buff)
		for i in range(0, 4): t13[i].set_color(c3)
		for i in range(5, 9): t13[i].set_color(c4)

		self.play(Write(t13[:5]))
		self.wait()
		self.play(Write(t13[5:]))
		self.wait(2)

		t14 = MathTex(
			angle, #0
			"A", #1
			"X", #2
			"D", #3
			"=", #4
			angle, #5
			"D", #6
			"B", #7
			"F" + x_space, #8
			angle, #9
			"E", #10
			"Y", #11
			"A", #12
			"=", #13
			angle, #14
			"G", #15
			"C", #16
			"E" #17
		)
		t14.scale(label_scale_factor).next_to(t12, DOWN, y_buff)
		for i in [*range(0, 4), *range(5, 9)]: t14[i].set_color(c3)
		for i in [*range(9, 13), *range(14, 18)]: t14[i].set_color(c4)
		
		self.add_foreground_mobjects(
			circle_ABC,
			angle_DBF, angle_FDB,
			angle_GCE, angle_CEG,
			triangle_ABC,
			line_GY, angle_XDA, line_FX,
			line_AD, line_AE, line_AX, line_AY,
			line_FB, line_FD,
			line_GC, line_GE,
			dot_A, dot_B, dot_C, dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
			label_gamma, label_A, label_B, label_C, label_D, label_E, label_F, label_G, label_X, label_Y
		)
		self.play(AnimationGroup(
			Create(line_AX),
			AnimationGroup(
				Create(angle_AXD),
				FadeOut(t13[4]),
				Write(t14[0]),
				ReplacementTransform(t13[0], t14[1]),
				ReplacementTransform(t13[3], t14[2]),
				Write(t14[3:7]),
				ReplacementTransform(t13[2], t14[7]),
				ReplacementTransform(t13[1], t14[8])
			),
			Create(line_AY),
			AnimationGroup(
				Create(angle_EYA),
				FadeOut(t13[9]),
				Write(t14[9:11]),
				ReplacementTransform(t13[8], t14[11]),
				ReplacementTransform(t13[5], t14[12]),
				Write(t14[13:15]),
				ReplacementTransform(t13[6], t14[15]),
				ReplacementTransform(t13[7], t14[16]),
				Write(t14[17])
			),
			lag_ratio=long_lag_ratio
		))
		self.wait(2)

		t15 = MathTex(
			angle, #0
			"A", #1
			"X", #2
			"D", #3
			"=", #4
			angle, #5
			"X", #6
			"D", #7
			"A" + x_space, #8
			angle, #9
			"E", #10
			"Y", #11
			"A", #12
			"=", #13
			angle, #14
			"A", #15
			"E", #16
			"Y" #17
		)
		t15.scale(label_scale_factor).next_to(ref_line, DOWN, y_buff)
		for i in [*range(0, 4), *range(5, 9)]: t15[i].set_color(c3)
		for i in [*range(9, 13), *range(14, 18)]: t15[i].set_color(c4)

		self.play(
			*[Uncreate(item) for item in [angle_DBF, angle_FDB, line_FB]],
			*[FadeOut(item) for item in [t11[:4], t11[5:9], t12[4:9], t14[4:9]]],
			ReplacementTransform(t14[:4], t15[:4]),
			ReplacementTransform(t11[4], t15[4]),
			ReplacementTransform(t12[:4], t15[5:9])
		)
		self.play(
			*[Uncreate(item) for item in [angle_GCE, angle_CEG, line_GC]],
			*[FadeOut(item) for item in [t11[9:13], t11[14:], t12[13:], t14[13:]]],
			ReplacementTransform(t14[9:13], t15[9:13]),
			ReplacementTransform(t11[13], t15[13]),
			ReplacementTransform(t12[9:13], t15[14:])
		)
		self.wait(2)

		t16 = MathTex(
			"A", #0
			"X", #1
			"=", #2
			"A", #3
			"D" + x_space, #4
			"A", #5
			"Y", #6
			"=", #7
			"A", #8
			"E" #9
		)
		t16.scale(label_scale_factor).next_to(ref_line, DOWN, y_buff)
		for i in [0, 1, 3, 4]: t16[i].set_color(c3)
		for i in [5, 6, 8, 9]: t16[i].set_color(c4)

		self.play(
			*[FadeOut(t15[i]) for i in [0, 3, 5, 6]],
			ReplacementTransform(t15[1], t16[0]),
			ReplacementTransform(t15[2], t16[1]),
			ReplacementTransform(t15[4], t16[2]),
			ReplacementTransform(t15[8], t16[3]),
			ReplacementTransform(t15[7], t16[4])
		)
		self.play(
			*[FadeOut(t15[i]) for i in [9, 10, 14, 17]],
			ReplacementTransform(t15[12], t16[5]),
			ReplacementTransform(t15[11], t16[6]),
			ReplacementTransform(t15[13], t16[7]),
			ReplacementTransform(t15[15], t16[8]),
			ReplacementTransform(t15[16], t16[9])
		)
		self.wait(2)

		t17 = MathTex(
			"A", #0
			"X", #1
			"=", #2
			"A", #3
			"D", #4
			"=", #5
			"A", #6
			"E", #7
			"=", #8
			"A", #9
			"Y" #10
		)
		t17.scale(label_scale_factor).move_to(ref_line)
		for i in [0, 1, 3, 4, 6, 7, 9, 10]: t17[i].set_color(c2)

		self.play(
			*[FadeOut(item) for item in [
				triangle_ABC,
				dot_B, dot_C,
				label_B, label_C,
				t4[:2], t4[3:]
			]],
			ReplacementTransform(t16[:5], t17[:5]),
			ReplacementTransform(t4[2], t17[5]),
			ReplacementTransform(t16[8:], t17[6:8]),
			ReplacementTransform(t16[7], t17[8]),
			ReplacementTransform(t16[5:7], t17[9:])
		)
		self.wait()

		t18 = MathTex(
			"X", #0
			"Y", #1
			"D", #2
			"E", #3
			is_cyclic #4
		)
		t18.scale(label_scale_factor).move_to(ref_line)
		for i in range(0, 4): t18[i].set_color(c2)
		new_label_X = MP('$X$', dot_X, dir(88), label_scale_factor)
		new_label_Y = MP('$Y$', dot_Y, LEFT, label_scale_factor)
		new_label_D = MP('$D$', dot_D, DOWN, label_scale_factor)
		new_label_E = MP('$E$', dot_E, DOWN, label_scale_factor)
		radius_float = .01
		shifting_up_factor = .4
		for item in [
			circle_Ar,
			angle_EYX, angle_EDX, angle_GFX,
			line_XY, line_DE, line_FG,
			new_label_X, new_label_Y, new_label_D, new_label_E,
			ref_line, t18
		]:
			item.shift(shifting_up_factor*UP)

		self.play(
			FadeOutAndShift(t3, 2*UP),
			*[item.animate.shift(shifting_up_factor*UP) for item in [
				circle_ABC,
				line_GY, angle_XDA, line_FX, angle_AEY,
				angle_AXD, angle_EYA,
				line_AD, line_AE, line_AX, line_AY,
				line_FD, line_GE,
				dot_A, dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
				label_gamma, label_A, label_D, label_E, label_F, label_G, label_X, label_Y,
				t17
			]],
			run_time=.7
		)
		self.play(
			*[Uncreate(item) for item in [
				line_AD, line_AE, line_AX, line_AY,
				angle_AXD, angle_XDA,
				angle_AEY, angle_EYA
			]],
			*[FadeOut(item) for item in [dot_A, label_A]],
			ClockwiseTransform(label_X, new_label_X, float=radius_float),
			CounterclockwiseTransform(label_Y, new_label_Y, float=radius_float),
			CounterclockwiseTransform(label_D, new_label_D, float=radius_float),
			ClockwiseTransform(label_E, new_label_E, float=radius_float),
			GrowFromCenter(circle_Ar),
			*[FadeOut(t17[i]) for i in [0, 2, 3, 5, 6, 8, 9]],
			ReplacementTransform(t17[1], t18[0]),
			ReplacementTransform(t17[10], t18[1]),
			ReplacementTransform(t17[4], t18[2]),
			ReplacementTransform(t17[7], t18[3]),
			Write(t18[4])
		)
		self.wait()

		t19 = MathTex(
			"X", #0
			"Y", #1
			"D", #2
			"E", #3
			is_cyclic + x_space, #4
			"X", #5
			"Y", #6
			"F", #7
			"G", #8
			is_cyclic #9
		)
		t19.scale(label_scale_factor).move_to(ref_line)
		for i in range(0, 4): t19[i].set_color(c2)
		for i in range(5, 9): t19[i].set_color(c6)

		self.play(AnimationGroup(
			ReplacementTransform(t18, t19[:5]),
			Write(t19[5:]),
			lag_ratio=long_lag_ratio
		))
		self.wait()

		t20 = MathTex(
			angle, #0
			"E", #1
			"Y", #2
			"X", #3
			"=", #4
			angle, #5
			"E", #6
			"D", #7
			"X" + x_space, #8
			angle, #9
			"G", #10
			"Y", #11
			"X", #12
			"=", #13
			angle, #14
			"G", #15
			"F", #16
			"X" #17
		)
		t20.scale(label_scale_factor).move_to(ref_line)
		for i in [*range(0, 4), *range(5, 9)]: t20[i].set_color(c2)
		for i in [*range(9, 13), *range(14, 18)]: t20[i].set_color(c6)
		self.add_foreground_mobjects(
			circle_ABC, circle_Ar,
			angle_EYX, angle_EDX,
			line_XY, line_DE,
			line_GY, line_FX,
			line_FD, line_GE,
			dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
			label_gamma, label_D, label_E, label_F, label_G, label_X, label_Y
		)
		self.play(AnimationGroup(
			Create(line_XY),
			AnimationGroup(
				Create(angle_EYX),
				*[FadeOut(t19[i]) for i in [2, 4]],
				Write(t20[0]),
				ReplacementTransform(t19[3], t20[1]),
				ReplacementTransform(t19[1], t20[2]),
				ReplacementTransform(t19[0], t20[3])
			),
			Write(t20[4]),
			Create(line_DE),
			AnimationGroup(
				Create(angle_EDX),
				Write(t20[5:9])
			),
			lag_ratio=med_lag_ratio
		))
		self.wait()

		self.add_foreground_mobjects(
			circle_ABC, circle_Ar,
			angle_EYX, angle_EDX, angle_GFX,
			line_XY, line_DE, line_FG,
			line_GY, line_FX,
			line_FD, line_GE,
			dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
			label_gamma, label_D, label_E, label_F, label_G, label_X, label_Y
		)
		self.play(AnimationGroup(
			AnimationGroup(
				*[FadeOut(t19[i]) for i in [7, 9]],
				Write(t20[9]),
				ReplacementTransform(t19[8], t20[10]),
				ReplacementTransform(t19[6], t20[11]),
				ReplacementTransform(t19[5], t20[12])
			),
			Write(t20[13]),
			Create(line_FG),
			AnimationGroup(
				Create(angle_GFX),
				Write(t20[14:])
			),
			lag_ratio=med_lag_ratio
		))
		self.wait(2)

		t21 = MathTex(
			angle, #0
			"E", #1
			"D", #2
			"X", #3
			"=", #4
			angle, #5
			"E", #6
			"Y", #7
			"X", #8
			"=", #9
			angle, #10
			"G", #11
			"Y", #12
			"X", #13
			"=", #14
			angle, #15
			"G", #16
			"F", #17
			"X" #18
		)
		t21.scale(label_scale_factor).move_to(ref_line)
		for i in [*range(0, 4), *range(5, 9), *range(10, 14), *range(15, 19)]: t21[i].set_color(c5)

		self.play(
			ReplacementTransform(t20[5:9], t21[:4]),
			ReplacementTransform(t20[4], t21[4]),
			ReplacementTransform(t20[:4], t21[5:9]),
			Write(t21[9]),
			ReplacementTransform(t20[9:], t21[10:])
		)
		self.wait()

		t22 = MathTex(
			angle, #0
			"E", #1
			"D", #2
			"X", #3
			"=", #4
			angle, #5
			"G", #6
			"F", #7
			"X" #8
		)
		t22.scale(label_scale_factor).move_to(ref_line)
		for i in [*range(0, 4), *range(5, 9)]: t22[i].set_color(c5)
		new_label_X = MP('$X$', dot_X, UP, label_scale_factor)
		new_label_Y = MP('$Y$', dot_Y, dir(Y), label_scale_factor)
		new_label_D = MP('$D$', dot_D, dir(179), label_scale_factor)
		new_label_E = MP('$E$', dot_E, dir(82), label_scale_factor)
		for item in [
			new_label_X, new_label_Y, new_label_D, new_label_E,
			t22,
			ref_line
		]:
			item.shift(shifting_up_factor*DOWN)

		self.play(
			FadeOut(circle_Ar),
			FadeInFrom(t3, 2*UP),
			*[item.animate.shift(shifting_up_factor*DOWN) for item in [
				circle_ABC,
				angle_EYX, angle_EDX, angle_GFX,
				line_XY, line_DE, line_FG,
				line_GY, line_FX,
				line_FD, line_GE,
				dot_D, dot_E, dot_F, dot_G, dot_X, dot_Y,
				label_gamma, label_D, label_E, label_F, label_G, label_X, label_Y,
				t21
			]],
			run_time=.7
		)
		self.play(
			*[Uncreate(item) for item in [line_XY, angle_EYX]],
			CounterclockwiseTransform(label_X, new_label_X, float=radius_float),
			ClockwiseTransform(label_Y, new_label_Y, float=radius_float),
			ClockwiseTransform(label_D, new_label_D, float=radius_float),
			CounterclockwiseTransform(label_E, new_label_E, float=radius_float),
			*[FadeOut(t21[i]) for i in [*range(4, 9), *range(10, 15)]],
			ReplacementTransform(t21[:4], t22[:4]),
			ReplacementTransform(t21[9], t22[4]),
			ReplacementTransform(t21[15:], t22[5:])
		)
		self.wait(2)

		t23 = MathTex(
			"D", #0
			"E", #1
			r"\text{ y }", #2
			"F", #3
			"G", #4
			r"\text{ son paralelas}" #5
		)
		t23.scale(.7).next_to(ref_line, DOWN, 1.5)
		for i in [0, 1, 3, 4]: t23[i].set_color(c5)

		self.play(
			*[FadeOut(t22[i]) for i in [0, 3, 4, 5, 8]],
			ReplacementTransform(t22[2], t23[0]),
			ReplacementTransform(t22[1], t23[1]),
			Write(t23[2]),
			ReplacementTransform(t22[7], t23[3]),
			ReplacementTransform(t22[6], t23[4]),
			Write(t23[5])
		)
		self.wait(2)
		self.play(Circumscribe(t23))
		self.play(Circumscribe(t23))
		self.wait()
		self.play(*[FadeOut(item, shift=DOWN) for item in self.mobjects])

		ending_credit = Tex(
			"Video hecho con ",
			r"\textsc{Manim}"
		)
		ending_credit.scale(1.5)
		ending_credit[1].set_color_by_gradient(TEAL_E, TEAL_A)

		self.play(Write(ending_credit[0]))
		self.play(Write(ending_credit[1]))
		self.wait()
		self.play(FadeOut(ending_credit, shift=DOWN))
		self.wait()
