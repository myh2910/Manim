import os, sys
filepath = os.path.realpath(__file__)
sys.path.append(os.path.dirname(os.path.dirname(filepath)))

from asymptote import *

class Thumbnail(Scene):
    def construct(self):
        t1 = Tex("IMO 2015 ", "Problema 4")
        t2 = Tex(r"Solución con \textsc{Manim}")

        t1[0].set_color_by_gradient(BLUE_A, BLUE)
        t1[1].set_color_by_gradient(RED_A, RED)
        t2.set_color_by_gradient(GOLD_A, GOLD)
        
        t1.scale(2.8)
        t2.scale(2.8)
        VGroup(t1, t2).arrange(DOWN, buff=1)

        self.add(t1, t2)

if __name__ == '__main__':
    RUN(filepath, 'Thumbnail', '-spqk -o Thumbnail')