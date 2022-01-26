from render.macros import *

class Video(Scene):
	def construct(self):
		t1 = Tex('IMO 2015, ', 'Problema 4')
		t1.set_color_by_tex_to_color_map({'IMO 2015, ': BLUE, 'Problema 4': RED}).scale(1.6)

		t2 = Tex(
			r'\textbf{Problema 4.} ',
			r"El triángulo $ABC$ tiene circunferencia circunscrita $\Omega$ y circuncentro $O$. Una circunferencia $\Gamma$ de centro $A$ corta al segmento $BC$ en los puntos $D$ y $E$ tales que $B$, $D$, $E$ y $C$ son todos diferentes y están en la recta $BC$ en este orden. Sean $F$ y $G$ los puntos de intersección de $\Gamma$ y $\Omega$, tales que $A$, $F$, $B$, $C$ y $G$ están sobre $\Omega$ en este orden. Sea $K$ el segundo punto de intersección de la circunferencia circunscrita al triángulo $BDF$ y el segmento $AB$. Sea $L$ el segundo punto de intersección de la circunferencia circunscrita al triángulo $CGE$ y el segmento $CA$." + LINEBREAK + \
			r"Supongamos que las rectas $FK$ y $GL$ son distintas y se cortan en el punto $X$. Demostrar que $X$ está en la recta $AO$.",
			tex_environment=None,
			tex_template=TexTemplateLibrary.simple
		)
		t2.set_color_by_tex('Problema', RED)

		t3 = Tex(
			r"\hphantom{\textbf{Problema 4.} }El triángulo $ABC$ tiene circunferencia circunscrita $\Omega$ y circuncentro $O$. Una circunferencia $\Gamma$ de centro $A$ corta al segmento $BC$ en los puntos $D$ y $E$ tales que $B$, $D$, $E$ y $C$ son todos diferentes y están en la recta $BC$ en este orden. Sean $F$ y $G$ los puntos de intersección de $\Gamma$ y $\Omega$, tales que $A$, $F$, $B$, $C$ y $G$ están sobre $\Omega$ en este orden. Sea $K$ el segundo punto de intersección de la circunferencia circunscrita al triángulo $BDF$ y el segmento $AB$. Sea $L$ el segundo punto de intersección de la circunferencia circunscrita al triángulo $CGE$ y el segmento $CA$." + LINEBREAK + \
			r"Supongamos que las rectas $FK$ y $GL$ son distintas y se cortan en el punto $X$. Demostrar que $X$ está en la recta $AO$.",
			tex_environment=None,
			tex_template=TexTemplateLibrary.simple
		)
		for item in [t2, t3]:
			item.scale(.7).to_corner(UP)

		t5 = MathTex(
			# 0    1    2    3    4    5    6    7    8    9   10   11
			ITEM, 'A', 'D', '=', 'A', 'E', '=', 'A', 'F', '=', 'A', 'G' + LINEBREAK,
			#12   13   14   15   16   17
			ITEM, 'B', 'D', 'K', 'F', IS_CYCLIC + LINEBREAK,
			#18   19   20   21   22   23
			ITEM, 'C', 'G', 'L', 'E', IS_CYCLIC + LINEBREAK,
			#             24   25   26   27   28   29   30
			ITEM + PROVE_THAT, 'A', ',', 'X', ',', 'O', ARE_COLLINEAR,
			tex_environment='align*',
			tex_template=TexTemplateLibrary.simple
		)
		t6 = MathTex(
			# 0    1    2    3    4    5
			'&A', ',', 'X', ',', 'O', ARE_COLLINEAR + LINEBREAK,
			#6    7                              8    9   10
			IFF, 'X', BELONGS_TO('la mediatriz de'), 'F', 'G' + LINEBREAK,
			#11   12    13   14   15   16     17   18   19   20
			IFF, ANGLE, 'K', 'F', 'G', '=', ANGLE, 'L', 'G', 'F',
			tex_environment='align*',
			tex_template=TexTemplateLibrary.simple
		)
		t7 = MathTex(
			ITEM + 'AD=AE=AF=AG' + LINEBREAK + \
			ITEM + 'BDKF' + IS_CYCLIC + LINEBREAK + \
			ITEM + 'CGLE' + IS_CYCLIC + LINEBREAK + \
			#              0    1      2    3    4    5      6    7    8    9
			ITEM + PROVE_THAT, ANGLE, 'K', 'F', 'G', '=', ANGLE, 'L', 'G', 'F',
			tex_environment='align*',
			tex_template=TexTemplateLibrary.simple
		)
		t8 = MathTex(
			ITEM + 'AD=AE=AF=AG' + LINEBREAK + \
			ITEM + 'BDKF' + IS_CYCLIC + LINEBREAK + \
			ITEM + 'CGLE' + IS_CYCLIC + LINEBREAK + \
			#              0    1    2    3
			ITEM + PROVE_THAT, 'x', '=', 'y',
			tex_environment='align*',
			tex_template=TexTemplateLibrary.simple
		)
		t9 = MathTex(
			#0    1    2     3    4    5    6
			'C', '-', 'x', '&=', 'C', '-', r'y \\ ',
			#7     8    9
			'x', '&=', 'y',
			tex_environment='align*',
			tex_template=TexTemplateLibrary.simple
		)
		for item in [t5, t6, t7, t8]:
			item.set_color(WHITE).scale(.6)
		t5.shift(4*RIGHT)
		for item in [t6, t7, t8]:
			item.move_to(t5, aligned_edge=LEFT)
		t9.move_to(t5)

		plane = PolarPlane()
		plane_scale_factor = 3.3
		for name, angle, array in [('A', 110, UP), ('B', 200, None), ('C', 340, None)]:
			add_dot(name, plane.pr2pt(plane_scale_factor, angle*DEGREES), array)

		add_dot('O', ORIGIN, DOWN)
		add_circle('omega', radius=plane_scale_factor, array=UP, label=r'$\Omega$', color=BLUE)

		[A, B, C] = get_coord('A,B,C')
		for line_label in ['AB', 'BC', 'CA']:
			add_line(line_label, get_coord('{},{}'.format(*line_label)), color=RED)

		for label, axis in [('D', .3), ('E', -.3)]:
			add_dot(label, (1-axis)*get_mobj('BC').get_projection(A) + axis*B, DOWN)

		circle_radius = modulo('A,D')
		add_circle('gamma', A, circle_radius, array=RIGHT, label=r'$\Gamma$', color=GREEN)

		rotate_by_angle = 2*np.arcsin(circle_radius/(2*plane_scale_factor))
		for dot1, axis, dot2, dot3, dot4, line_label, dot5 in [
			('F', 1, 'B', 'D', 'F', 'AB', 'K'), ('G', -1, 'C', 'G', 'E', 'CA', 'L')
		]:
			add_dot(dot1, rotate_vector(A, axis*rotate_by_angle), axis*LEFT)
			center = circumcenter(*get_coord(f'{dot2},{dot3},{dot4}'))
			ref_dot = get_coord(dot2)
			add_circle(f'{dot2}{dot3}{dot4}', center, point=ref_dot, color=GREEN)
			add_dot(dot5, 2*get_mobj(line_label).get_projection(center) - ref_dot, None)

		add_dot('X', line_intersection(*[get_coord('{},{}'.format(*i)) for i in ['FK', 'GL']]), DOWN)
		for label in 'FG':
			line_label = label + 'X'
			add_line(line_label, get_coord(f'{label},X'), color=GREEN)
			add_mobject(f'dashed_{line_label}', DashedVMobject(get_all(line_label)))
			add_line('A' + label, [A, get_coord(label)], color=PURPLE)

		shift_right_by, shift_left_by = 3.5, 3
		for shift_by, lst in [
			(shift_right_by, get_all('omega,AB,BC,CA,O,A,B,C')),
			(-shift_left_by, get_all('BDF,CGE,FX,GX,dashed_FX,dashed_GX,AF,AG,K,L,X'))
		]:
			for obj in lst:
				obj.shift(shift_by*RIGHT)

		self.add_sound('assets/2015_4.mp3')

		self.play(Write(t1), run_time=4)
		self.wait()
		self.play(FadeOut(t1), TransformFromCopy(t1[1], t2[0]))
		self.play(Create(t3), run_time=4)
		self.wait(4)
		self.play(VGroup(t2[0], t3).animate.scale(.5).shift(UP + 3.5*LEFT))

		for i in get_all('O'):
			self.play(GrowFromCenter(i))
		self.add_foreground_mobjects(*get_all('O'))
		for i in get_all('omega'):
			self.play(GrowFromCenter(i))
		self.add_foreground_mobject(get_label('omega'))

		self.play(GrowFromCenter(get_vgroup('A,B,C')))
		self.play(*[GrowFromCenter(i) for i in get_label('A,B,C')])
		self.add_foreground_mobjects(*get_all('A,B,C'))
		self.play(Create(get_vgroup('AB,BC,CA')))

		change_1 = get_vgroup('omega,AB,BC,CA,O,A,B,C') + get_vgroup('omega,O,A,B,C', 1)
		self.play(FadeOut(VGroup(t2[0], t3)))
		self.play(change_1.animate.shift(shift_right_by*LEFT), run_time=2)

		for i in [*get_all('gamma'), get_vgroup('F,D,E,G')]:
			self.play(GrowFromCenter(i))
		self.play(*[GrowFromCenter(i) for i in get_label('F,D,E,G')])
		self.add_foreground_mobjects(*get_all('F,D,E,G'))

		self.play((change_1 + get_vgroup('gamma,F,D,E,G', 2)).animate.shift(shift_left_by*LEFT))
		self.play(get_vgroup('F,D,E,G').animate.set_color(ORANGE))

		for idx, mobj in enumerate(get_label('D,E,F,G')):
			j = 3*idx
			self.play(
				Write(t5[j]),
				*[TransformFromCopy(obj, t5[j+i]) for i, obj in [(1, get_label('A')), (2, mobj)]],
				run_time=2
			)
		self.play(
			FadeOut(*get_all('gamma')),
			*[i.animate.set_color(WHITE) for i in [t5[:12], *get_mobj('F,D,E,G')]]
		)
		for i in get_all('BDF,K'):
			self.play(GrowFromCenter(i))
		self.add_foreground_mobjects(*get_all('K'))

		self.play(get_vgroup('K,B,D,F').animate.set_color(ORANGE))
		self.play(
			Write(t5[12]),
			*[TransformFromCopy(obj, t5[i+13]) for i, obj in enumerate(get_label('B,D,K,F'))],
			run_time=2
		)
		self.play(Write(t5[17]))
		self.play(FadeOut(get_all('BDF')))
		self.play(*[i.animate.set_color(WHITE) for i in [t5[12:18], *get_mobj('K,B,D,F')]])

		for i in get_all('CGE,L'):
			self.play(GrowFromCenter(i))
		self.add_foreground_mobjects(*get_all('L'))

		self.play(get_vgroup('L,C,G,E').animate.set_color(ORANGE))
		self.play(
			Write(t5[18]),
			*[TransformFromCopy(obj, t5[i+19]) for i, obj in enumerate(get_label('C,G,L,E'))],
			run_time=2
		)
		self.play(Write(t5[23]))
		self.play(FadeOut(get_all('CGE')))
		self.play(*[i.animate.set_color(WHITE) for i in [t5[18:24], get_vgroup('L,C,G,E')]])

		self.play(Create(get_vgroup('FX,GX')), run_time=2)
		for i in get_all('X'):
			self.play(GrowFromCenter(i))
		self.add_foreground_mobjects(*get_all('X'))
		self.play(ReplacementTransform(get_vgroup('FX,GX'), get_vgroup('dashed_FX,dashed_GX')))

		self.play(get_vgroup('A,X,O').animate.set_color(ORANGE))
		self.play(
			Write(t5[24]),
			*[anim for i, obj in enumerate(get_label('A,X,O')) for anim in [
				TransformFromCopy(obj, t5[2*i+25]), Write(t5[2*i+26])
			]], run_time=2
		)
		self.play(*[i.animate.set_color(WHITE) for i in [t5[24:], get_vgroup('A,X,O')]])
		self.wait()
		self.play(Create(get_vgroup('AF,AG')))

		change_2 = [get_vgroup('AB,BC,CA'), *get_all('B,C,D,E')]
		self.play(*[FadeOut(i) for i in [*change_2, get_label('omega')]])

		rotate_by = angle_of_vector(vector('F,G'))
		self.play(
			Rotate(get_vgroup('dashed_FX,dashed_GX,AF,AG,A,F,G,X,K,L'), rotate_by, IN, get_coord('O')),
			UpdateFromFunc(get_label('A'), lambda m: m.next_to(get_mobj('A'), UP, LABEL_BUFF)),
			UpdateFromFunc(get_label('F'), lambda m: m.next_to(get_mobj('F'), LEFT, LABEL_BUFF)),
			UpdateFromFunc(get_label('G'), lambda m: m.next_to(get_mobj('G'), RIGHT, LABEL_BUFF)),
			UpdateFromFunc(get_label('K'), lambda m: m.next_to(get_mobj('K'), normal('O,K'), LABEL_BUFF)),
			UpdateFromFunc(get_label('L'), lambda m: m.next_to(get_mobj('L'), normal('O,L'), LABEL_BUFF)),
			UpdateFromFunc(get_label('X'), lambda m: m.next_to(get_mobj('X'), DOWN, LABEL_BUFF)),
			run_time=2
		)
		for i in 'FG':
			add_line('O' + i, get_coord('O,' + i), color=RED)
		self.play(Create(get_vgroup('OF,OG')))

		self.play(FadeOut(get_mobj('omega')))

		add_doublearrow('dOA', get_coord('O,A'), pos=.26, color=BLUE, stroke_width=4, tip_length=.2)
		for label, angle in [('A', 135), ('O', 225), ('X', 267)]:
			add_dot(f'{label}1', get_coord(label), plane.pr2pt(1, angle*DEGREES), f'${label}$')

		self.play(
			CounterclockwiseTransform(*get_label('A,A1'), float=SMALL_RADIUS),
			*[ClockwiseTransform(*get_label(f'{i},{i}1'), float=SMALL_RADIUS) for i in 'OX']
		)
		self.play(Create(get_mobj('dOA')), run_time=2)

		add_mobject('tFG', Tex('Mediatriz de $FG$').scale(.5).next_to(get_coord('O') + .1*RIGHT + .3*DOWN))
		self.play(Write(get_mobj('tFG')))
		self.wait()

		self.play(FadeOut(t5), *[TransformFromCopy(t5[i+25], t6[i]) for i in range(6)])
		self.play(Write(t6[6]))
		self.play(
			*[TransformFromCopy(get_label(obj), t6[i]) for obj, i in [('X', 7), ('F', 9), ('G', 10)]],
			Write(t6[8]),
			run_time=2
		)
		for label, direction in [('A', UP), ('O', DOWN), ('X', DOWN)]:
			add_dot(f'{label}1', get_coord(label), direction, f'${label}$')

		self.play(FadeOut(*get_mobj('dOA,tFG')))
		self.play(
			ClockwiseTransform(*get_label('A,A1'), float=SMALL_RADIUS),
			*[CounterclockwiseTransform(*get_label(f'{i},{i}1'), float=SMALL_RADIUS) for i in 'OX']
		)
		self.play(*[FadeOut(i) for i in get_all('A,O,AF,AG,OF,OG')])
		add_line('FG', get_coord('F,G'), color=GREEN)
		self.play(Create(get_mobj('FG')))

		for name, objs in [('aGFK', 'G,F,X'), ('aLGF', 'X,G,F')]:
			for i in range(2):
				add_angle(name + str(i), get_coord(objs), .5-.125*i, color=PURPLE)
			add_mobject(name, get_vgroup(f'{name}0,{name}1'))
		self.bring_to_back(*get_mobj('aGFK,aLGF'))
		self.play(*[Create(get_mobj(i)) for i in ['aGFK', 'aLGF']])

		for i, j in [('F', 'K'), ('G', 'L')]:
			add_line(i + j, get_coord(i + ',' + j), color=GREEN)

		self.play(Write(t6[11]))
		self.play(
			Write(t6[12]),
			*[TransformFromCopy(obj, t6[i+13]) for i, obj in enumerate(get_label('K,F,G'))],
			run_time=2
		)
		self.play(
			Write(t6[16:18]),
			*[TransformFromCopy(obj, t6[i+18]) for i, obj in enumerate(get_label('L,G,F'))],
			run_time=2
		)
		self.play(
			*[ReplacementTransform(*get_mobj(f'dashed_{i}')) for i in ['FX,FK', 'GX,GL']],
			*[FadeOut(i) for i in get_all('X')],
			run_time=2
		)
		self.play(FadeOut(t6[:12]))
		self.play(
			Write(t7[0]), *[ReplacementTransform(t6[i+12], t7[i+1]) for i in range(9)],
			run_time=2
		)
		self.play(
			Rotate(get_vgroup('aGFK,aLGF,FG,FK,GL,K,L,F,G'), rotate_by, OUT, get_coord('O')),
			UpdateFromFunc(get_label('F'), lambda m: m.next_to(get_mobj('F'), LEFT, LABEL_BUFF)),
			UpdateFromFunc(get_label('G'), lambda m: m.next_to(get_mobj('G'), RIGHT, LABEL_BUFF)),
			UpdateFromFunc(get_label('K'), lambda m: m.next_to(get_mobj('K'),  normal('O,K'), LABEL_BUFF)),
			UpdateFromFunc(get_label('L'), lambda m: m.next_to(get_mobj('L'), normal('O,L'), LABEL_BUFF))
		)
		get_vgroup('A,dOA').rotate(rotate_by, about_point=get_coord('O'))
		get_label('A').next_to(get_mobj('A'), UP, LABEL_BUFF)

		self.add_foreground_mobjects(*(get_mobj('aGFK,aLGF,FG,FK,GL,K,L,F,G,A,B,O,D,E') + get_label('B,C,D,E')))
		self.play(*[FadeIn(i) for i in get_all('O,A,omega') + change_2])
		self.wait()
		self.play(*[ReplacementTransform(obj, t8[i+1]) for i, obj in enumerate(
			[t7[1:5], t7[5], t7[6:]]
		)])
		add_line('GF', get_coord('G,F'))
		for i, objs in [('x', 'FG,FK'), ('y', 'GL,GF')]:
			add_mobject('t' + i, Tex(f'${i}$').scale(LABEL_SCALE).move_to(Angle(*get_mobj(objs), .7)))

		for name, objs in [('aGFK1', 'G,F,K'), ('aLGF1', 'L,G,F')]:
			add_angle(name, get_coord(objs), .5)
		self.play(
			*[Transform(*get_mobj(f'{obj},{obj}1')) for obj in ['aGFK', 'aLGF']],
			*[TransformFromCopy(t8[i], get_mobj(obj)) for i, obj in [(1, 'tx'), (3, 'ty')]],
			run_time=2
		)
		get_mobj('tFG').shift(.42*DOWN + .05*RIGHT)

		for label, angle in [('A', 159), ('O', 225)]:
			add_dot(label + '1', get_coord(label), plane.pr2pt(1, angle*DEGREES + rotate_by), f'${label}$')
		self.play(
			CounterclockwiseTransform(*get_label('A,A1'), float=SMALL_RADIUS),
			ClockwiseTransform(*get_label('O,O1'), float=SMALL_RADIUS)
		)
		self.play(Create(get_mobj('dOA')), run_time=2)
		self.play(Write(get_mobj('tFG')))

		for label, direction in [('A', UP), ('O', DOWN)]:
			add_dot(label + '1', get_coord(label), direction, f'${label}$')
		add_line('OA', get_coord('O,A'), color=PURPLE)

		add_mobject('aOA_GF', RightAngle(*get_mobj('OA,GF'), .2))
		self.bring_to_back(get_mobj('aOA_GF'))
		self.play(Create(get_mobj('aOA_GF')))
		self.wait()

		self.play(FadeOut(get_mobj('tFG')), ReplacementTransform(*get_mobj('dOA,OA')))
		self.play(
			ClockwiseTransform(*get_label('A,A1'), float=SMALL_RADIUS),
			CounterclockwiseTransform(*get_label('O,O1'), float=SMALL_RADIUS)
		)
		add_mobject('tC', Tex('$C$').scale(LABEL_SCALE).move_to(Angle(*get_mobj('CA,BC'), .8, (1, -1))))

		add_angle('aACB', get_mobj('A,C,B'))
		self.bring_to_back(get_mobj('aACB'))
		self.play(Create(get_mobj('aACB')), TransformFromCopy(get_label('C'), get_mobj('tC'), run_time=2))

		change_3 = get_mobj('aGFK,aLGF,aOA_GF,FK,GL,FG,tx,ty') + get_all('D,E,F,K,G,L')
		add_line('OB', get_coord('O,B'), color=PURPLE)
		self.play(*[FadeOut(i) for i in change_3], Create(get_mobj('OB')))
		add_mobject('aAOB', Angle(*get_mobj('OA,OB'), .35))
		self.bring_to_back(get_mobj('aAOB'))

		add_mobject('t2C', Tex('$2C$').scale(LABEL_SCALE).move_to(Angle(*get_mobj('OA,OB'), .9)))
		self.play(Create(get_mobj('aAOB')), TransformFromCopy(*get_mobj('tC,t2C')), run_time=2)

		for name, objs in [('aBAO', 'B,A,O'), ('aOBA', 'O,B,A')]:
			add_angle(name, get_coord(objs))
		self.bring_to_back(*get_mobj('aBAO,aOBA'))

		for name, objs, axis in [('tC1', 'AB,OA', (1, -1)), ('tC2', 'OB,AB', (-1, -1))]:
			add_mobject(name, Tex('$90-C$').scale(LABEL_SCALE).move_to(Angle(*get_mobj(objs), 1.4, axis)))
		self.play(
			*[Create(get_mobj(i)) for i in ['aBAO', 'aOBA']],
			*[TransformFromCopy(*get_mobj(f't2C,tC{i+1}')) for i in range(2)],
			run_time=2
		)
		self.play(FadeOut(*get_mobj('aAOB,aOBA,OB,t2C,tC2')))
		self.wait()

		self.bring_to_back(get_mobj('aOA_GF'))
		self.play(*[FadeIn(i) for i in change_3])

		add_mobject('aFG_AB', Angle(*get_mobj('FG,AB'), .85, (1, -1)))
		add_mobject('tC3', Tex('$C$').scale(LABEL_SCALE).move_to(Angle(*get_mobj('FG,AB'), 1.2, (1, -1))))
		self.bring_to_back(get_mobj('aFG_AB'))
		self.play(TransformFromCopy(*get_mobj('tC1,tC3')), Create(get_mobj('aFG_AB')), run_time=2)
		self.wait()

		get_mobj('BDF').set_color(ORANGE)
		self.bring_to_back(get_mobj('BDF'))
		self.play(GrowFromCenter(get_mobj('BDF')))

		circle_center = circumcenter(*get_coord('B,D,F'))
		for obj, axis in [('F', LEFT), ('K', UP), ('D', [None]), ('B', [None])]:
			angle = angle_of_vector(get_coord(obj) - circle_center)
			if axis[0] == None:
				axis = plane.pr2pt(1, angle)
			add_dot(f'{obj}1', plane.pr2pt(plane_scale_factor, angle) + shift_left_by*LEFT, axis, f'${obj}$')
		ref_angle = angle_of_vector(2*get_mobj('FG').get_projection(circle_center) - get_coord('F') - circle_center)
		add_dot('r1', plane.pr2pt(plane_scale_factor, ref_angle) + shift_left_by*LEFT, label=None)

		add_mobject('BDF1', get_mobj('omega').copy().set_color(ORANGE))

		for objs, color in [
			([('KB1', 'K1,B1'), ('BD1', 'B1,D1')], RED), ([('FK1', 'F1,K1'), ('FG1', 'F1,r1')], GREEN)
		]:
			for name, coords in objs:
				add_line(name, get_coord(coords), color=color)

		for name1, name2, label, line, axis in [
			('aFG_AB1', 'tC_1', '$C$', 'KB1', (1, -1)), ('aGFK1', 'tx1', '$x$', 'FK1', (1, 1))
		]:
			objs = get_mobj(f'FG1,{line}')
			add_mobject(name1, Angle(*objs, .5, axis))
			add_mobject(name2, Tex(label).scale(LABEL_SCALE).move_to(Angle(*objs, .9, axis)))

		self.add_foreground_mobjects(*get_mobj('C,E,G,F1,K1,D1,B1,r1'))
		self.play(
			*[FadeOut(i) for i in get_all(
				'aLGF,aACB,aBAO,aOA_GF,aFG_AB,aGFK,omega,AB,BC,CA,OA,FK,GL,FG,O,A,B,C,D,E,F,G,K,L,ty,tC,tC1,tC3,tx'
			)],
			ReplacementTransform(*get_mobj('BDF,BDF1')),
			*[TransformFromCopy(*args) for args in list(zip(
				get_all('aFG_AB,aGFK,AB,BC,FK,FG,F,K,D,B,tC3,tx'),
				get_all('aFG_AB1,aGFK1,KB1,BD1,FK1,FG1,F1,K1,D1,B1,tC_1,tx1')
			))],
			GrowFromCenter(get_mobj('r1'))
		)
		add_angle('aFKB1', get_coord('F1,K1,B1'))
		add_mobject('tC-x', MathTex('C', '-', 'x').scale(LABEL_SCALE).move_to(
			Angle(*get_mobj('FK1,KB1'), .9, (-1, 1))
		))
		self.bring_to_back(get_mobj('aFKB1'))
		self.play(
			*[TransformFromCopy(i, get_mobj('tC-x')[2*idx]) for idx, i in enumerate(get_mobj('tC_1,tx1'))],
			Write(get_mobj('tC-x')[1]),
			Create(get_mobj('aFKB1')),
			run_time=2
		)
		self.play(FadeOut(*get_mobj('aFG_AB1,aGFK1,tC_1,tx1,FG1'), get_label('K1')), FadeOut(get_mobj('r1')))

		alpha = angle_between_vectors(vector('O,K1'), vector('O,D1'))
		add_mobject('tC-x1', get_mobj('tC-x').copy().move_to(def_angle(get_coord('F1,D1,B1'), 1.2)))
		self.add_foreground_mobjects(*get_mobj('F1,B1,D1,K1'))
		self.bring_to_back(get_mobj('aFKB1'))

		alpha_tracker = ValueTracker(alpha)
		get_mobj('K1').add_updater(lambda m: m.become(
			get_mobj('D1').copy().rotate(alpha_tracker.get_value(), about_point=get_coord('O'))
		))
		get_mobj('aFKB1').add_updater(lambda m: m.become(def_angle([
			get_coord('F1'), rotate_vector(vector('O,D1'),
			alpha_tracker.get_value()) + get_coord('O'),
			get_coord('B1')
		])))
		get_mobj('FK1').add_updater(lambda m: m.become(Line(
			get_coord('F1'),
			rotate_vector(vector('O,D1'), alpha_tracker.get_value()) + get_coord('O'),
			color=GREEN
		)))
		get_mobj('KB1').add_updater(lambda m: m.become(Line(
			rotate_vector(vector('O,D1'),
			alpha_tracker.get_value()) + get_coord('O'), get_coord('B1'),
			color=RED
		)))
		self.play(
			alpha_tracker.animate.set_value(0),
			ClockwiseTransform(*get_mobj('tC-x,tC-x1'), path_arc=-alpha),
			run_time=2
		)
		for obj in get_mobj('K1,aFKB1,FK1,KB1'):
			obj.clear_updaters()
		self.remove(*get_mobj('KB1,K1'))
		self.add_foreground_mobjects(*get_mobj('C,E'))

		beta = 120*DEGREES
		beta_tracker = ValueTracker(0)
		get_mobj('aFKB1').add_updater(lambda m: m.become(def_angle(get_coord('F1,D1,B1'))))
		get_mobj('FK1').add_updater(lambda m: m.become(Line(*get_coord('F1,D1'), color=GREEN)))
		get_mobj('tC-x').add_updater(lambda m: m.move_to(
			def_angle(get_coord('F1,D1,B1'), 1.2 - beta_tracker.get_value()*(.15)/beta)
		))
		self.play(
			*[ReplacementTransform(*args) for args in list(zip(get_all('BD1,F1,D1,B1'), get_all('BC,F,D,B')))],
			FadeOut(get_mobj('BDF1')),
			FadeIn(*get_all('aLGF,aACB,omega,CA,GL,FG,A,C,E,G,L,ty,tC')),
			beta_tracker.animate.set_value(beta)
		)
		self.wait()

		for obj in get_mobj('aFKB1,FK1,tC-x'):
			obj.clear_updaters()

		get_mobj('CGE').set_color(ORANGE)
		self.bring_to_back(get_mobj('CGE'))
		self.play(GrowFromCenter(get_mobj('CGE')))

		circle_center = circumcenter(*get_coord('C,G,E'))
		for obj in 'ELGC':
			angle = angle_of_vector(get_coord(obj) - circle_center)
			add_dot(
				f'{obj}1',
				plane.pr2pt(plane_scale_factor, angle) + shift_left_by*LEFT,
				plane.pr2pt(1, angle),
				f'${obj}$'
			)
		ref_angle = angle_of_vector(
			2*get_mobj('FG').get_projection(circle_center) - get_coord('G') - circle_center
		)
		add_dot('r1', plane.pr2pt(plane_scale_factor, ref_angle) + shift_left_by*LEFT, label=None)

		add_mobject('CGE1', get_mobj('omega').copy().set_color(ORANGE))

		for objs, color in [
			([('CL1', 'C1,L1'), ('EC1', 'E1,C1')], RED), ([('GL1', 'G1,L1'), ('FG1', 'r1,G1')], GREEN)
		]:
			for name, coords in objs:
				add_line(name, get_coord(coords), color=color)

		for name1, name2, label, line1, line2, radius in [
			('aACB1', 'tC1', '$C$', 'CL1', 'EC1', .9), ('aLGF1', 'ty1', '$y$', 'GL1', 'FG1', .8)
		]:
			objs = get_mobj(f'{line1},{line2}')
			add_mobject(name1, Angle(*objs, .5, (1, -1)))
			add_mobject(name2, Tex(label).scale(LABEL_SCALE).move_to(Angle(*objs, radius, (1, -1))))

		self.add_foreground_mobjects(*get_mobj('r1,A,B,F,D'))
		self.play(
			*[FadeOut(i) for i in get_all(
				'aFKB1,aACB,aLGF,omega,BC,CA,GL,FG,FK1,A,B,C,D,E,F,G,L,ty,tC,tC-x'
			)],
			ReplacementTransform(*get_mobj('CGE,CGE1')),
			*[TransformFromCopy(*args) for args in list(zip(
				get_all('aACB,aLGF,CA,BC,GL,FG,G,L,E,C,tC,ty'),
				get_all('aACB1,aLGF1,CL1,EC1,GL1,FG1,G1,L1,E1,C1,tC1,ty1')
			))],
			GrowFromCenter(get_mobj('r1'))
		)
		theta = angle_between_vectors(vector('O,G1'), vector('O,C1'))
		add_mobject('tC_1', get_mobj('tC1').copy().move_to(Angle(*get_mobj('GL1,FG1'), 1.5, (1, -1))))
		self.add_foreground_mobjects(*get_mobj('G1,C1,E1,L1'))
		self.bring_to_back(get_mobj('aACB1'))

		theta_tracker = ValueTracker(theta)
		get_mobj('C1').add_updater(lambda m: m.become(
			get_mobj('G1').copy().rotate(theta_tracker.get_value(), IN, about_point=get_coord('O'))
		))
		get_mobj('aACB1').add_updater(lambda m: m.become(def_angle(
			[
				get_coord('L1'),
				rotate_vector(vector('O,G1'),
				theta_tracker.get_value(), IN) + get_coord('O'),
				get_coord('E1')
			],
			.5+.7*(1-theta_tracker.get_value()/theta)
		)))
		get_mobj('CL1').add_updater(lambda m: m.become(Line(
			rotate_vector(vector('O,G1'), theta_tracker.get_value(), IN) + get_coord('O'),
			get_coord('L1'),
			color=RED
		)))
		get_mobj('EC1').add_updater(lambda m: m.become(Line(
			get_coord('E1'),
			rotate_vector(vector('O,G1'), theta_tracker.get_value(), IN) + get_coord('O'),
			color=RED
		)))
		self.play(FadeOut(get_label('C1')))
		self.play(
			theta_tracker.animate.set_value(0),
			CounterclockwiseTransform(*get_mobj('tC1,tC_1'), path_arc=theta),
			run_time=2
		)
		for obj in get_mobj('C1,aACB1,CL1,EC1'):
			obj.clear_updaters()
		self.remove(*get_mobj('CL1,C1'))

		add_angle('aFGE1', get_coord('r1,G1,E1'), 1.9)
		add_mobject('tC-y', MathTex('C', '-', 'y').scale(LABEL_SCALE).move_to(
			Angle(*get_mobj('FG1,EC1'), 2.4, (-1, -1))
		))
		self.bring_to_back(get_mobj('aFGE1'))

		self.play(
			*[TransformFromCopy(i, get_mobj('tC-y')[2*idx]) for idx, i in enumerate(get_mobj('tC_1,ty1'))],
			Write(get_mobj('tC-y')[1]),
			Create(get_mobj('aFGE1')),
			run_time=2
		)
		self.play(FadeOut(*get_mobj('aACB1,aLGF1,tC_1,ty1,GL1'), get_label('L1')), FadeOut(get_mobj('L1')))

		add_angle('aFGE', get_coord('F,G,E'), .7)
		add_line('EG', get_coord('E,G'), color=GREEN)
		self.add_foreground_mobjects(*get_mobj('tC-y,F'))

		self.play(
			*[ReplacementTransform(*args) for args in list(zip(
				get_all('aFGE1,FG1,EC1,G1,E1'), get_all('aFGE,FG,EG,G,E')
			))],
			get_mobj('tC-y').animate.move_to(Angle(*get_mobj('FG,EG'), 1.8, (-1, -1))),
			*[FadeOut(i) for i in get_mobj('CGE1,r1')],
			FadeIn(*get_all('aFKB1,BC,FK1,A,B,C,D,F,tC-x'))
		)
		self.wait()

		get_mobj('gamma').set_color(BLUE)
		self.add_foreground_mobjects(*get_mobj('D,E,G,tC-x'))
		for i, j in list(zip(get_all('gamma'), [2, 1])):
			self.play(GrowFromCenter(i), run_time=j)

		self.play(FadeOut(t7, t8))
		self.play(
			*[TransformFromCopy(t[i], t9[4*j+i]) for j, t in enumerate(get_mobj('tC-x,tC-y')) for i in range(3)],
			Write(t9[3]),
			run_time=2
		)
		self.wait()

		self.play(*[t.animate.set_color(DARK_GRAY) for t in [t9[:2], t9[4:6]]])
		self.play(*[TransformFromCopy(t9[i], t9[j]) for i, j in [(2, 7), (6, 9)]], Write(t9[8]), run_time=2)
		for color in [YELLOW, WHITE]:
			self.play(Circumscribe(t9[7:10]), t9[7:10].animate.set_color(color))
		self.wait()

		self.play(*[FadeOut(obj, shift=DOWN) for obj in self.mobjects])

		ending_credit = Tex('Video hecho con ', r'\textsc{Manim}')
		ending_credit.scale(1.5)
		ending_credit[1].set_color_by_gradient(BLUE_B, BLUE_E)
		for i in range(2):
			self.play(Write(ending_credit[i]))
		self.wait()
		self.play(FadeOut(ending_credit, shift=DOWN))
		self.wait()
