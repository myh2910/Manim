import os, sys
filepath = os.path.realpath(__file__)
sys.path.append(os.path.dirname(os.path.dirname(filepath)))

from asymptote import *

class Video(Scene):
    def construct(self):
        self.add_sound("imo_2018_p1/audio.mp3")
        logo = ImageMobject('imo_2018_p1/imo_2018_logo.png')

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
            r"Sea $\Gamma$ la circunferencia circunscrita al tri\'angulo acut\'angulo $ABC$. Los puntos $D$ y $E$ est\'an en los segmentos $AB$ y $AC$, respectivamente, y son tales que $AD=AE$. Las mediatrices de $BD$ y $CE$ cortan a los arcos menores $AB$ y $AC$ de $\Gamma$ en los puntos $F$ y $G$, respectivamente. Demostrar que las rectas $DE$ y $FG$ son paralelas (o son la misma recta).",
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
        self.wait()

if __name__ == '__main__':
    RUN(filepath, 'Video', '-pqk -o IMO_2018_problema_1_yohan_min')