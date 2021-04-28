import os, sys
filepath = os.path.realpath(__file__)
sys.path.append(os.path.dirname(os.path.dirname(filepath)))

from asymptote import *

class Thumbnail(Scene):
    def construct(self):
        logo = ImageMobject("imo_2020_p1/imo_2020_logo.png")
        t1 = Tex(r"\textsf{Problema 1}")
        t2 = Tex(r"\emph{Solución}", " con ", r"\textsc{Manim}")

        t1.set_color("#3c94d4")
        t2[0].set_color_by_gradient(RED_D, RED)
        t2[1].set_color_by_gradient(GREY)
        t2[2].set_color_by_gradient(GOLD_D, GOLD)

        logo.scale(1.6).shift(2.1*UP)
        t1.scale(3.4).shift(.7*DOWN)
        t2.scale(3).shift(2.6*DOWN)

        l1 = Line(LEFT, RIGHT, color=GOLD_D).set_width(t2[2].get_width())
        l1.next_to(t2[2], DOWN, buff=0.2)
        l2 = Line(LEFT, RIGHT, color=GOLD).set_width(t2[2].get_width()-.6)
        l2.next_to(t2[2], DOWN, buff=0.35)

        self.add(logo, t1, t2, l1, l2)

if __name__ == '__main__':
    RUN(filepath, 'Thumbnail', '-spqk -o Thumbnail -c WHITE')