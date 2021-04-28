import os, sys
filepath = os.path.realpath(__file__)
sys.path.append(os.path.dirname(os.path.dirname(filepath)))

from asymptote import *

class Thumbnail(Scene):
    def construct(self):
        imo_logo = ImageMobject("imo_2018_p1/imo_2018_logo.png")
        text_1 = Tex(r"$\mathbb{IMO}$ 2018")
        text_2 = Tex(r"\textsf{Problema 1}")
        text_3 = Tex(r"\emph{Solución}", " con ", r"$\mathbb{M}$\textsc{anim}")

        text_1.set_color(YELLOW_A)
        text_2.set_color(BLUE_B)
        text_3[0].set_color_by_gradient(RED_B, RED_A)
        text_3[1].set_color_by_gradient(GREY_A)
        text_3[2].set_color_by_gradient(GOLD, GOLD_A)

        imo_logo.scale(1.2)
        text_1.scale(2.6)
        text_2.scale(2.5)
        text_3.scale(2.8)

        imo_logo.shift(3.5*LEFT+1.2*UP)
        text_2.next_to(text_1, DOWN, .68)
        VGroup(text_1, text_2).shift(2.9*RIGHT+1.76*UP)
        text_3.shift(1.7*DOWN)

        line_1 = Line(LEFT, RIGHT, color=BLUE_B).set_width(text_2.get_width()+.4)
        line_1.next_to(text_2, DOWN, buff=.2)
        line_2 = Line(LEFT, RIGHT, color=BLUE_A).set_width(text_2.get_width()+.2)
        line_2.next_to(text_2, DOWN, buff=.34)

        self.add(imo_logo, text_1, text_2, text_3, line_1, line_2)

if __name__ == '__main__':
    RUN(filepath, 'Thumbnail', '-spqk -o Thumbnail')