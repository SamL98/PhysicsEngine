""" Functions for drawing shaped on a canvas """
from circle import Circle, draw_circle
from line import Line, draw_line

"""
Draw a shape on the canvas
:param canvas: canvas to draw on
:param shape: Shape to draw
"""
def draw_shape(canvas, shape):
	if type(shape) == Circle:
		draw_circle(canvas, shape.bbox, shape.rad)
	elif type(shape) == Line:
		draw_line(canvas, shape.bbox, shape.m)