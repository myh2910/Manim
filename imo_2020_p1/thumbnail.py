import os, sys
filepath = os.path.realpath(__file__)
sys.path.append(os.path.dirname(os.path.dirname(filepath)))

from asymptote import *

class Thumbnail(Scene):
    def construct(self):
        imo_logo = ImageMobject("imo_2020_p1/imo_2020_logo.png")
        text_1 = Tex(r"\textsf{Problema 1}")
        text_2 = Tex(r"\emph{Solución}", " con ", r"\textsc{Manim}")

        text_1.set_color("#3c94d4")
        text_2[0].set_color_by_gradient(RED_D, RED)
        text_2[1].set_color_by_gradient(GREY)
        text_2[2].set_color_by_gradient(GOLD_D, GOLD)

        imo_logo.scale(1.6)
        text_1.scale(3.4)
        text_2.scale(3)

        imo_logo.shift(2.1*UP)
        text_1.shift(.7*DOWN)
        text_2.shift(2.6*DOWN)

        line_1 = Line(LEFT, RIGHT, color=GOLD_D).set_width(text_2[2].get_width())
        line_1.next_to(text_2[2], DOWN, buff=0.2)
        line_2 = Line(LEFT, RIGHT, color=GOLD).set_width(text_2[2].get_width()-.6)
        line_2.next_to(text_2[2], DOWN, buff=0.35)

        self.add(imo_logo, text_1, text_2, line_1, line_2)

if __name__ == '__main__':
    RUN(filepath, 'Thumbnail', '-spqk -o Thumbnail -c WHITE')