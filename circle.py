from shape import Shape, BBox
from draw_util import is_viewable, get_drawing_coords, dist

class Circle(Shape):
	def __init__(self, bbox, rad, vel=[0.0, 0.0]):
		Shape.__init__(self, bbox, vel=vel)
		self.rad = rad

"""
Create a circle Shape object
:param pos: the top-left corner of the ball
:param rad: the radius of the ball
"""
def create_ball(pos=(0, 0), rad=10, vel=[0,0]):
	bbox = BBox(pos[0], pos[1], pos[0]+2*rad, pos[1]+2*rad)
	return Circle(bbox, rad, vel=vel)

"""
Draw a circle defined by the bounding box and radius on the canvas
:param canvas: canvas to draw on
:param bbox: BBox defining the position of the circle
:param rad: radius of the circle
"""
def draw_circle(canvas, bbox, rad):
	if not is_viewable(bbox, canvas.shape):
		return

	center, t, l, b, r = get_drawing_coords(bbox, canvas.shape)
	for i in range(t, b):
		for j in range(l, r):
			if dist((i, j), center) <= rad:
				canvas[i, j] = 0