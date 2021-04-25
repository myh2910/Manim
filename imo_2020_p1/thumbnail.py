import os, sys
filepath = os.path.realpath(__file__)
sys.path.append(os.path.dirname(os.path.dirname(filepath)))

from asymptote import *

class Thumbnail(Scene):
    def construct(self):
        imo_logo = ImageMobject("imo_2020_p1/imo_2020_logo.png")
        text_1 = Tex(r"\textsf{Problema 1}")
        text_2 = Tex(r"\emph{Solución} con ", r"\textsc{Manim}")

        text_1.set_color_by_gradient("#3c94d4", "#B0E0E6")
        text_2[0].set_color_by_gradient("#FFB6C1", "#F08080")
        text_2[1].set_color_by_gradient("#EEE8AA", "#DAA520")
        text_1.scale(2.8)
        text_2.scale(3)
        VGroup(text_1, text_2).arrange(DOWN, buff=1.7)
        text_1.shift(3.6*RIGHT)
        imo_logo.shift(3.4*LEFT + 1.1*UP)

        line_1 = Line(LEFT, RIGHT, color="#F0E68C").set_width(text_2[1].get_width())
        line_1.next_to(text_2[1], DOWN, buff=0.2)
        line_2 = Line(LEFT, RIGHT, color="#EEE8AA").set_width(text_2[1].get_width()-.6)
        line_2.next_to(text_2[1], DOWN, buff=0.35)

        self.add(imo_logo, text_1, text_2, line_1, line_2)

if __name__ == '__main__':
    RUN(filepath, 'Thumbnail', '-spqk')