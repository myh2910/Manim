from asymptote import *

class Video(Scene):
    def construct(self):
        ## INICIAL SETTINGS
        ## Colors
        text_color, dot_color = WHITE, ORANGE

        ## Texts
        title_1 = Tex("IMO 2015, ", "Problema 4")
        title_1.set_color_by_tex_to_color_map({
            "IMO 2015, " : BLUE,
            "Problema 4" : RED
        })
        title_1.scale(1.6)

        linebreak = r" \\ \hphantom{} \\ "

        title_2 = Tex(
            "\\textbf{Problema 4.} ",
            "El tri\\'angulo $ABC$ tiene circunferencia circunscrita $\\Omega$ y circuncentro $O$. Una circunferencia $\\Gamma$ de centro $A$ corta al segmento $BC$ en los puntos $D$ y $E$ tales que $B$, $D$, $E$ y $C$ son todos diferentes y est\\'an en la recta $BC$ en este orden. Sean $F$ y $G$ los puntos de intersecci\\'on de $\\Gamma$ y $\\Omega$, tales que $A$, $F$, $B$, $C$ y $G$ est\\'an sobre $\\Omega$ en este orden. Sea $K$ el segundo punto de intersecci\\'on de la circunferencia circunscrita al tri\\'angulo $BDF$ y el segmento $AB$. Sea $L$ el segundo punto de intersecci\\'on de la circunferencia circunscrita al tri\\'angulo $CGE$ y el segmento $CA$." + linebreak + "Supongamos que las rectas $FK$ y $GL$ son distintas y se cortan en el punto $X$. Demostrar que $X$ est\\'a en la recta $AO$.",
            tex_environment=None,
            tex_template=TexTemplateLibrary.simple
        )
        title_2.set_color_by_tex("Problema", RED)
        title_2.scale(0.7).to_corner(UP)
        
        title_3 = Tex(
            "\\hphantom{\\textbf{Problema 4.} }El tri\\'angulo $ABC$ tiene circunferencia circunscrita $\\Omega$ y circuncentro $O$. Una circunferencia $\\Gamma$ de centro $A$ corta al segmento $BC$ en los puntos $D$ y $E$ tales que $B$, $D$, $E$ y $C$ son todos diferentes y est\\'an en la recta $BC$ en este orden. Sean $F$ y $G$ los puntos de intersecci\\'on de $\\Gamma$ y $\\Omega$, tales que $A$, $F$, $B$, $C$ y $G$ est\\'an sobre $\\Omega$ en este orden. Sea $K$ el segundo punto de intersecci\\'on de la circunferencia circunscrita al tri\\'angulo $BDF$ y el segmento $AB$. Sea $L$ el segundo punto de intersecci\\'on de la circunferencia circunscrita al tri\\'angulo $CGE$ y el segmento $CA$." + linebreak + "Supongamos que las rectas $FK$ y $GL$ son distintas y se cortan en el punto $X$. Demostrar que $X$ est\\'a en la recta $AO$.",
            tex_environment=None,
            tex_template=TexTemplateLibrary.simple
        )
        title_3.scale(0.7).to_corner(UP)

        title_2_3 = VGroup(title_2[0], title_3)

        isquare = "\\text{\\tiny $\\blacksquare\\,$ }&" ##ii = "$\\bullet\\,$ "

        text_1 = MathTex(
            isquare, #0
            "A", #1
            "D", #2
            "=", #3
            "A", #4
            "E", #5
            "=", #6
            "A", #7
            "F", #8
            "=", #9
            "A", #10
            "G" + linebreak, #11
            isquare, #12
            "B", #13
            "D", #14
            "K", #15
            "F", #16
            "\\text{ es c\\'iclico}" + linebreak, #17
            isquare, #18
            "C", #19
            "G", #20
            "L", #21
            "E", #22
            "\\text{ es c\\'iclico}" + linebreak, #23
            isquare + "\\text{Demostrar que }", #24
            "A", #25
            ",", #26
            "X", #27
            ",", #28
            "O", #29
            "\\text{ son colineales}", #30
            tex_environment="align*",
            tex_template=TexTemplateLibrary.simple
        )
        iff = "\\iff &"

        text_2 = MathTex(
            "&A", #0
            ",", #1
            "X", #2
            ",", #3
            "O", #4
            "\\text{ son colineales}" + linebreak, #5
            iff, #6
            "X", #7
            "\\text{ pertenece a la mediatriz de }", #8
            "F", #9
            "G" + linebreak, #10
            iff, #11
            "\\angle ", #12
            "K", #13
            "F", #14
            "G", #15
            "=", #16
            "\\angle ", #17
            "L", #18
            "G", #19
            "F", #20
            tex_environment="align*",
            tex_template=TexTemplateLibrary.simple
        )
        text_3 = MathTex(
            isquare + "AD=AE=AF=AG" + linebreak + isquare + "BDKF\\text{ es c\\'iclico}" + linebreak + isquare + "CGLE\\text{ es c\\'iclico}" + linebreak + isquare + "\\text{Demostrar que }", #0
            "\\angle ", #1
            "K", #2
            "F", #3
            "G", #4
            "=", #5
            "\\angle ", #6
            "L", #7
            "G", #8
            "F", #9
            tex_environment="align*",
            tex_template=TexTemplateLibrary.simple
        )
        text_4 = MathTex(
            isquare + "AD=AE=AF=AG" + linebreak + isquare + "BDKF\\text{ es c\\'iclico}" + linebreak + isquare + "CGLE\\text{ es c\\'iclico}" + linebreak + isquare + "\\text{Demostrar que }", #0
            "x", #1
            "=", #2
            "y", #3
            tex_environment="align*",
            tex_template=TexTemplateLibrary.simple
        )
        for item in [text_1, text_2, text_3, text_4]:
            item.set_color(text_color).scale(0.6)

        text_5 = MathTex(
            "C", #0
            "-", #1
            "x", #2
            "&=", #3
            "C", #4
            "-", #5
            r"y \\ ", #6
            "x", #7
            "&=", #8
            "y", #9
            tex_environment="align*",
            tex_template=TexTemplateLibrary.simple
        )
        text_1.shift(4*RIGHT)
        for item in [text_2, text_3, text_4]:
            item.move_to(text_1, aligned_edge=LEFT)

        text_5.move_to(text_1)

        ## DEFINING COMPLEX NUMBERS (LIKE ASYMPTOTE IN LATEX)
        ## A, B, C, D, E, F, G, K, L, X
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

        ## DEFINING DOTS, CIRCLES, LINES
        ## Dots
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

        ## Circles
        circle_omega = CR(k, c=BLUE)
        circle_BDF = CP(B, O1, GREEN)
        circle_CGE = CP(C, O2, GREEN)
        circle_gamma = CP(D, A, GREEN)

        ## Lines
        line_FX = LINE(F, X, GREEN)
        line_GX = LINE(G, X, GREEN)
        line_AF = LINE(A, F, PURPLE)
        line_AG = LINE(A, G, PURPLE)
        line_AB = LINE(A, B, RED)
        line_BC = LINE(B, C, RED)
        line_CA = LINE(C, A, RED)

        dashed_FX = DashedVMobject(line_FX).set_color(GREEN)
        dashed_GX = DashedVMobject(line_GX).set_color(GREEN)

        ## SHIFTING POINTS
        r, l = 3.5, 3
        to_shift_right = [
            circle_omega,
            dot_O,
            dot_A,
            dot_B,
            dot_C,
            line_AB,
            line_BC,
            line_CA
        ]
        to_shift_left = [
            dot_K,
            dot_L,
            circle_BDF,
            circle_CGE,
            dot_X,
            line_FX,
            line_GX,
            dashed_FX,
            dashed_GX,
            line_AF,
            line_AG
        ]
        for item in to_shift_right:
            item.shift(r*RIGHT)

        for item in to_shift_left:
            item.shift(l*LEFT)

        ## LABELS, VGROUPS AND LISTS
        ## Labels
        f = .5
        label_omega = MP('$\\Omega$', circle_omega, UP, f)
        label_gamma = MP('$\\Gamma$', circle_gamma, RIGHT, f)
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

        ## VGroups and Lists
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
        
        ## RENDERING VIDEO
        self.play(*WR(title_1), run_time=4)
        self.wait()
        self.play(
            *FO(title_1),
            *RT(title_1[1].copy(), title_2[0])
        )
        self.play(*MAKE(title_3), run_time=4)
        self.wait(4)
        self.play(ANIM(title_2_3).scale(0.5).shift(UP + 3.5*LEFT))
        self.play(*GC(dot_O))
        self.play(*GC(label_O))

        FORW(self, dot_O, label_O)

        self.play(*GC(circle_omega))
        self.play(*GC(label_omega))

        FORW(self, label_omega)

        self.play(*GC(dots_ABC))
        self.play(*GC(labels_ABC))

        FORW(self, *dots_ABC, *labels_ABC)

        self.play(*MAKE(lines_ABC))

        change_1 = VGroup(
            circle_omega,
            *lines_ABC,
            dot_O,
            *dots_ABC,
            label_O,
            label_omega,
            *labels_ABC
        )
        self.play(*FO(title_2_3))
        self.play(ANIM(change_1).shift(r*LEFT), run_time=2)
        self.play(*GC(circle_gamma))
        self.play(*GC(label_gamma))
        self.play(*GC(dots_FDEG))
        self.play(*GC(labels_FDEG))

        FORW(self, *dots_FDEG, *labels_FDEG)

        self.play(
            ANIM(
                VGroup(
                    change_1,
                    circle_gamma,
                    *dots_FDEG,
                    label_gamma,
                    *labels_FDEG
                )
            ).shift(l*LEFT)
        )
        self.play(*COL(dots_FDEG, c=dot_color))
        self.play(
            *WR(text_1[0]),
            *RT(label_A.copy(), text_1[1]),
            *RT(label_D.copy(), text_1[2]),
            run_time=2
        )
        self.play(
            *WR(text_1[3]),
            *RT(label_A.copy(), text_1[4]),
            *RT(label_E.copy(), text_1[5]),
            run_time=2
        )
        self.play(
            *WR(text_1[6]),
            *RT(label_A.copy(), text_1[7]),
            *RT(label_F.copy(), text_1[8]),
            run_time=2
        )
        self.play(
            *WR(text_1[9]),
            *RT(label_A.copy(), text_1[10]),
            *RT(label_G.copy(), text_1[11]),
            run_time=2
        )
        self.play(*FO(circle_gamma, label_gamma), *COL(text_1[:12], dots_FDEG))
        self.play(*GC(circle_BDF))
        self.play(*GC(dot_K))
        self.play(*GC(label_K))

        FORW(self, dot_K, label_K)

        self.play(*COL(dots_KBDF, c=dot_color))
        self.play(
            *WR(text_1[12]),
            *RT(label_B.copy(), text_1[13]),
            *RT(label_D.copy(), text_1[14]),
            *RT(label_K.copy(), text_1[15]),
            *RT(label_F.copy(), text_1[16]),
            run_time=2
        )
        self.play(*WR(text_1[17]))
        self.play(*FO(circle_BDF))
        self.play(*COL(text_1[12:18], dots_KBDF))
        self.play(*GC(circle_CGE))
        self.play(*GC(dot_L))
        self.play(*GC(label_L))

        FORW(self, dot_L, label_L)

        self.play(*COL(dots_LCGE, c=dot_color))
        self.play(
            *WR(text_1[18]),
            *RT(label_C.copy(), text_1[19]),
            *RT(label_G.copy(), text_1[20]),
            *RT(label_L.copy(), text_1[21]),
            *RT(label_E.copy(), text_1[22]),
            run_time=2
        )
        self.play(*WR(text_1[23]))
        self.play(*FO(circle_CGE))
        self.play(*COL(text_1[18:24], dots_LCGE))
        self.play(*MAKE(lines_FX_GX), run_time=2)
        self.play(*GC(dot_X))
        self.play(*GC(label_X))

        FORW(self, dot_X, label_X)

        self.play(*RT(lines_FX_GX, dashed_FX_GX))
        self.play(*COL(dots_AXO, c=dot_color))
        self.play(
            *WR(text_1[24]),
            *RT(label_A.copy(), text_1[25]),
            *WR(text_1[26]),
            *RT(label_X.copy(), text_1[27]),
            *WR(text_1[28]),
            *RT(label_O.copy(), text_1[29]),
            *WR(text_1[30]),
            run_time=2
        )
        self.play(*COL(text_1[24:], dots_AXO))
        self.wait()
        self.play(*MAKE(lines_AF_AG))

        change_2 = [
            *lines_ABC,
            dot_B,
            dot_C,
            dot_D,
            dot_E,
            label_B,
            label_C,
            label_D,
            label_E
        ]
        self.play(*FO(change_2, label_omega))

        t = arg(G-F)
        buff = .25

        self.play(
            Rotate(
                VGroup(
                    *dashed_FX_GX,
                    *lines_AF_AG,
                    dot_A,
                    dot_F,
                    dot_G,
                    dot_X,
                    dot_K,
                    dot_L
                ),
                t,
                IN,
                nparray(dot_O)
            ),
            UFF(label_A, lambda m: m.next_to(dot_A, UP, buff*f)),
            UFF(label_F, lambda m: m.next_to(dot_F, LEFT, buff*f)),
            UFF(label_G, lambda m: m.next_to(dot_G, RIGHT, buff*f)),
            UFF(label_K, lambda m: m.next_to(dot_K, dir(comp(dot_K) - comp(dot_O)), buff*f)),
            UFF(label_L, lambda m: m.next_to(dot_L, dir(comp(dot_L) - comp(dot_O)), buff*f)),
            UFF(label_X, lambda m: m.next_to(dot_X, DOWN, buff*f)),
            run_time=2
        )
        line_OF = LINE(dot_O, dot_F, RED)
        line_OG = LINE(dot_O, dot_G, RED)
        lines_OF_OG = VGroup(line_OF, line_OG)

        self.play(*MAKE(lines_OF_OG))
        self.play(*FO(circle_omega))

        arrow_OA = DA(dot_O, dot_A, .26, BLUE, stroke_width=4, tip_length=.2)
        new_label_A = MP('$A$', dot_A, dir(135), f)
        new_label_O = MP('$O$', dot_O, dir(225), f)
        new_label_X = MP('$X$', dot_X, dir(267), f)
        repl_rad = .01

        self.play(
            *CCT(label_A, new_label_A, float=repl_rad),
            *CT(label_O, new_label_O, float=repl_rad),
            *CT(label_X, new_label_X, float=repl_rad)
        )
        self.play(*MAKE(arrow_OA), run_time=2)

        text_FG = Tex('Mediatriz de $FG$').scale(.5).next_to(nparray(dot_O) + .1*RIGHT + .3*DOWN)

        self.play(*WR(text_FG))
        self.wait()
        self.play(
            *FO(text_1),
            *[ReplacementTransform(text_1[i+25].copy(), text_2[i]) for i in range(0, 6)]
        )
        self.play(*WR(text_2[6]))
        self.play(
            *RT(label_X.copy(), text_2[7]),
            *WR(text_2[8]),
            *RT(label_F.copy(), text_2[9]),
            *RT(label_G.copy(), text_2[10]),
            run_time=2
        )
        new_label_A = MP('$A$', dot_A, UP, f)
        new_label_O = MP('$O$', dot_O, DOWN, f)
        new_label_X = MP('$X$', dot_X, DOWN, f)

        self.play(*FO(arrow_OA, text_FG))
        self.play(
            *CT(label_A, new_label_A, float=repl_rad),
            *CCT(label_O, new_label_O, float=repl_rad),
            *CCT(label_X, new_label_X, float=repl_rad)
        )
        self.play(
            *FO(
                label_A,
                label_O,
                dot_A,
                dot_O,
                *lines_AF_AG,
                *lines_OF_OG
            )
        )
        line_FG = LINE(dot_F, dot_G, GREEN)
        arc_GFK = MA(dot_G, dot_F, dot_K, .5, 2, color=PURPLE)
        arc_LGF = MA(dot_L, dot_G, dot_F, .5, 2, color=PURPLE)
        
        self.play(*MAKE(line_FG))

        BACK(self, arc_GFK, arc_LGF)
        line_FK = LINE(dot_F, dot_K, GREEN)
        line_GL = LINE(dot_G, dot_L, GREEN)
        lines_FK_GL = VGroup(line_FK, line_GL)

        self.play(*MAKE(arc_GFK, arc_LGF))
        self.play(*WR(text_2[11]))
        self.play(
            *WR(text_2[12]),
            *RT(label_K.copy(), text_2[13]),
            *RT(label_F.copy(), text_2[14]),
            *RT(label_G.copy(), text_2[15]),
            run_time=2
        )
        self.play(
            *WR(text_2[16:18]),
            *RT(label_L.copy(), text_2[18]),
            *RT(label_G.copy(), text_2[19]),
            *RT(label_F.copy(), text_2[20]),
            run_time=2
        )
        self.play(
            *RT(dashed_FX, line_FK),
            *RT(dashed_GX, line_GL),
            *FO(dot_X, label_X),
            run_time=2
        )
        self.play(*FO(text_2[:12]))
        self.play(
            *WR(text_3[0]),
            *[ReplacementTransform(text_2[i+11], text_3[i]) for i in range(1, 10)],
            run_time=2
        )
        self.play(
            Rotate(
                VGroup(
                    arc_GFK,
                    arc_LGF,
                    line_FG,
                    *lines_FK_GL,
                    dot_K,
                    dot_L,
                    dot_F,
                    dot_G
                ),
                t,
                OUT,
                nparray(dot_O)
            ),
            UFF(label_F, lambda m: m.next_to(dot_F, LEFT, buff*f)),
            UFF(label_G, lambda m: m.next_to(dot_G, RIGHT, buff*f)),
            UFF(label_K, lambda m: m.next_to(dot_K, dir(comp(dot_K)-comp(dot_O)), buff*f)),
            UFF(label_L, lambda m: m.next_to(dot_L, dir(comp(dot_L)-comp(dot_O)), buff*f))
        )
        VGroup(dot_A, arrow_OA).rotate(t, about_point=nparray(dot_O))
        label_A.next_to(dot_A, UP, buff*f)
        FORW(
            self,
            arc_GFK,
            arc_LGF,
            line_FG,
            *lines_FK_GL,
            dot_K,
            dot_L,
            dot_F,
            dot_G,
            dot_A,
            dot_O,
            *change_2[3:]
        )
        self.play(
            *FI(
                dot_O,
                label_O,
                dot_A,
                label_A,
                circle_omega,
                label_omega,
                *change_2
            )
        )
        self.wait()
        self.play(
            *RT(text_3[1:5], text_4[1]),
            *RT(text_3[5], text_4[2]),
            *RT(text_3[6:], text_4[3])
        )
        line_GF = LINE(dot_G, dot_F)
        text_x = Tex('$x$').scale(f).move_to(Angle(line_FG, line_FK, .7))
        text_y = Tex('$y$').scale(f).move_to(Angle(line_GL, line_GF, .7))

        self.play(
            *TR(arc_GFK, MA(dot_G, dot_F, dot_K, .5)),
            *TR(arc_LGF, MA(dot_L, dot_G, dot_F, .5)),
            *RT(text_4[1].copy(), text_x),
            *RT(text_4[3].copy(), text_y),
            run_time=2
        )
        text_FG.shift(.42*DOWN + .05*RIGHT)
        new_label_A = MP('$A$', dot_A, dir(159 + degrees(t)), f)
        new_label_O = MP('$O$', dot_O, dir(225 + degrees(t)), f)

        self.play(
            *CCT(label_A, new_label_A, float=repl_rad),
            *CT(label_O, new_label_O, float=repl_rad)
        )
        self.play(*MAKE(arrow_OA), run_time=2)
        self.play(*WR(text_FG))

        new_label_A = MP('$A$', dot_A, UP, f)
        new_label_O = MP('$O$', dot_O, DOWN, f)
        line_OA = LINE(dot_O, dot_A, PURPLE)
        arc_OA_GF = RightAngle(line_OA, line_GF, .2)
        BACK(self, arc_OA_GF)

        self.play(*MAKE(arc_OA_GF))
        self.wait()
        self.play(
            *FO(text_FG),
            *RT(arrow_OA, line_OA)
        )
        self.play(
            *CT(label_A, new_label_A, float=repl_rad),
            *CCT(label_O, new_label_O, float=repl_rad)
        )
        text_C = Tex('$C$').scale(f).move_to(Angle(line_CA, line_BC, .8, (1, -1)))
        arc_ACB = MA(dot_A, dot_C, dot_B, .5)
        BACK(self, arc_ACB)

        self.play(
            *MAKE(arc_ACB),
            *RT(label_C.copy(), text_C),
            run_time=2
        )
        change_3 = [
            arc_GFK,
            arc_LGF,
            arc_OA_GF,
            *lines_FK_GL,
            line_FG,
            text_x,
            text_y,
            dot_D,
            dot_E,
            dot_F,
            dot_K,
            dot_G,
            dot_L,
            label_D,
            label_E,
            label_F,
            label_K,
            label_G,
            label_L
        ]
        line_OB = LINE(dot_O, dot_B, PURPLE)

        self.play(
            *FO(change_3),
            *MAKE(line_OB)
        )
        arc_AOB = Angle(line_OA, line_OB, .35)
        BACK(self, arc_AOB)
        text_2C = Tex('$2C$').scale(f).move_to(Angle(line_OA, line_OB, .9))

        self.play(
            *MAKE(arc_AOB),
            *RT(text_C.copy(), text_2C),
            run_time=2
        )
        arc_BAO = MA(dot_B, dot_A, dot_O, .5)
        arc_OBA = MA(dot_O, dot_B, dot_A, .5)
        BACK(self, arc_BAO, arc_OBA)
        text_C_1 = Tex('$90-C$').scale(f).move_to(Angle(line_AB, line_OA, 1.4, (1, -1)))
        text_C_2 = Tex('$90-C$').scale(f).move_to(Angle(line_OB, line_AB, 1.4, (-1, -1)))

        self.play(
            *MAKE(arc_BAO, arc_OBA),
            *RT(text_2C.copy(), text_C_1),
            *RT(text_2C.copy(), text_C_2),
            run_time=2
        )
        self.play(
            *FO(arc_AOB, arc_OBA, line_OB, text_2C, text_C_2)
        )
        self.wait()

        BACK(self, arc_OA_GF)

        self.play(*FI(change_3))

        arc_FG_AB = Angle(line_FG, line_AB, .85, (1, -1))
        text_C_3 = Tex('$C$').scale(f).move_to(Angle(line_FG, line_AB, 1.2, (1, -1)))
        BACK(self, arc_FG_AB)

        self.play(
            *RT(text_C_1.copy(), text_C_3),
            *MAKE(arc_FG_AB),
            run_time=2
        )
        self.wait()

        circle_BDF.set_color(ORANGE)
        BACK(self, circle_BDF)

        self.play(*GC(circle_BDF))

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
        FORW(self, ref_dot1)

        self.play(
            *FO(
                arc_LGF,
                arc_ACB,
                arc_BAO,
                arc_OA_GF,
                arc_FG_AB,
                arc_GFK,
                circle_omega,
                line_AB,
                line_BC,
                line_CA,
                line_OA,
                line_FK,
                line_GL,
                line_FG,
                dot_O,
                dot_A,
                dot_B,
                dot_C,
                dot_D,
                dot_E,
                dot_F,
                dot_G,
                dot_K,
                dot_L,
                label_O,
                label_omega,
                label_A,
                label_B,
                label_C,
                label_D,
                label_E,
                label_F,
                label_G,
                label_K,
                label_L,
                text_y,
                text_C,
                text_C_1,
                text_C_3,
                text_x
            ),
            *RT(
                [
                    arc_FG_AB.copy(),
                    arc_GFK.copy(),
                    circle_BDF,
                    line_AB.copy(),
                    line_BC.copy(),
                    line_FK.copy(),
                    line_FG.copy(),
                    dot_F.copy(),
                    dot_K.copy(),
                    dot_D.copy(),
                    dot_B.copy(),
                    label_F.copy(),
                    label_K.copy(),
                    label_D.copy(),
                    label_B.copy(),
                    text_C_3.copy(),
                    text_x.copy()
                ],
                [
                    arc_FG_AB1,
                    arc_GFK1,
                    circle_BDF1,
                    line_KB1,
                    line_BD1,
                    line_FK1,
                    line_FG1,
                    dot_F1,
                    dot_K1,
                    dot_D1,
                    dot_B1,
                    label_F1,
                    label_K1,
                    label_D1,
                    label_B1,
                    text_C1,
                    text_x1
                ],
                True
            ),
            *GC(ref_dot1)
        )
        arc_FKB1 = MA(dot_F1, dot_K1, dot_B1, .5)
        text_Cx = MathTex('C', '-', 'x').scale(f).move_to(Angle(line_FK1, line_KB1, .9, (-1, 1)))
        BACK(self, arc_FKB1)

        self.play(
            *RT(text_C1.copy(), text_Cx[0]),
            *RT(text_x1.copy(), text_Cx[2]),
            *WR(text_Cx[1]),
            *MAKE(arc_FKB1),
            run_time=2
        )
        self.play(*FO(arc_FG_AB1, arc_GFK1, text_C1, text_x1, label_K1, line_FG1, ref_dot1))

        alpha = degrees(arg((K-O1)/(D-O1)))
        new_text_Cx = text_Cx.copy().move_to(Angle(LINE(D1, F1), LINE(D1, B1), 1.2))
        FORW(self, dot_F1, dot_B1, dot_D1, dot_K1)
        BACK(self, arc_FKB1)
        alpha_tracker = ValueTracker(alpha)
        dot_K1.add_updater(lambda m: m.become(dot_D1.copy().rotate(radians(alpha_tracker.get_value()), about_point=nparray(dot_O))))
        arc_FKB1.add_updater(lambda m: m.become(MA(dot_F1, dot_D1.copy().rotate(radians(alpha_tracker.get_value()), about_point=nparray(dot_O)), dot_B1, .5)))
        line_FK1.add_updater(lambda m: m.become(LINE(dot_F1, dot_D1.copy().rotate(radians(alpha_tracker.get_value()), about_point=nparray(dot_O)), GREEN)))
        line_KB1.add_updater(lambda m: m.become(LINE(dot_D1.copy().rotate(radians(alpha_tracker.get_value()), about_point=nparray(dot_O)), dot_B1, RED)))

        self.play(
            ANIM(alpha_tracker).set_value(0),
            *CT(text_Cx, new_text_Cx, path_arc=-radians(alpha)),
            run_time=2
        )
        dot_K1.clear_updaters()
        arc_FKB1.clear_updaters()
        line_FK1.clear_updaters()
        line_KB1.clear_updaters()
        self.remove(line_KB1, dot_K1)
        FORW(self, dot_C, dot_E)
        beta = 120
        beta_tracker = ValueTracker(0)
        arc_FKB1.add_updater(lambda m: m.become(MA(dot_F1, dot_D1, dot_B1, .5)))
        line_FK1.add_updater(lambda m: m.become(LINE(dot_F1, dot_D1, GREEN)))
        text_Cx.add_updater(lambda m: m.move_to(MA(dot_F1, dot_D1, dot_B1, 1.2 - beta_tracker.get_value()*(.15)/beta)))

        self.play(
            *RT(
                [
                    line_BD1,
                    dot_F1,
                    dot_D1,
                    dot_B1,
                    label_F1,
                    label_D1,
                    label_B1
                ],
                [
                    line_BC,
                    dot_F,
                    dot_D,
                    dot_B,
                    label_F,
                    label_D,
                    label_B
                ],
                True
            ),
            *FO(circle_BDF1),
            *FI(
                arc_LGF,
                arc_ACB,
                circle_omega,
                line_CA,
                line_GL,
                line_FG,
                dot_A,
                dot_C,
                dot_E,
                dot_G,
                dot_L,
                label_omega,
                label_A,
                label_C,
                label_E,
                label_G,
                label_L,
                text_y,
                text_C
            ),
            ANIM(beta_tracker).set_value(beta)
        )
        self.wait()

        arc_FKB1.clear_updaters()
        line_FK1.clear_updaters()
        text_Cx.clear_updaters()
        circle_CGE.set_color(ORANGE)
        BACK(self, circle_CGE)

        self.play(*GC(circle_CGE))

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
        FORW(self, ref_dot2, dot_A, dot_B, dot_F, dot_D)

        self.play(
            *FO(
                arc_FKB1,
                arc_ACB,
                arc_LGF,
                circle_omega,
                line_BC,
                line_CA,
                line_GL,
                line_FG,
                line_FK1,
                dot_A,
                dot_B,
                dot_C,
                dot_D,
                dot_E,
                dot_F,
                dot_G,
                dot_L,
                label_omega,
                label_A,
                label_B,
                label_C,
                label_D,
                label_E,
                label_F,
                label_G,
                label_L,
                text_y,
                text_C,
                text_Cx,
            ),
            *RT(
                [
                    arc_ACB.copy(),
                    arc_LGF.copy(),
                    circle_CGE,
                    line_CA.copy(),
                    line_BC.copy(),
                    line_GL.copy(),
                    line_FG.copy(),
                    dot_G.copy(),
                    dot_L.copy(),
                    dot_E.copy(),
                    dot_C.copy(),
                    label_G.copy(),
                    label_L.copy(),
                    label_E.copy(),
                    label_C.copy(),
                    text_C.copy(),
                    text_y.copy()
                ],
                [
                    arc_ACB2,
                    arc_LGF2,
                    circle_CGE2,
                    line_CL2,
                    line_EC2,
                    line_GL2,
                    line_FG2,
                    dot_G2,
                    dot_L2,
                    dot_E2,
                    dot_C2,
                    label_G2,
                    label_L2,
                    label_E2,
                    label_C2,
                    text_C2,
                    text_y2
                ],
                True
            ),
            *GC(ref_dot2)
        )
        theta = degrees(arg((G-O2)/(C-O2)))
        new_text_C2 = text_C2.copy().move_to(Angle(line_GL2, line_FG2, 1.5, (1, -1)))
        FORW(self, dot_G2, dot_C2, dot_E2, dot_L2)
        BACK(self, arc_ACB2)
        theta_tracker = ValueTracker(theta)
        dot_C2.add_updater(lambda m: m.become(dot_G2.copy().rotate(radians(theta_tracker.get_value()), IN, about_point=nparray(dot_O))))
        arc_ACB2.add_updater(lambda m: m.become(MA(dot_L2, dot_G2.copy().rotate(radians(theta_tracker.get_value()), IN, about_point=nparray(dot_O)), dot_E2, .5+.7*(1-theta_tracker.get_value()/theta))))
        line_CL2.add_updater(lambda m: m.become(LINE(dot_G2.copy().rotate(radians(theta_tracker.get_value()), IN, about_point=nparray(dot_O)), L2, RED)))
        line_EC2.add_updater(lambda m: m.become(LINE(dot_E2, dot_G2.copy().rotate(radians(theta_tracker.get_value()), IN, about_point=nparray(dot_O)), RED)))

        self.play(*FO(label_C2))
        self.play(
            ANIM(theta_tracker).set_value(0),
            *CCT(text_C2, new_text_C2, path_arc=radians(theta)),
            run_time=2
        )
        dot_C2.clear_updaters()
        arc_ACB2.clear_updaters()
        line_CL2.clear_updaters()
        line_EC2.clear_updaters()
        self.remove(line_CL2, dot_C2)
        arc_FGE2 = MA(ref_dot2, dot_G2, dot_E2, 1.9)
        text_Cy = MathTex('C', '-', 'y').scale(f).move_to(Angle(line_FG2, line_EC2, 2.4, (-1, -1)))
        BACK(self, arc_FGE2)

        self.play(
            *RT(text_C2.copy(), text_Cy[0]),
            *RT(text_y2.copy(), text_Cy[2]),
            *WR(text_Cy[1]),
            *MAKE(arc_FGE2),
            run_time=2
        )
        self.play(*FO(arc_ACB2, arc_LGF2, text_C2, text_y2, label_L2, line_GL2, dot_L2))

        arc_FGE = MA(dot_F, dot_G, dot_E, .7)
        line_EG = LINE(dot_E, dot_G, GREEN)
        FORW(self, text_Cy, dot_F)

        self.play(
            *RT(
                [
                    arc_FGE2,
                    line_FG2,
                    line_EC2,
                    dot_G2,
                    dot_E2,
                    label_G2,
                    label_E2,
                    
                ],
                [
                    arc_FGE,
                    line_FG,
                    line_EG,
                    dot_G,
                    dot_E,
                    label_G,
                    label_E
                ],
                True
            ),
            ANIM(text_Cy).move_to(Angle(line_FG, line_EG, 1.8, (-1, -1))),
            *FO(circle_CGE2, ref_dot2),
            *FI(
                arc_FKB1,
                line_BC,
                line_FK1,
                dot_A,
                dot_B,
                dot_C,
                dot_D,
                dot_F,
                label_A,
                label_B,
                label_C,
                label_D,
                label_F,
                text_Cx
            )
        )
        self.wait()

        circle_gamma.set_color(BLUE)
        FORW(self, dot_D, dot_E, dot_G, text_Cx)
        
        self.play(*GC(circle_gamma), run_time=2)
        self.play(*GC(label_gamma))
        self.play(*FO(text_3, text_4))
        self.play(
            *[ReplacementTransform(text_Cx[i].copy(), text_5[i]) for i in range(0, 3)],
            *WR(text_5[3]),
            *[ReplacementTransform(text_Cy[i].copy(), text_5[i+4]) for i in range(0, 3)],
            run_time=2
        )
        self.wait()
        self.play(
            ANIM(text_5[:2]).set_color(DARK_GRAY),
            ANIM(text_5[4:6]).set_color(DARK_GRAY)
        )
        self.play(
            *RT([text_5[2].copy(), text_5[6].copy()], [text_5[7], text_5[9]], True),
            *WR(text_5[8]),
            run_time=2
        )
        self.play(ShowCreationThenDestructionAround(text_5[7:10]), ANIM(text_5[7:10]).set_color(YELLOW))
        self.play(ShowCreationThenDestructionAround(text_5[7:10]), ANIM(text_5[7:10]).set_color(WHITE))
        self.wait()
        self.play(
            AnimationGroup(
                *[FadeOutAndShift(item, DOWN) for item in self.mobjects]
            )
        )
        ending_credit = Tex(
            "Video hecho con ",
            r"\textsc{Manim}"
        )
        ending_credit.scale(1.5)
        ending_credit[1].set_color_by_gradient(BLUE_B, BLUE_E)

        self.play(*WR(ending_credit[0]))
        self.play(*WR(ending_credit[1]))
        self.wait()
        self.play(FadeOutAndShift(ending_credit, DOWN))
        self.wait()

if __name__ == '__main__':
    from subprocess import run
    run('manim imo_2015_p4.py Video -p')