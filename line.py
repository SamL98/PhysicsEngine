from shape import Shape, BBox
from draw_util import is_viewable, get_drawing_coords
from numpy import inf
import numpy as np

class Line(Shape):
	def __init__(self, bbox, m, b, vel=[0.0, 0.0]):
		Shape.__init__(self, bbox, vel=vel)
		self.m = m
		self.b = b

"""
Create a line Shape object
:param pos: the top-left corner of the 
"""
def create_line(frm, to, vel=[0.0, 0.0]):
	t = min(frm[0], to[0])
	b = max(frm[0], to[0])
	l = min(frm[1], to[1])
	r = max(frm[1], to[1])
	bbox = BBox(t, l, b, r)

	if to[1] == frm[1]:
		slope = inf
		inter = inf
	else:
		slope = -(to[0]-frm[0])/(to[1]-frm[1])
		nice_slopes = np.arange(-2.0, 2.05, 0.05)
		slope_idx = np.argsort(np.abs(nice_slopes - slope))[0]

		nice_slopes = [-2.]
		while nice_slopes[-1] < 2.:
			nice_slopes.append(nice_slopes[-1] + .05)

		slope = nice_slopes[slope_idx]
		inter = frm[0] - slope*frm[1]

	return Line(bbox, slope, inter, vel=vel)

"""
Draw a line on the canvas
:param canvas: the canvas to draw on
:param bbox: the bounding box of the line
"""
def draw_line(canvas, bbox, m):
	if not is_viewable(bbox, canvas.shape):
		return

	center, t, l, b, r = get_drawing_coords(bbox, canvas.shape)

	if m == inf:
		canvas[t:b, l] = 0

	elif m == 0:
		canvas[t, l:r] = 0

	elif m > 0:
		i, j = b-1, l
		m_accum = 0
		while j < r:
			canvas[i, j] = 0
			i, j = i, j + 1

			m_accum -= m
			if abs(m_accum - int(m_accum)) < 1e-5:
				i += int(m_accum)
				m_accum = 0
			else:
				canvas[i+1, j-1] = 0
				canvas[i+1, j] = 0

	else:
		i, j = t, l
		m_accum = 0
		while j < r:
			canvas[i, j] = 0
			i, j = i, j + 1

			m_accum += m
			if abs(m_accum - int(m_accum)) < 1e-5:
				i -= int(m_accum)
				m_accum = 0