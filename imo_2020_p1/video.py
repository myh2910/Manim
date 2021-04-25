import os, sys
filepath = os.path.realpath(__file__)
sys.path.append(os.path.dirname(os.path.dirname(filepath)))

from asymptote import *

class Video(Scene):
    def construct(self):
        problem = Tex(
            "\\textbf{Problema 1.} ",
            r"Considere el cuadril\'atero convexo $ABCD$. El punto $P$ est\'a en el interior de $ABCD$. Asuma las siguientes igualdades de razones: $$\angle PAD:\angle PBA:\angle DPA=1:2:3=\angle CBP:\angle BAP:\angle BPC.$$ Demuestre que las siguientes tres rectas concurren en un punto: la bisectriz interna del \'angulo $\angle ADP$, la bisectriz interna del \'angulo $\angle PCB$ y la mediatriz del segmento $AB$.",
            tex_environment=None,
            tex_template=TexTemplateLibrary.simple
        )
        problem.set_color_by_tex("Problema", RED)
        problem.scale(0.7).to_corner(UP)
        self.add(problem)

if __name__ == '__main__':
    RUN(filepath, 'Video', '-spqk')