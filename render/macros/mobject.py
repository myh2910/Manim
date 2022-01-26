from manim import *
from .constants import *

mobjs_dict = {}

def add_mobject(name, mobj, array=None, label=None, label_buff=BUFF, label_scale=LABEL_SCALE):
	"""Adds an Mobject to mobjs_dict."""
	if label != None:
		if label == 0:
			label = f"${name}$"
		label = Tex(label).scale(label_scale).next_to(mobj, array, label_buff * label_scale)
	mobjs_dict[name] = {"mobj": mobj, "label": label}

def add_dot(name, coord=ORIGIN, array=None, label=0, label_buff=BUFF, label_scale=LABEL_SCALE, **kwargs):
	"""Adds a Dot to mobjs_dict."""
	mobj = Dot(coord, **kwargs)
	try:
		if array == None:
			array = normalize(coord)
	except:
		if array[0] == None:
			array = normalize(coord)
	add_mobject(name, mobj, array, label, label_buff, label_scale)

def add_line(name, line=[ORIGIN, RIGHT], array=None, label=None, label_buff=BUFF, label_scale=LABEL_SCALE, **kwargs):
	"""Adds a Line to mobjs_dict."""
	mobj = Line(*line, **kwargs)
	add_mobject(name, mobj, array, label, label_buff, label_scale)

def add_doublearrow(name, line=[ORIGIN, RIGHT], pos=0, array=None, label=None, label_buff=BUFF, label_scale=LABEL_SCALE, **kwargs):
	"""Adds a DoubleArrow to mobjs_dict."""
	if pos == 0:
		mobj = DoubleArrow(*line, **kwargs)
	else:
		[A, B] = line
		mobj = DoubleArrow((pos + 1) * A - pos * B, (pos + 1) * B - pos * A, **kwargs)
	add_mobject(name, mobj, array, label, label_buff, label_scale)

def add_circle(name, center=ORIGIN, radius=1, point=None, array=None, label=None, label_buff=BUFF, label_scale=LABEL_SCALE, **kwargs):
	"""Adds a Circle to mobjs_dict."""
	try:
		if point != None:
			radius = np.linalg.norm(point - center)
	except:
		if point[0] != None:
			radius = np.linalg.norm(point - center)
	mobj = Circle(radius, **kwargs).move_to(center)
	add_mobject(name, mobj, array, label, label_buff, label_scale)

def def_angle(dots=[RIGHT, ORIGIN, UP], radius=.5, **kwargs):
	"""An Angle defined by the given arguments."""
	[A, B, C] = dots
	return Angle(Line(B, A), Line(B, C), radius, **kwargs)

def add_angle(name, dots=[RIGHT, ORIGIN, UP], radius=.5, array=None, label=None, label_buff=BUFF, label_scale=LABEL_SCALE, **kwargs):
	"""Adds an Angle to mobjs_dict."""
	mobj = def_angle(dots, radius, **kwargs)
	add_mobject(name, mobj, array, label, label_buff, label_scale)

def get_all(name):
	"""The "mobj" and "label" properties."""
	mobjs = name.split(",")
	obj_lst = []
	for i in mobjs:
		obj = mobjs_dict[i]
		obj_mobj, obj_label = obj["mobj"], obj["label"]
		obj_lst += [obj_mobj]
		if obj_label:
			obj_lst += [obj_label]
	if len(obj_lst) == 1:
		obj_lst = obj_lst[0]
	return obj_lst

def get_mobj(name):
	"""The "mobj" properties."""
	mobjs = name.split(",")
	obj_lst = [mobjs_dict[i]["mobj"] for i in mobjs]
	if len(obj_lst) == 1:
		obj_lst = obj_lst[0]
	return obj_lst

def get_label(name):
	"""The "label" properties."""
	mobjs = name.split(",")
	obj_lst = []
	for i in mobjs:
		obj_label = mobjs_dict[i]["label"]
		if obj_label:
			obj_lst += [obj_label]
	if len(obj_lst) == 1:
		obj_lst = obj_lst[0]
	return obj_lst

def get_coord(name):
	"""The coordinates of the given argument."""
	mobjs = name.split(",")
	obj_lst = [mobjs_dict[i]["mobj"].get_center() for i in mobjs]
	if len(obj_lst) == 1:
		obj_lst = obj_lst[0]
	return obj_lst

def get_vgroup(name, arg=0):
	"""VGroup of the given VMobjets."""
	mobjs = name.split(",")
	args = (["mobj"], ["label"], ["mobj", "label"])
	lst = args[arg]
	obj_lst = []
	for i in mobjs:
		obj = mobjs_dict[i]
		for prop in lst:
			try:
				if obj[prop]:
					obj_lst += [obj[prop]]
			except:
				if obj[prop][0] != None:
					obj_lst += [obj[prop]]
	return VGroup(*obj_lst)

# Some macros
def vector(name):
	coords = get_coord(name)
	return coords[1] - coords[0]

def modulo(name):
	"""The norm of the given vector."""
	return np.linalg.norm(vector(name))

def normal(name):
	"""The normalized vector of the given vector."""
	return normalize(vector(name))

def circumcenter(A, B, C):
	"""The circumcenter of the triangle formed by the given coordinates."""
	M, N = (A + B) / 2, (B + C) / 2
	P, Q = M + rotate_vector(A - M, PI / 2), N + rotate_vector(B - N, PI / 2)
	return line_intersection([M, P], [N, Q])
