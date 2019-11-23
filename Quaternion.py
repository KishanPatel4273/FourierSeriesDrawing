from Vector import *

class Quaternion:
	def __init__(self, w, x, y, z):
		self.w = w
		self.v = Vector3f(x, y, z)

	def getW(self):
		return self.w

	def getX(self):
		return self.v.getX()

	def getY(self):
		return self.v.getY()

	def getZ(self):
		return self.v.getZ()

	def getV(self):
		return self.v

	def __str__(self):
		return "(" + str(self.w) + " ," + str(self.v.getX()) + " ," + str(self.v.getY()) + " ," + str(self.v.getZ()) + ")"  

def add_quaterion(a, b):
	return Quaternion(a.getW() + b.getW(), a.getX() + b.getX(), a.getY() + b.getY(), a.getZ() + b.getZ())

def scale_quaternion(s, q):
	return Quaternion(s*q.getW(), s*q.getX(), s*q.getY(), s*q.getZ())

def conjugate_quaternion(q):
	return Quaternion(q.getW(), -q.getX(), -q.getY(), -q.getZ())

def inverse_quaternion(q):
	return self.scale_quaternion(1/(q.getW()**2 + q.getX()**2 + q.getY()**2 + q.getZ()**2) , self.conjugate_quaternion(q))

def multiply_quaternion(a, b):
	return Quaternion(a.getW()*b..getX()         ,
							  0,
							  0,
							  0)
