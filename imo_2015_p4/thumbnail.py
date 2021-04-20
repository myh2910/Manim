from manim import *

class Thumbnail(Scene):
    def construct(self):
        text_1 = Tex("IMO 2015 ", "Problema 4")
        text_2 = Tex(r"Solución con \textsc{Manim}")

        text_1[0].set_color_by_gradient(BLUE_A, BLUE)
        text_1[1].set_color_by_gradient(RED_A, RED)
        text_2.set_color_by_gradient(GOLD_A, GOLD)
        text_1.scale(2.8)
        text_2.scale(2.8)
        VGroup(text_1, text_2).arrange(DOWN, buff=1)
        self.add(text_1, text_2)

if __name__ == '__main__':
    from subprocess import run
    run('manim imo_2015_p4/thumbnail.py Thumbnail -p')