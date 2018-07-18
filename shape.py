from force import Force

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
	def __init__(self, bbox, vel=[0.0, 0.0]):
		self.bbox = bbox
		self.vel = vel
		self.forces = []
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
		self.vel = vel
		if self.isAtRest():
			self.needsUpdate = False

	def isAtRest(self):
		return self.vel[0] == 0 and self.vel[1] == 0

	def addForce(self, force):
		self.forces.append(force)

	def hasForceFrom(self, obj):
		return obj in [force.source for force in self.forces]