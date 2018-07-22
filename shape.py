import numpy as np

""" Class to hold the bounding box of a drawn object """
class BBox(object):
	"""
	:param t: coordinate of the top of the box
	:param b: bottom of the box
	:param l: left of the box
	:param r: right of the box
	"""
	def __init__(self, t, l, b, r):
		self.origin = (t, l)
		self.width = r-l
		self.height = b-t
		self.center = (t+self.height/2, l+self.width/2)
		self.size = (self.height, self.width)
		self.br = (b, r)
		self.t = t
		self.b = b
		self.l = l
		self.r = r

	""" String representation """
	def __str__(self):
		return '[' + ','.join([str(d) for d in [self.t, self.l, self.b, self.r]]) + ']'

	"""
	Set the center of the bounding box. All other fields needs to be updated as well.
	:param center: the new center of the bbox
	"""
	def setCenter(self, center):
		self.center = center
		self.t = center[0]-self.height/2
		self.l = center[1]-self.width/2
		self.b = center[0]+self.height/2
		self.r = center[1]+self.width/2
		self.origin = (self.t, self.l)
		self.br = (self.b, self.r)

""" Shape to hold the bounding box and type of multiple shapes for tracking """
class Shape(object):
	"""
	:param bbox: a BBox object representing the position of the object
	"""
	def __init__(self, bbox, m=0.0, g=None, vel=[0.0, 0.0]):
		self.bbox = bbox
		self.x = np.array([bbox.center[0], bbox.center[1]])
		self.v = np.array(vel)
		self.a = None
		if not g is None:
			self.a = [g, 0]
		self.restitution = 2.75
		self.mass = m
		self.needsUpdate = False

	"""
	Set the y position of the shape
	:param y: the new y position
	"""
	def setPos(self, pos):
		self.needsUpdate = True
		self.bbox.setCenter(pos)

	def setVel(self, vel):
		self.needsUpdate = True
		self.v = np.array(vel)
		if self.isAtRest():
			self.needsUpdate = False

	def isAtRest(self):
		return self.v[0] == 0 and self.v[1] == 0

	def nextPos(self, dt=0.125):
		if self.a is None: return

		x = np.zeros(2)
		v = np.zeros(2)

		x[0] = self.x[0] + self.v[0]*dt + .5*self.a[0]*dt**2
		v[0] = self.v[0] + self.a[0]*dt

		x[1] = self.x[1] + self.v[1]*dt + .5*self.a[1]*dt**2
		v[1] = self.v[1] + self.a[1]*dt

		self.x = x
		self.setPos((x[0], x[1]))
		self.setVel(v)