from manim import *

class Thumbnail(Scene):
    def construct(self):
        logo = ImageMobject('assets/2018.png')
        t1 = Tex(r'$\mathbb{IMO}$ 2018')
        t2 = Tex(r'\textsf{Problema 1}')
        t3 = Tex(r"\emph{Soluci\'on}", ' con ', r'$\mathbb{M}$\textsc{anim}')

        t1.set_color(YELLOW_A)
        t2.set_color(BLUE_B)
        t3[0].set_color_by_gradient(RED_B, RED_A)
        t3[1].set_color_by_gradient(GREY_A)
        t3[2].set_color_by_gradient(GOLD, GOLD_A)

        logo.scale(1.2).shift(3.5*LEFT+1.2*UP)
        t1.scale(2.6)
        t2.scale(2.5).next_to(t1, DOWN, .68)
        t3.scale(2.8).shift(1.7*DOWN)
        VGroup(t1, t2).shift(2.9*RIGHT+1.76*UP)

        l1 = Line(LEFT, RIGHT, color=BLUE_B).set_width(t2.get_width()+.4)
        l1.next_to(t2, DOWN, buff=.2)
        l2 = Line(LEFT, RIGHT, color=BLUE_A).set_width(t2.get_width()+.2)
        l2.next_to(t2, DOWN, buff=.34)

        self.add(logo, t1, t2, t3, l1, l2)
