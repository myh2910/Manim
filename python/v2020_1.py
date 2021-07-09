from asymptote import *

class Video(Scene):
	def construct(self):
		self.add_sound('assets/2020_1.mp3')
		logo = ImageMobject('assets/2020.png')
		self.play(FadeIn(logo, shift=UP))

		t1 = Tex(r'\textsf{Problema 1}').set_color_by_gradient('#3c94d4', BLUE_B)
		t1.scale(2.5).shift(.3*UP+3.6*RIGHT)
		self.play(AnimationGroup(logo.animate.shift(3.1*LEFT), Write(t1), lag_ratio=.8))
		self.wait(.5)

		t2 = Tex(
			r'\textbf{Problema 1.} \ \ ',
			r"Considere el cuadril\'atero convexo $ABCD$. El punto $P$ est\'a en el interior de $ABCD$. Asuma las siguientes igualdades de razones: $$\angle PAD:\angle PBA:\angle DPA=1:2:3=\angle CBP:\angle BAP:\angle BPC.$$ Demuestre que las siguientes tres rectas concurren en un punto: la bisectriz interna del \'angulo $\angle ADP$, la bisectriz interna del \'angulo $\angle PCB$ y la mediatriz del segmento $AB$.",
			tex_environment=None,
			tex_template=TEX_TEMPLATE('512.34pt')
		)
		t2[0].set_color_by_gradient(GOLD, GOLD_A)
		t2.scale(.5).to_corner(UP)
		self.play(AnimationGroup(
			FadeOut(logo), ReplacementTransform(t1, t2[0]),
			run_time=2, lag_ratio=.5
		))
		self.play(Create(t2[1]), run_time=4)
		self.wait()
		self.play(t2.animate.scale(.88).to_corner(UP))

		alpha, beta = 18, 32
		P = dir(5*beta-90)
		B = dir(-3*beta-90)
		C = dir(3*beta-90)
		A = sim(B, P, dir(2*alpha+2*beta+90), dir(-2*alpha-2*beta+90), dir(-2*alpha+2*beta+90))
		D = sim(A, P, dir(-2*alpha+90), dir(4*alpha+90), dir(-4*alpha+90))
		O = circumcenter(P, A, B)

		scale_factor = 2.5
		P *= scale_factor
		A *= scale_factor
		B *= scale_factor
		C *= scale_factor
		D *= scale_factor
		O *= scale_factor

		displacement_vector = comp((0, (origin-P).imag))
		P += displacement_vector
		A += displacement_vector
		B += displacement_vector
		C += displacement_vector
		D += displacement_vector
		O += displacement_vector

		dot_P, dot_A, dot_B, dot_C, dot_D, dot_O = DOT(P), DOT(A), DOT(B), DOT(C), DOT(D), DOT(O)
		polygon_ABCD = POLY(A, B, C, D, color=BLUE)

		label_scale_factor = .5
		label_P = MP('$P$', dot_P, RIGHT, label_scale_factor)
		label_A = MP('$A$', dot_A, A, label_scale_factor)
		label_B = MP('$B$', dot_B, B, label_scale_factor)
		label_C = MP('$C$', dot_C, C, label_scale_factor)
		label_D = MP('$D$', dot_D, D, label_scale_factor)
		label_O = MP('$O$', dot_O, LEFT, label_scale_factor)

		line_color = RED_A
		line_PA = LINE(P, A, line_color)
		line_PB = LINE(P, B, line_color)
		line_PC = LINE(P, C, line_color)
		line_PD = LINE(P, D, line_color)

		circle_PAB = CP(P, O, RED)

		color_alpha, color_beta = PURPLE_A, TEAL_A
		small_angle_length, large_angle_length = .4, .5
		small_angle_buff = .4
		angle_PAD = MA(P, A, D, large_angle_length, color=color_alpha)
		angle_PBA = MA(P, B, A, large_angle_length, color=color_alpha)
		angle_DPA = MA(D, P, A, large_angle_length, color=color_alpha)

		label_alpha = Tex(r'$\alpha$').set_color(color_alpha).scale(label_scale_factor).move_to(MA(P, A, D, large_angle_length+small_angle_buff))
		label_2alpha = Tex(r'$2\alpha$').set_color(color_alpha).scale(label_scale_factor).move_to(MA(P, B, A, large_angle_length+small_angle_buff))
		label_3alpha = Tex(r'$3\alpha$').set_color(color_alpha).scale(label_scale_factor).move_to(MA(D, P, A, large_angle_length+small_angle_buff))

		angle_CBP = MA(C, B, P, large_angle_length, color=color_beta)
		angle_BAP = MA(B, A, P, large_angle_length, color=color_beta)
		angle_BPC = MA(B, P, C, large_angle_length, color=color_beta)

		label_beta = Tex(r'$\beta$').set_color(color_beta).scale(label_scale_factor).move_to(MA(C, B, P, large_angle_length+small_angle_buff))
		label_2beta = Tex(r'$2\beta$').set_color(color_beta).scale(label_scale_factor).move_to(MA(B, A, P, large_angle_length+small_angle_buff))
		label_3beta = Tex(r'$3\beta$').set_color(color_beta).scale(label_scale_factor).move_to(MA(B, P, C, large_angle_length+.5))

		line_color_2 = YELLOW_A
		line_OA = LINE(O, A, line_color_2)
		line_OB = LINE(O, B, line_color_2)
		line_OP = LINE(O, P, line_color_2)

		angle_POA = MA(P, O, A, large_angle_length, color=color_alpha)
		label_4alpha = Tex(r'$4\alpha$').set_color(color_alpha).scale(label_scale_factor).move_to(MA(P, O, A, large_angle_length+.5))

		angle_BOP = MA(B, O, P, small_angle_length, color=color_beta)
		label_4beta = Tex(r'$4\beta$').set_color(color_beta).scale(label_scale_factor).move_to(MA(B, O, P, large_angle_length+.8))

		quadrilateral_ABCD = [
			polygon_ABCD,
			dot_A, dot_B, dot_C, dot_D,
			label_A, label_B, label_C, label_D,
		]
		VGroup(
			angle_PAD, angle_PBA, angle_DPA, angle_CBP, angle_BAP, angle_BPC, angle_POA, angle_BOP,
			polygon_ABCD,
			line_PA, line_PB, line_PC, line_PD, line_OA, line_OB, line_OP,
			circle_PAB,
			dot_A, dot_B, dot_C, dot_D, dot_P, dot_O,
			label_A, label_B, label_C, label_D, label_P, label_O,
			label_alpha, label_2alpha, label_3alpha, label_4alpha, label_beta, label_2beta, label_3beta, label_4beta
		).shift(1.2*DOWN)
		
		self.play(FadeIn(VGroup(*quadrilateral_ABCD), shift=UP))
		self.play(AnimationGroup(*[GrowFromCenter(i) for i in [dot_P, label_P]], lag_ratio=.8))
		self.add_foreground_mobjects(
			polygon_ABCD,
			dot_P, dot_A, dot_B, dot_C, dot_D,
			label_P, label_A, label_B, label_C, label_D
		)
		self.play(*[Create(line) for line in [line_PA, line_PB, line_PC, line_PD]], run_time=1.5)

		self.add_foreground_mobjects(
			polygon_ABCD,
			line_PA, line_PB, line_PC, line_PD,
			dot_P, dot_A, dot_B, dot_C, dot_D,
			label_P, label_A, label_B, label_C, label_D
		)
		self.play(Create(angle_PAD), Write(label_alpha))
		self.add_foreground_mobject(label_alpha)
		self.play(Create(angle_PBA), TransformFromCopy(label_alpha, label_2alpha))
		self.add_foreground_mobject(label_2alpha)
		self.play(Create(angle_DPA), TransformFromCopy(label_alpha, label_3alpha))
		self.add_foreground_mobject(label_3alpha)
		self.wait(.5)

		self.play(Create(angle_CBP), Write(label_beta))
		self.add_foreground_mobject(label_beta)
		self.play(Create(angle_BAP), TransformFromCopy(label_beta, label_2beta))
		self.add_foreground_mobject(label_2beta)
		self.play(Create(angle_BPC), TransformFromCopy(label_beta, label_3beta))
		self.add_foreground_mobject(label_3beta)

		quadrilateral_ABCD.extend([
			dot_P, label_P,
			line_PA, line_PB, line_PC, line_PD,
			angle_PAD, angle_PBA, angle_DPA,
			label_alpha, label_2alpha, label_3alpha,
			angle_CBP, angle_BAP, angle_BPC,
			label_beta, label_2beta, label_3beta
		])
		VGroup(
			angle_POA, angle_BOP,
			circle_PAB,
			line_OA, line_OB, line_OP,
			dot_O, label_O,
			label_4alpha, label_4beta
		).shift(3.1*LEFT)

		x_space = r'\qquad\qquad'
		t3 = MathTex(
			#      0    1           2    3    4    5                   6    7           8    9   10   11
			r'\alpha', '=', r'\angle ', 'P', 'A', 'D' + x_space, r'\beta', '=', r'\angle ', 'C', 'B', 'P'
		)
		for i in [0, *range(2, 6)]:
			t3[i].set_color(color_alpha)
			t3[i+6].set_color(color_beta)

		text_scale_factor = .5
		t3.scale(text_scale_factor).shift(.3*UP+3.5*RIGHT)

		self.play(VGroup(*quadrilateral_ABCD).animate.shift(3.1*LEFT))

		short_lag_ratio, short_run_time = .5, 5
		for idx, (i, args) in enumerate([
			(label_alpha, [label_P, label_A, label_D]),
			(label_beta, [label_C, label_B, label_P])
		]):
			j = 6*idx
			self.play(AnimationGroup(
				TransformFromCopy(i, t3[j]),
				Write(t3[j+1:j+3]),
				TransformFromCopy(VGroup(*args), t3[j+3:j+6]),
				lag_ratio=short_lag_ratio, run_time=short_run_time
			))
			self.wait()

		y_space = .3
		t4 = MathTex(
			#       0    1    2    3    4    5                            6    7    8    9   10   11
			r'\angle ', 'D', 'P', 'A', '=', r'3\alpha' + x_space, r'\angle ', 'B', 'P', 'C', '=', r'3\beta'
		)
		for i in [*range(4), 5]:
			t4[i].set_color(color_alpha)
			t4[i+6].set_color(color_beta)
		t4.scale(text_scale_factor).next_to(t3, DOWN, y_space)

		for idx, (i, args) in enumerate([
			(label_3alpha, [label_D, label_P, label_A]),
			(label_3beta, [label_B, label_P, label_C])
		]):
			j = 6*idx
			self.play(AnimationGroup(
				Write(t4[j]), TransformFromCopy(VGroup(*args), t4[j+1:j+4]),
				Write(t4[j+4]), TransformFromCopy(i, t4[j+5]),
				lag_ratio=short_lag_ratio, run_time=short_run_time
			))
			self.wait()

		t5 = MathTex(
			#       0    1    2    3    4    5                     6    7    8    9   10          11   12   13   14
			r'\angle ', 'A', 'D', 'P', '=', r'180^\circ-', r'\angle ', 'D', 'P', 'A', '-', r'\angle ', 'P', 'A', 'D'
		)
		t6 = MathTex(
			#       0    1    2    3    4    5                     6    7    8
			r'\angle ', 'A', 'D', 'P', '=', r'180^\circ-', r'3\alpha', '-', r'\alpha'
		)
		t7 = MathTex(
			#       0    1    2    3    4              5    6
			r'\angle ', 'A', 'D', 'P', '=', r'180^\circ-', r'4\alpha'
		)
		t8 = MathTex(
			#       0    1    2    3    4    5                     6    7    8    9   10          11   12   13   14
			r'\angle ', 'P', 'C', 'B', '=', r'180^\circ-', r'\angle ', 'B', 'P', 'C', '-', r'\angle ', 'C', 'B', 'P'
		)
		t9 = MathTex(
			#       0    1    2    3    4    5                    6    7    8
			r'\angle ', 'P', 'C', 'B', '=', r'180^\circ-', r'3\beta', '-', r'\beta'
		)
		t10 = MathTex(
			#       0    1    2    3    4              5    6
			r'\angle ', 'P', 'C', 'B', '=', r'180^\circ-', r'4\beta'
		)
		t11 = MathTex(
			#       0    1    2    3    4              5    6                            7    8    9   10   11             12   13
			r'\angle ', 'A', 'D', 'P', '=', r'180^\circ-', r'4\alpha' + x_space, r'\angle ', 'P', 'C', 'B', '=', r'180^\circ-', r'4\beta'
		)
		for i in [*range(4), *range(6, 10), *range(11, 15)]:
			t5[i].set_color(color_alpha)
			t8[i].set_color(color_beta)
		for i in [*range(4), 6, 8]:
			t6[i].set_color(color_alpha)
			t9[i].set_color(color_beta)
		for i in [*range(4), 6]:
			t7[i].set_color(color_alpha)
			t10[i].set_color(color_beta)
			t11[i].set_color(color_alpha)
			t11[i+7].set_color(color_beta)
		for text in [t5, t6, t7, t8, t9, t10]:
			text.scale(.7).next_to(t4, DOWN, 1.5)
		t11.scale(text_scale_factor).next_to(t4, DOWN, y_space)

		long_run_time = 7
		self.play(AnimationGroup(
			Write(t5[0]), TransformFromCopy(VGroup(label_A, label_D, label_P), t5[1:4]),
			Write(t5[4:7]), TransformFromCopy(VGroup(label_D, label_P, label_A), t5[7:10]),
			Write(t5[10:12]), TransformFromCopy(VGroup(label_P, label_A, label_D), t5[12:]),
			lag_ratio=short_lag_ratio, run_time=long_run_time
		))
		self.wait()

		self.play(*[ReplacementTransform(*args) for args in [
			(t5[:6], t6[:6]), (t5[6:10], t6[6]), (t5[10], t6[7]), (t5[11:], t6[8])
		]])
		self.play(*[ReplacementTransform(*args) for args in [(t6[:6], t7[:6]), (t6[6:], t7[6:])]])
		self.play(*[ReplacementTransform(*args) for args in [(t7[:6], t11[:6]), (t7[6], t11[6])]])
		self.wait()

		self.play(AnimationGroup(
			Write(t8[0]), TransformFromCopy(VGroup(label_P, label_C, label_B), t8[1:4]),
			Write(t8[4:7]), TransformFromCopy(VGroup(label_B, label_P, label_C), t8[7:10]),
			Write(t8[10:12]), TransformFromCopy(VGroup(label_C, label_B, label_P), t8[12:]),
			lag_ratio=short_lag_ratio, run_time=long_run_time
		))
		self.wait()

		self.play(*[ReplacementTransform(*args) for args in [
			(t8[:6], t9[:6]), (t8[6:10], t9[6]), (t8[10], t9[7]), (t8[11:], t9[8])
		]])
		self.play(*[ReplacementTransform(*args) for args in [(t9[:6], t10[:6]), (t9[6:], t10[6:])]])
		self.play(ReplacementTransform(t10, t11[7:]))
		self.wait()

		self.play(AnimationGroup(*[GrowFromCenter(i) for i in [dot_O, label_O]], lag_ratio=.8))
		self.play(*[Uncreate(item) for item in [
			angle_PAD, angle_DPA, angle_CBP, angle_BPC,
			label_alpha, label_3alpha, label_beta, label_3beta
		]])
		self.add_foreground_mobjects(
			polygon_ABCD,
			circle_PAB,
			angle_PBA, angle_BAP,
			line_PA, line_PB, line_PC, line_PD,
			dot_P, dot_A, dot_B, dot_C, dot_D, dot_O,
			label_P, label_A, label_B, label_C, label_D, label_O, label_2alpha, label_2beta
		)
		self.play(GrowFromCenter(circle_PAB))
		self.wait()

		self.add_foreground_mobjects(
			polygon_ABCD,
			circle_PAB,
			angle_PBA, angle_BAP,
			line_PA, line_PB, line_PC, line_PD, line_OA, line_OP,
			dot_P, dot_A, dot_B, dot_C, dot_D, dot_O,
			label_P, label_A, label_B, label_C, label_D, label_O, label_2alpha, label_2beta
		)
		self.play(Create(line_OP), Create(line_OA))

		self.add_foreground_mobjects(
			polygon_ABCD,
			circle_PAB,
			angle_PBA, angle_BAP, angle_POA,
			line_PA, line_PB, line_PC, line_PD, line_OA, line_OP,
			dot_P, dot_A, dot_B, dot_C, dot_D, dot_O,
			label_P, label_A, label_B, label_C, label_D, label_O, label_2alpha, label_2beta
		)
		self.play(Create(angle_POA), TransformFromCopy(label_2alpha, label_4alpha))
		self.add_foreground_mobject(label_4alpha)
		self.wait()

		t12 = MathTex(
			#       0    1    2    3    4    5                            6    7    8    9   10   11
			r'\angle ', 'P', 'O', 'A', '=', r'4\alpha' + x_space, r'\angle ', 'B', 'O', 'P', '=', r'4\beta'
		)
		for i in [*range(4), 5]:
			t12[i].set_color(color_alpha)
			t12[i+6].set_color(color_beta)
		t12.scale(text_scale_factor).next_to(t11, DOWN, y_space)
		self.play(AnimationGroup(
			Write(t12[0]), TransformFromCopy(VGroup(label_P, label_O, label_A), t12[1:4]),
			Write(t12[4]), TransformFromCopy(label_4alpha, t12[5]),
			lag_ratio=short_lag_ratio, run_time=short_run_time
		))
		self.play(*[Uncreate(i) for i in [angle_PBA, label_2alpha, angle_POA, label_4alpha]])
		self.wait()

		self.add_foreground_mobjects(
			polygon_ABCD,
			circle_PAB,
			angle_PBA,
			line_PA, line_PB, line_PC, line_PD, line_OA, line_OB, line_OP,
			dot_P, dot_A, dot_B, dot_C, dot_D, dot_O,
			label_P, label_A, label_B, label_C, label_D, label_O, label_2beta
		)
		self.play(Create(line_OB))
		self.play(Create(angle_BOP), TransformFromCopy(label_2beta, label_4beta))
		self.add_foreground_mobject(label_4alpha)
		self.wait()

		self.play(AnimationGroup(
			Write(t12[6]), TransformFromCopy(VGroup(label_B, label_O, label_P), t12[7:10]),
			Write(t12[10]), TransformFromCopy(label_4beta, t12[11]),
			lag_ratio=short_lag_ratio, run_time=short_run_time
		))
		self.play(
			*[Uncreate(i) for i in [angle_BAP, label_2beta, angle_BOP, label_4beta]],
			FadeOut(t3, t4),
			*[i.animate.move_to(j) for i, j in [(t11, t3), (t12, t4)]]
		)
		self.wait()

		large_y_space = .4
		t13 = MathTex(
			#       0    1    2    3    4           5    6    7    8    9   10
			r'\angle ', 'A', 'D', 'P', '+', r'\angle ', 'P', 'O', 'A', '=', r'180^\circ'
		)
		for i in [*range(4), *range(5, 9)]:
			t13[i].set_color(color_alpha)
		t13.scale(.7).next_to(t12, DOWN, large_y_space)
		self.play(AnimationGroup(
			TransformFromCopy(t11[:4], t13[:4]), Write(t13[4]),
			TransformFromCopy(t12[:4], t13[5:9]), Write(t13[9]),
			AnimationGroup(*[ReplacementTransform(i.copy(), t13[10]) for i in [t11[5:7], t12[5]]]),
			lag_ratio=short_lag_ratio, run_time=short_run_time
		))
		self.wait()

		t14 = MathTex(
			#         0    1    2    3    4    5
			r'\implies ', 'A', 'D', 'P', 'O', r"\text{ es c\'iclico}",
			tex_template=TexTemplateLibrary.simple
		)
		for i in range(4):
			t14[i+1].set_color(color_alpha)
		t14.scale(.7).next_to(t13, DOWN, large_y_space)
		self.play(AnimationGroup(
			Write(t14[0]),
			TransformFromCopy(VGroup(label_A, label_D, label_P, label_O), t14[1:5]),
			Write(t14[5]),
			lag_ratio=short_lag_ratio, run_time=3
		))
		self.wait()
		self.play(FadeOut(t13, t14[0]))
		self.play(t14[1:].animate.next_to(t12, DOWN, large_y_space))

		t15 = MathTex(
			#0    1    2    3    4
			'O', 'A', '=', 'O', 'P'
		)
		for i in [0, 1, 3, 4]:
			t15[i].set_color(color_alpha)
		t15.scale(.7).next_to(t14[1:], DOWN, large_y_space)
		self.play(AnimationGroup(
			TransformFromCopy(VGroup(label_O, label_A), t15[:2]),
			Write(t15[2]),
			TransformFromCopy(VGroup(label_O, label_P), t15[3:]),
			lag_ratio=short_lag_ratio, run_time=short_run_time
		))
		self.wait()

		t16 = MathTex(
			#         0    1    2                                                                 3    4    5    6
			r'\implies ', 'O', r"\text{ pertenece a la bisectriz interna del \'angulo }", r'\angle ', 'A', 'D', 'P',
			tex_template=TexTemplateLibrary.simple
		)
		for i in [0, *range(2, 6)]:
			t16[i+1].set_color(color_alpha)
		t16.scale(.5).next_to(t15, DOWN, large_y_space)
		self.play(AnimationGroup(
			Write(t16[0]), TransformFromCopy(label_O, t16[1]),
			Write(t16[2:4]), TransformFromCopy(VGroup(label_A, label_D, label_P), t16[4:]),
			lag_ratio=short_lag_ratio, run_time=short_run_time
		))
		self.wait()
		self.play(FadeOut(t14[1:], t15, t16[0]), t16[1:].animate.next_to(t12, DOWN, y_space))
		t17 = MathTex(
			#       0    1    2    3    4           5    6    7    8    9   10
			r'\angle ', 'P', 'C', 'B', '+', r'\angle ', 'B', 'O', 'P', '=', r'180^\circ'
		)
		for i in [*range(4), *range(5, 9)]:
			t17[i].set_color(color_beta)
		t17.scale(.7).next_to(t16[1:], DOWN, large_y_space)
		self.play(AnimationGroup(
			TransformFromCopy(t11[7:11], t17[:4]), Write(t17[4]),
			TransformFromCopy(t12[6:10], t17[5:9]), Write(t17[9]),
			AnimationGroup(*[ReplacementTransform(i.copy(), t17[10]) for i in [t11[12:], t12[11]]]),
			lag_ratio=short_lag_ratio, run_time=short_run_time
		))
		self.wait()

		t18 = MathTex(
			#         0    1    2    3    4    5
			r'\implies ', 'P', 'C', 'B', 'O', r"\text{ es c\'iclico}",
			tex_template=TexTemplateLibrary.simple
		)
		for i in range(4):
			t18[i+1].set_color(color_beta)
		t18.scale(.7).next_to(t17, DOWN, large_y_space)
		self.play(AnimationGroup(
			Write(t18[0]),
			TransformFromCopy(VGroup(label_P, label_C, label_B, label_O), t18[1:5]),
			Write(t18[5]),
			lag_ratio=short_lag_ratio, run_time=3
		))
		self.wait()
		self.play(FadeOut(t17, t18[0]))
		self.play(t18[1:].animate.next_to(t16[1:], DOWN, large_y_space))

		t19 = MathTex(
			#0    1    2    3    4
			"O", "B", "=", "O", "P"
		)
		for i in [0, 1, 3, 4]:
			t19[i].set_color(color_beta)
		t19.scale(.7).next_to(t18[1:], DOWN, large_y_space)
		self.play(AnimationGroup(
			TransformFromCopy(VGroup(label_O, label_B), t19[:2]),
			Write(t19[2]),
			TransformFromCopy(VGroup(label_O, label_P), t19[3:]),
			lag_ratio=short_lag_ratio, run_time=short_run_time
		))
		self.wait()

		t20 = MathTex(
			#         0    1    2                                                                 3    4    5    6
			r'\implies ', 'O', r"\text{ pertenece a la bisectriz interna del \'angulo }", r'\angle ', 'P', 'C', 'B',
			tex_template=TexTemplateLibrary.simple
		)
		for i in [0, *range(2, 6)]:
			t20[i+1].set_color(color_beta)
		t20.scale(.5).next_to(t19, DOWN, large_y_space)
		self.play(AnimationGroup(
			Write(t20[0]), TransformFromCopy(label_O, t20[1]),
			Write(t20[2:4]), TransformFromCopy(VGroup(label_P, label_C, label_B), t20[4:]),
			lag_ratio=short_lag_ratio, run_time=short_run_time
		))
		self.wait()
		self.play(
			FadeOut(*[t11, t12, t18[1:], t19, t20[0]]),
			*[i[1:].animate.move_to(j) for i, j in [(t16, t3), (t20, t4)]]
		)
		self.wait()

		t21 = MathTex(
			#0    1    2    3    4
			'O', 'A', '=', 'O', 'B'
		)
		for i in range(2):
			t21[i].set_color(color_alpha)
			t21[i+3].set_color(color_beta)
		t21.scale(.7).next_to(t20[1:], DOWN, large_y_space)
		self.play(AnimationGroup(
			TransformFromCopy(VGroup(label_O, label_A), t21[:2]),
			Write(t21[2]),
			TransformFromCopy(VGroup(label_O, label_B), t21[3:]),
			lag_ratio=short_lag_ratio, run_time=short_run_time
		))
		t22 = MathTex(
			#         0    1    2                                                  3    4
			r'\implies ', 'O', r'\text{ pertenece a la mediatriz del segmento }', 'A', 'B',
			tex_template=TexTemplateLibrary.simple
		)
		for i in [1, 3, 4]:
			t22[i].set_color(YELLOW_A)
		t22.scale(.5).next_to(t21, DOWN, large_y_space)
		self.play(AnimationGroup(
			Write(t22[0]), TransformFromCopy(label_O, t22[1]),
			Write(t22[2]), TransformFromCopy(VGroup(label_A, label_B), t22[3:]),
			lag_ratio=short_lag_ratio, run_time=short_run_time
		))
		self.wait()
		self.play(
			*[FadeOut(item) for item in [line_OA, line_OB, line_OP, t21, t22[0]]],
			t22[1:].animate.next_to(t20[1:], DOWN, y_space, LEFT)
		)
		self.wait()

		t23 = Tex(
			#                                  0    1
			r"La bisectriz interna del \'angulo ", r'$\angle ADP$',
			#                                      2    3
			r",\\ la bisectriz interna del \'angulo ", r'$\angle PCB$',
			#                               4    5
			r'\\ y la mediatriz del segmento ', '$AB$',
			#                                                6      7      8
			r"\\ concurren en el circuncentro del tri\'angulo ", '$PAB$', '.',
			tex_template=TEX_TEMPLATE('250pt', '1.2')
		)
		for i, color in enumerate([color_alpha, color_beta, YELLOW_A, RED_A]):
			t23[2*i+1].set_color(color)
		t23.scale(.5).next_to(t3, DOWN, 1.5)
		self.play(AnimationGroup(
			VGroup(t16[1:], t20[1:], t22[1:]).animate.shift(.5*UP),
			*[Write(t23[i]) for i in range(9)],
			lag_ratio=1, run_time=8
		))
		self.wait()

		for i in range(2):
			self.play(Circumscribe(t23))
		self.wait()

		self.play(*[FadeOut(item, shift=DOWN) for item in self.mobjects])

		ending_credit = Tex('Video hecho con ', r'\textsc{Manim}')
		ending_credit.scale(1.5)
		ending_credit[1].set_color_by_gradient(GOLD, GOLD_A)
		for i in range(2):
			self.play(Write(ending_credit[i]))
		self.wait()
		self.play(FadeOut(ending_credit, shift=DOWN))
		self.wait()
