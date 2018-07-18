import numpy as np

"""
Clear the given canvas

:param canvas: numpy array to clear (set to 1)
"""
def clear(canvas):
	canvas[0:canvas.shape[0], 0:canvas.shape[1]] = 1

"""
Calculate the Euclidean distance between two points

:param p1: one point
:param p2: the other point
"""
def dist(p1, p2):
	return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

""" 
Return whether or not given bounding box is viewable in the canvas

:param bbox: the bounding box defining a shape
:param canvas_shape: the shape of the current canvas
"""
def is_viewable(bbox, canvas_shape):
	pos = (int(bbox.origin[0]), int(bbox.origin[1]))
	xInView = pos[0]<canvas_shape[0] and pos[0]+bbox.height/2>=0
	yInView = pos[1]<canvas_shape[1] and pos[1]+bbox.width/2>=0
	return xInView and yInView

"""
Return the bounding box of the part of the shape to draw
because some of the bounding box may be out of view.

:param bbox: the bounding box
:param canvas_shape: the shape of the current canvas
"""
def get_drawing_coords(bbox, canvas_shape):
	pos = (int(bbox.origin[0]), int(bbox.origin[1]))	
	center = (int(bbox.center[0]), int(bbox.center[1]))

	t = max(0, pos[0])
	b = min(canvas_shape[0], center[0]+bbox.height//2)
	l = max(0, pos[1])
	r = min(canvas_shape[1], center[1]+bbox.width//2)

	return center, t, l, b, r