import os, sys
filepath = os.path.realpath(__file__)
sys.path.append(os.path.dirname(os.path.dirname(filepath)))

from asymptote import *

class Video(Scene):
    def construct(self):
        self.add_sound("imo_2020_p1/audio.mp3")
        logo = ImageMobject('imo_2020_p1/imo_2020_logo.png')

        self.play(FadeInFrom(logo, DOWN))

        t1 = Tex(r"\textsf{Problema 1}").set_color_by_gradient("#3c94d4", BLUE_B)
        t1.scale(2.5).shift(.3*UP+3.6*RIGHT)

        self.play(AnimationGroup(
            logo.animate.shift(3.1*LEFT),
            Write(t1),
            lag_ratio=.8
        ))
        self.wait(.5)

        t2 = Tex(
            r"\textbf{Problema 1.} \ \ ",
            r"Considere el cuadril\'atero convexo $ABCD$. El punto $P$ est\'a en el interior de $ABCD$. Asuma las siguientes igualdades de razones: $$\angle PAD:\angle PBA:\angle DPA=1:2:3=\angle CBP:\angle BAP:\angle BPC.$$ Demuestre que las siguientes tres rectas concurren en un punto: la bisectriz interna del \'angulo $\angle ADP$, la bisectriz interna del \'angulo $\angle PCB$ y la mediatriz del segmento $AB$.",
            tex_environment=None,
            tex_template=TEX_TEMPLATE('512.34pt')
        )
        t2[0].set_color_by_gradient(GOLD, GOLD_A)
        t2.scale(.5).to_corner(UP)

        self.play(AnimationGroup(
            FadeOut(logo),
            ReplacementTransform(t1, t2[0]),
            run_time=2,
            lag_ratio=.5
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
        label_P = MP("$P$", dot_P, RIGHT, label_scale_factor)
        label_A = MP("$A$", dot_A, A, label_scale_factor)
        label_B = MP("$B$", dot_B, B, label_scale_factor)
        label_C = MP("$C$", dot_C, C, label_scale_factor)
        label_D = MP("$D$", dot_D, D, label_scale_factor)
        label_O = MP("$O$", dot_O, LEFT, label_scale_factor)
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
        label_alpha = Tex(r"$\alpha$").set_color(color_alpha).scale(label_scale_factor).move_to(MA(P, A, D, large_angle_length+small_angle_buff))
        label_2alpha = Tex(r"$2\alpha$").set_color(color_alpha).scale(label_scale_factor).move_to(MA(P, B, A, large_angle_length+small_angle_buff))
        label_3alpha = Tex(r"$3\alpha$").set_color(color_alpha).scale(label_scale_factor).move_to(MA(D, P, A, large_angle_length+small_angle_buff))
        angle_CBP = MA(C, B, P, large_angle_length, color=color_beta)
        angle_BAP = MA(B, A, P, large_angle_length, color=color_beta)
        angle_BPC = MA(B, P, C, large_angle_length, color=color_beta)
        label_beta = Tex(r"$\beta$").set_color(color_beta).scale(label_scale_factor).move_to(MA(C, B, P, large_angle_length+small_angle_buff))
        label_2beta = Tex(r"$2\beta$").set_color(color_beta).scale(label_scale_factor).move_to(MA(B, A, P, large_angle_length+small_angle_buff))
        label_3beta = Tex(r"$3\beta$").set_color(color_beta).scale(label_scale_factor).move_to(MA(B, P, C, large_angle_length+.5))
        line_color_2 = YELLOW_A
        line_OA = LINE(O, A, line_color_2)
        line_OB = LINE(O, B, line_color_2)
        line_OP = LINE(O, P, line_color_2)
        angle_POA = MA(P, O, A, large_angle_length, color=color_alpha)
        label_4alpha = Tex(r"$4\alpha$").set_color(color_alpha).scale(label_scale_factor).move_to(MA(P, O, A, large_angle_length+.5))
        angle_BOP = MA(B, O, P, small_angle_length, color=color_beta)
        label_4beta = Tex(r"$4\beta$").set_color(color_beta).scale(label_scale_factor).move_to(MA(B, O, P, large_angle_length+.8))
        quadrilateral_ABCD = [
            polygon_ABCD,
            dot_A, dot_B, dot_C, dot_D,
            label_A, label_B, label_C, label_D,
        ]
        VGroup(
            angle_PAD, angle_PBA, angle_DPA,
            angle_CBP, angle_BAP, angle_BPC,
            angle_POA, angle_BOP,
            polygon_ABCD,
            line_PA, line_PB, line_PC, line_PD,
            line_OA, line_OB, line_OP,
            circle_PAB,
            dot_A, dot_B, dot_C, dot_D,
            dot_P, dot_O,
            label_A, label_B, label_C, label_D,
            label_P, label_O,
            label_alpha, label_2alpha, label_3alpha, label_4alpha,
            label_beta, label_2beta, label_3beta, label_4beta
        ).shift(1.2*DOWN)
        
        self.play(FadeInFrom(VGroup(*quadrilateral_ABCD), DOWN))
        self.play(AnimationGroup(
            GrowFromCenter(dot_P),
            GrowFromCenter(label_P),
            lag_ratio=.8
        ))
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
        self.play(
            Create(angle_PAD),
            Write(label_alpha)
        )
        self.add_foreground_mobject(label_alpha)

        self.play(
            Create(angle_PBA),
            *TC(label_alpha, label_2alpha)
        )
        self.add_foreground_mobject(label_2alpha)

        self.play(
            Create(angle_DPA),
            *TC(label_alpha, label_3alpha)
        )
        self.add_foreground_mobject(label_3alpha)

        self.wait(.5)
        self.play(
            Create(angle_CBP),
            Write(label_beta)
        )
        self.add_foreground_mobject(label_beta)

        self.play(
            Create(angle_BAP),
            *TC(label_beta, label_2beta)
        )
        self.add_foreground_mobject(label_2beta)

        self.play(
            Create(angle_BPC),
            *TC(label_beta, label_3beta)
        )
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
        x_space = r"\qquad\qquad"
        text_scale_factor = .5
        t3 = MathTex(
            r"\alpha", #0
            "=", #1
            r"\angle ", #2
            "P", #3
            "A", #4
            "D" + x_space, #5
            r"\beta", #6
            "=", #7
            r"\angle ", #8
            "C", #9
            "B", #10
            "P" #11
        )
        for i in [0, *range(2, 6)]:
            t3[i].set_color(color_alpha)
        for i in [6, *range(8, 12)]:
            t3[i].set_color(color_beta)
        t3.scale(text_scale_factor).shift(.3*UP+3.5*RIGHT)

        self.play(VGroup(*quadrilateral_ABCD).animate.shift(3.1*LEFT))

        short_lag_ratio, short_run_time = .5, 5

        self.play(AnimationGroup(
            *TC(label_alpha, t3[0]),
            Write(t3[1:3]),
            *TC(VGroup(label_P, label_A, label_D), t3[3:6]),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time
        ))
        self.wait()
        self.play(AnimationGroup(
            *TC(label_beta, t3[6]),
            Write(t3[7:9]),
            *TC(VGroup(label_C, label_B, label_P), t3[9:]),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time
        ))
        self.wait()

        y_space = .3
        t4 = MathTex(
            r"\angle ", #0
            "D", #1
            "P", #2
            "A", #3
            "=", #4
            r"3\alpha" + x_space, #5
            r"\angle ", #6
            "B", #7
            "P", #8
            "C", #9
            "=", #10
            r"3\beta" #11
        )
        for i in [*range(0, 4), 5]:
            t4[i].set_color(color_alpha)
        for i in [*range(6, 10), 11]:
            t4[i].set_color(color_beta)
        t4.scale(text_scale_factor).next_to(t3, DOWN, y_space)

        self.play(AnimationGroup(
            Write(t4[0]),
            *TC(VGroup(label_D, label_P, label_A), t4[1:4]),
            Write(t4[4]),
            *TC(label_3alpha, t4[5]),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time
        ))
        self.wait()
        self.play(AnimationGroup(
            Write(t4[6]),
            *TC(VGroup(label_B, label_P, label_C), t4[7:10]),
            Write(t4[10]),
            *TC(label_3beta, t4[11]),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time
        ))
        self.wait()

        t5 = MathTex(
            r"\angle ", #0
            "A", #1
            "D", #2
            "P", #3
            "=", #4
            r"180^\circ-", #5
            r"\angle ", #6
            "D", #7
            "P", #8
            "A", #9
            "-", #10
            r"\angle ", #11
            "P", #12
            "A", #13
            "D" #14
        )
        for i in [*range(0, 4), *range(6, 10), *range(11, 15)]:
            t5[i].set_color(color_alpha)
        t6 = MathTex(
            r"\angle ", #0
            "A", #1
            "D", #2
            "P", #3
            "=", #4
            r"180^\circ-", #5
            r"3\alpha", #6
            "-", #7
            r"\alpha" #8
        )
        for i in [*range(0, 4), 6, 8]:
            t6[i].set_color(color_alpha)
        t7 = MathTex(
            r"\angle ", #0
            "A", #1
            "D", #2
            "P", #3
            "=", #4
            r"180^\circ-", #5
            r"4\alpha" #6
        )
        for i in [*range(0, 4), 6]:
            t7[i].set_color(color_alpha)
        t8 = MathTex(
            r"\angle ", #0
            "P", #1
            "C", #2
            "B", #3
            "=", #4
            r"180^\circ-", #5
            r"\angle ", #6
            "B", #7
            "P", #8
            "C", #9
            "-", #10
            r"\angle ", #11
            "C", #12
            "B", #13
            "P" #14
        )
        for i in [*range(0, 4), *range(6, 10), *range(11, 15)]:
            t8[i].set_color(color_beta)
        t9 = MathTex(
            r"\angle ", #0
            "P", #1
            "C", #2
            "B", #3
            "=", #4
            r"180^\circ-", #5
            r"3\beta", #6
            "-", #7
            r"\beta" #8
        )
        for i in [*range(0, 4), 6, 8]:
            t9[i].set_color(color_beta)
        t10 = MathTex(
            r"\angle ", #0
            "P", #1
            "C", #2
            "B", #3
            "=", #4
            r"180^\circ-", #5
            r"4\beta" #6
        )
        for i in [*range(0, 4), 6]:
            t10[i].set_color(color_beta)
        t11 = MathTex(
            r"\angle ", #0
            "A", #1
            "D", #2
            "P", #3
            "=", #4
            r"180^\circ-", #5
            r"4\alpha" + x_space, #6
            r"\angle ", #7
            "P", #8
            "C", #9
            "B", #10
            "=", #11
            r"180^\circ-", #12
            r"4\beta" #13
        )
        for i in [*range(0, 4), 6]:
            t11[i].set_color(color_alpha)
        for i in [*range(7, 11), 13]:
            t11[i].set_color(color_beta)
        for text in [t5, t6, t7, t8, t9, t10]:
            text.scale(.7).next_to(t4, DOWN, 1.5)
        t11.scale(text_scale_factor).next_to(t4, DOWN, y_space)
        long_run_time = 7

        self.play(AnimationGroup(
            Write(t5[0]),
            *TC(VGroup(label_A, label_D, label_P), t5[1:4]),
            Write(t5[4:7]),
            *TC(VGroup(label_D, label_P, label_A), t5[7:10]),
            Write(t5[10:12]),
            *TC(VGroup(label_P, label_A, label_D), t5[12:]),
            lag_ratio=short_lag_ratio,
            run_time=long_run_time
        ))
        self.wait()
        self.play(
            ReplacementTransform(t5[:6], t6[:6]),
            ReplacementTransform(t5[6:10], t6[6]),
            ReplacementTransform(t5[10], t6[7]),
            ReplacementTransform(t5[11:], t6[8])
        )
        self.play(
            ReplacementTransform(t6[:6], t7[:6]),
            ReplacementTransform(t6[6:], t7[6:])
        )
        self.play(
            ReplacementTransform(t7[:6], t11[:6]),
            ReplacementTransform(t7[6], t11[6])
        )
        self.wait()
        self.play(AnimationGroup(
            Write(t8[0]),
            *TC(VGroup(label_P, label_C, label_B), t8[1:4]),
            Write(t8[4:7]),
            *TC(VGroup(label_B, label_P, label_C), t8[7:10]),
            Write(t8[10:12]),
            *TC(VGroup(label_C, label_B, label_P), t8[12:]),
            lag_ratio=short_lag_ratio,
            run_time=long_run_time
        ))
        self.wait()
        self.play(
            ReplacementTransform(t8[:6], t9[:6]),
            ReplacementTransform(t8[6:10], t9[6]),
            ReplacementTransform(t8[10], t9[7]),
            ReplacementTransform(t8[11:], t9[8])
        )
        self.play(
            ReplacementTransform(t9[:6], t10[:6]),
            ReplacementTransform(t9[6:], t10[6:])
        )
        self.play(ReplacementTransform(t10, t11[7:]))
        self.wait()
        self.play(AnimationGroup(
            GrowFromCenter(dot_O),
            GrowFromCenter(label_O),
            lag_ratio=.8
        ))
        self.play(*[Uncreate(item) for item in [
            angle_PAD,
            angle_DPA,
            angle_CBP,
            angle_BPC,
            label_alpha,
            label_3alpha,
            label_beta,
            label_3beta
        ]])
        self.add_foreground_mobjects(
            polygon_ABCD,
            circle_PAB,
            angle_PBA, angle_BAP,
            line_PA, line_PB, line_PC, line_PD,
            dot_P, dot_A, dot_B, dot_C, dot_D, dot_O,
            label_P, label_A, label_B, label_C, label_D, label_O,
            label_2alpha, label_2beta,
        )
        self.play(GrowFromCenter(circle_PAB))
        self.wait()

        self.add_foreground_mobjects(
            polygon_ABCD,
            circle_PAB,
            angle_PBA, angle_BAP,
            line_PA, line_PB, line_PC, line_PD,
            line_OA, line_OP,
            dot_P, dot_A, dot_B, dot_C, dot_D, dot_O,
            label_P, label_A, label_B, label_C, label_D, label_O,
            label_2alpha, label_2beta
        )
        self.play(
            Create(line_OP),
            Create(line_OA)
        )
        self.add_foreground_mobjects(
            polygon_ABCD,
            circle_PAB,
            angle_PBA, angle_BAP,
            angle_POA,
            line_PA, line_PB, line_PC, line_PD,
            line_OA, line_OP,
            dot_P, dot_A, dot_B, dot_C, dot_D, dot_O,
            label_P, label_A, label_B, label_C, label_D, label_O,
            label_2alpha, label_2beta
        )
        self.play(
            Create(angle_POA),
            *TC(label_2alpha, label_4alpha)
        )
        self.add_foreground_mobject(label_4alpha)
        
        self.wait()

        t12 = MathTex(
            r"\angle ", #0
            "P", #1
            "O", #2
            "A", #3
            "=", #4
            r"4\alpha" + x_space, #5
            r"\angle ", #6
            "B", #7
            "O", #8
            "P", #9
            "=", #10
            r"4\beta" #11
        )
        for i in [*range(0, 4), 5]:
            t12[i].set_color(color_alpha)
        for i in [*range(6, 10), 11]:
            t12[i].set_color(color_beta)
        t12.scale(text_scale_factor).next_to(t11, DOWN, y_space)

        self.play(AnimationGroup(
            Write(t12[0]),
            *TC(VGroup(label_P, label_O, label_A), t12[1:4]),
            Write(t12[4]),
            *TC(label_4alpha, t12[5]),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time
        ))
        self.play(
            Uncreate(angle_PBA),
            Uncreate(label_2alpha),
            Uncreate(angle_POA),
            Uncreate(label_4alpha)
        )
        self.wait()
        self.add_foreground_mobjects(
            polygon_ABCD,
            circle_PAB,
            angle_PBA,
            line_PA, line_PB, line_PC, line_PD,
            line_OA, line_OB, line_OP,
            dot_P, dot_A, dot_B, dot_C, dot_D, dot_O,
            label_P, label_A, label_B, label_C, label_D, label_O,
            label_2beta
        )
        self.play(Create(line_OB))
        self.play(
            Create(angle_BOP),
            *TC(label_2beta, label_4beta)
        )
        self.add_foreground_mobject(label_4alpha)

        self.wait()
        self.play(AnimationGroup(
            Write(t12[6]),
            *TC(VGroup(label_B, label_O, label_P), t12[7:10]),
            Write(t12[10]),
            *TC(label_4beta, t12[11]),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time
        ))
        self.play(
            Uncreate(angle_BAP),
            Uncreate(label_2beta),
            Uncreate(angle_BOP),
            Uncreate(label_4beta),
            FadeOut(t3),
            FadeOut(t4),
            t11.animate.move_to(t3),
            t12.animate.move_to(t4)
        )
        self.wait()

        large_y_space = .4
        t13 = MathTex(
            r"\angle ", #0
            "A", #1
            "D", #2
            "P", #3
            "+", #4
            r"\angle ", #5
            "P", #6
            "O", #7
            "A", #8
            "=", #9
            r"180^\circ" #10
        )
        for i in [*range(0, 4), *range(5, 9)]:
            t13[i].set_color(color_alpha)
        t13.scale(.7).next_to(t12, DOWN, large_y_space)

        self.play(AnimationGroup(
            *TC(t11[:4], t13[:4]),
            Write(t13[4]),
            *TC(t12[:4], t13[5:9]),
            Write(t13[9]),
            AnimationGroup(
                *TC(t11[5:7], t13[10]),
                *TC(t12[5], t13[10])
            ),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time,
        ))
        self.wait()

        t14 = MathTex(
            r"\implies ", #0
            "A", #1
            "D", #2
            "P", #3
            "O", #4
            r"\text{ es cíclico}", #5
            tex_template=TexTemplateLibrary.simple
        )
        for i in range(1, 5):
            t14[i].set_color(color_alpha)
        t14.scale(.7).next_to(t13, DOWN, large_y_space)

        self.play(AnimationGroup(
            Write(t14[0]),
            *TC(VGroup(label_A, label_D, label_P, label_O), t14[1:5]),
            Write(t14[5]),
            lag_ratio=short_lag_ratio,
            run_time=3
        ))
        self.wait()
        self.play(FadeOut(t13), FadeOut(t14[0]))
        self.play(t14[1:].animate.next_to(t12, DOWN, large_y_space))

        t15 = MathTex(
            "O", #0
            "A", #1
            "=", #2
            "O", #3
            "P" #4
        )
        for i in [0, 1, 3, 4]:
            t15[i].set_color(color_alpha)
        t15.scale(.7).next_to(t14[1:], DOWN, large_y_space)

        self.play(AnimationGroup(
            *TC(VGroup(label_O, label_A), t15[:2]),
            Write(t15[2]),
            *TC(VGroup(label_O, label_P), t15[3:]),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time
        ))
        self.wait()

        t16 = MathTex(
            r"\implies ", #0
            "O", #1
            r"\text{ pertenece a la bisectriz interna del ángulo }", #2
            r"\angle ", #3
            "A", #4
            "D", #5
            "P", #6
            tex_template=TexTemplateLibrary.simple
        )
        for i in [1, *range(3, 7)]:
            t16[i].set_color(color_alpha)
        t16.scale(.5).next_to(t15, DOWN, large_y_space)

        self.play(AnimationGroup(
            Write(t16[0]),
            *TC(label_O, t16[1]),
            Write(t16[2:4]),
            *TC(VGroup(label_A, label_D, label_P), t16[4:]),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time
        ))
        self.wait()
        self.play(
            FadeOut(t14[1:]),
            FadeOut(t15),
            FadeOut(t16[0]),
            t16[1:].animate.next_to(t12, DOWN, y_space)
        )
        t17 = MathTex(
            r"\angle ", #0
            "P", #1
            "C", #2
            "B", #3
            "+", #4
            r"\angle ", #5
            "B", #6
            "O", #7
            "P", #8
            "=", #9
            r"180^\circ" #10
        )
        for i in [*range(0, 4), *range(5, 9)]:
            t17[i].set_color(color_beta)
        t17.scale(.7).next_to(t16[1:], DOWN, large_y_space)

        self.play(AnimationGroup(
            *TC(t11[7:11], t17[:4]),
            Write(t17[4]),
            *TC(t12[6:10], t17[5:9]),
            Write(t17[9]),
            AnimationGroup(
                *TC(t11[12:], t17[10]),
                *TC(t12[11], t17[10])
            ),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time
        ))
        self.wait()

        t18 = MathTex(
            r"\implies ", #0
            "P", #1
            "C", #2
            "B", #3
            "O", #4
            r"\text{ es cíclico}", #5
            tex_template=TexTemplateLibrary.simple
        )
        for i in range(1, 5):
            t18[i].set_color(color_beta)
        t18.scale(.7).next_to(t17, DOWN, large_y_space)

        self.play(AnimationGroup(
            Write(t18[0]),
            *TC(VGroup(label_P, label_C, label_B, label_O), t18[1:5]),
            Write(t18[5]),
            lag_ratio=short_lag_ratio,
            run_time=3
        ))
        self.wait()
        self.play(FadeOut(t17), FadeOut(t18[0]))
        self.play(t18[1:].animate.next_to(t16[1:], DOWN, large_y_space))

        t19 = MathTex(
            "O", #0
            "B", #1
            "=", #2
            "O", #3
            "P" #4
        )
        for i in [0, 1, 3, 4]:
            t19[i].set_color(color_beta)
        t19.scale(.7).next_to(t18[1:], DOWN, large_y_space)

        self.play(AnimationGroup(
            *TC(VGroup(label_O, label_B), t19[:2]),
            Write(t19[2]),
            *TC(VGroup(label_O, label_P), t19[3:]),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time
        ))
        self.wait()

        t20 = MathTex(
            r"\implies ", #0
            "O", #1
            r"\text{ pertenece a la bisectriz interna del ángulo }", #2
            r"\angle ", #3
            "P", #4
            "C", #5
            "B", #6
            tex_template=TexTemplateLibrary.simple
        )
        for i in [1, *range(3, 7)]:
            t20[i].set_color(color_beta)
        t20.scale(.5).next_to(t19, DOWN, large_y_space)

        self.play(AnimationGroup(
            Write(t20[0]),
            *TC(label_O, t20[1]),
            Write(t20[2:4]),
            *TC(VGroup(label_P, label_C, label_B), t20[4:]),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time
        ))
        self.wait()
        self.play(
            *[FadeOut(item) for item in [t11, t12, t18[1:], t19, t20[0]]],
            t16[1:].animate.move_to(t3),
            t20[1:].animate.move_to(t4)
        )
        self.wait()
        t21 = MathTex(
            "O", #0
            "A", #1
            "=", #2
            "O", #3
            "B" #4
        )
        for i in [0, 1]:
            t21[i].set_color(color_alpha)
        for i in [3, 4]:
            t21[i].set_color(color_beta)
        t21.scale(.7).next_to(t20[1:], DOWN, large_y_space)

        self.play(AnimationGroup(
            *TC(VGroup(label_O, label_A), t21[:2]),
            Write(t21[2]),
            *TC(VGroup(label_O, label_B), t21[3:]),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time
        ))
        t22 = MathTex(
            r"\implies ", #0
            "O", #1
            r"\text{ pertenece a la mediatriz del segmento }", #2
            "A", #3
            "B", #4
            tex_template=TexTemplateLibrary.simple
        )
        for i in [1, 3, 4]:
            t22[i].set_color(YELLOW_A)
        t22.scale(.5).next_to(t21, DOWN, large_y_space)

        self.play(AnimationGroup(
            Write(t22[0]),
            *TC(label_O, t22[1]),
            Write(t22[2]),
            *TC(VGroup(label_A, label_B), t22[3:]),
            lag_ratio=short_lag_ratio,
            run_time=short_run_time
        ))
        self.wait()
        self.play(
            *[FadeOut(item) for item in [line_OA, line_OB, line_OP, t21, t22[0]]],
            t22[1:].animate.next_to(t20[1:], DOWN, y_space, LEFT)
        )
        self.wait()

        t23 = Tex(
            "La bisectriz interna del ángulo ", #0
            r"$\angle ADP$", #1
            r",\\ la bisectriz interna del ángulo ", #2
            r"$\angle PCB$", #3
            r"\\ y la mediatriz del segmento ", #4
            "$AB$", #5
            r"\\ concurren en el circuncentro del triángulo ", #6
            r"$PAB$", #7
            ".", #8
            tex_template=TEX_TEMPLATE('250pt', '1.2')
        )
        t23[1].set_color(color_alpha)
        t23[3].set_color(color_beta)
        t23[5].set_color(YELLOW_A)
        t23[7].set_color(RED_A)
        t23.scale(.5).next_to(t3, DOWN, 1.5)

        self.play(AnimationGroup(
            VGroup(t16[1:], t20[1:], t22[1:]).animate.shift(.5*UP),
            *[Write(t23[i]) for i in range(0, 9)],
            lag_ratio=1,
            run_time=8
        ))
        self.wait()
        self.play(ShowCreationThenDestructionAround(t23))
        self.play(ShowCreationThenDestructionAround(t23))
        self.wait()
        self.play(*[FadeOutAndShift(item, DOWN) for item in self.mobjects])
        ending_credit = Tex(
            "Video hecho con ",
            r"\textsc{Manim}"
        )
        ending_credit.scale(1.5)
        ending_credit[1].set_color_by_gradient(GOLD, GOLD_A)

        self.play(Write(ending_credit[0]))
        self.play(Write(ending_credit[1]))
        self.wait()
        self.play(FadeOutAndShift(ending_credit, DOWN))
        self.wait()

if __name__ == '__main__':
    RUN(filepath, 'Video', '-pqk -o imo_2020_problema_1_yohan_min')