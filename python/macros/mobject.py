from manim import *

mobjs_dict = []

def add_dot(name, coord=ORIGIN, array=[None], color=None, label=None, scale_factor=.5, **kwargs):
	mobj = Dot(coord, **kwargs)
	if color:
		mobj.set_color(color)
	if array[0] == None:
		array = normalize(coord)
	if not label:
		label = f'${name}$'
	label = Tex(label).scale(scale_factor).next_to(mobj, array, .25*scale_factor)
	mobjs_dict.append({'name': name, 'type': 'Dot', 'mobj': mobj, 'coord': coord, 'label': label})

def add_line(name, line=[ORIGIN, RIGHT], color=None, array=[None], label=None, scale_factor=.5, **kwargs):
	mobj = Line(*line, **kwargs)
	if color:
		mobj.set_color(color)
	if array[0] != None:
		if not label:
			label = f'${name}$'
		label = Tex(label).scale(scale_factor).next_to(mobj, array, .25*scale_factor)
	else:
		label = None
	mobjs_dict.append({'name': name, 'type': 'Line', 'mobj': mobj, 'label': label})

def add_circle(name, center=ORIGIN, radius=1, point=[None], array=[None], label=None, scale_factor=.5, **kwargs):
	if point[0] != None:
		radius = np.linalg.norm(point - center)
	mobj = Circle(radius, **kwargs).move_to(center)
	if array[0] != None:
		if not label:
			label = f'${name}$'
		label = Tex(label).scale(scale_factor).next_to(mobj, array, .25*scale_factor)
	else:
		label = None
	mobjs_dict.append({'name': name, 'type': 'Circle', 'mobj': mobj, 'center': center, 'radius': radius, 'label': label})

def mobjs_of_type(mobjs_type=None):
	if mobjs_type:
		return [obj for obj in mobjs_dict if obj['type'] == mobjs_type]
	else:
		return mobjs_dict

def mobjs_lst(name, mobjs_type=None, args=['mobj', 'label']):
	mobjs = name.split(',')
	lst = mobjs_of_type(mobjs_type)
	if type(args) != list:
		args = [args]
	arg_lst = []
	for arg in args:
		if arg == 0:
			arg_lst += ['mobj']
		elif arg == 1:
			arg_lst += ['label']
		elif arg == 2:
			arg_lst += ['mobj', 'label']
		else:
			arg_lst += [arg]
	obj_lst = []
	for obj_name in mobjs:
		for obj in lst:
			if obj['name'] == obj_name:
				for i in arg_lst:
					try:
						if obj[i]:
							obj_lst += [obj[i]]
					except:
						if obj[i][0] != None:
							obj_lst += [obj[i]]
				break
	if len(obj_lst) == 1:
		obj_lst = obj_lst[0]
	return obj_lst

def vgroup(name, mobjs_type=None, args='mobj'):
	return VGroup(*mobjs_lst(name, mobjs_type, args))

def coord(name):
	return mobjs_lst(name, 'Dot', 'coord')

def dot(name, args=['mobj', 'label']):
	return mobjs_lst(name, 'Dot', args)
	
def line(name, args='mobj'):
	return mobjs_lst(name, 'Line', args)

def circle(name, args=['mobj', 'label']):
	return mobjs_lst(name, 'Circle', args)

# Some macros
def circumcenter(A, B, C):
	M, N = (A+B)/2, (B+C)/2
	P, Q = M + rotate_vector(A-M, PI/2), N + rotate_vector(B-N, PI/2)
	return line_intersection([M, P], [N, Q])
