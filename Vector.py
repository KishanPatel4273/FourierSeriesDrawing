import math
class Vector3f:
	def __init__(self, x, y, z):
		self.v = [x,y,z]

	def getX(self):
		return self.v[0]

	def getY(self):
		return self.v[1]

	def getZ(self):
		return self.v[2]

	def getVector(self):
		return self.v

	def __str__(self):
		return "(" + str(self.getX()) + ", " + str(self.getY()) + ", " + str(self.getZ()) +")"

class Vector2f:
	def __init__(self, x, y):
		self.v = [x,y]
		
	def getX(self):
		return self.v[0]

	def addX(self, x):
		self.v[0] += x

	def getY(self):
		return self.v[1]

	def addY(self, y):
		self.v[1] += y

	def getVector(self):
		return self.v

	def __str__(self):
		return "(" + str(self.getX()) + ", " + str(self.getY()) + ")"



#adds vector v and u together
def add_vector(v, u):
	if type(v) == type(u):
		if len(v.getVector()) == 3:#vector3f
			return Vector3f(v.getX() + u.getX(), v.getY() + u.getY(), v.getZ() + u.getZ())
		if len(v.getVector()) == 2:#vector2f
			return Vector2f(v.getX() + u.getX(), v.getY() + u.getY())
	

#scales vector v by s
def scale_vector(s, v):
	if len(v.getVector()) == 3:#vector3f
			return Vector3f(s*v.getX(), s*v.getY(), s*v.getZ())
	if len(v.getVector()) == 2:#vector2f
			return Vector2f(s*v.getX(), s*v.getY())

#computes dot product between v and u
def dot_product(v,u):
	dot_product = 0
	for i in range(len(v.getVector())):
		dot_product += v.getVector()[i] * u.getVector()[i]
	return dot_product

#computes cross product between v and u 
def cross_product(v,u):#vector3f
	return Vector3f(v.getY()*u.getZ() - v.getZ()*u.getY(), v.getZ()*u.getX() - v.getX()*u.getZ(), v.getX()*u.getY() - v.getY()*u.getX())