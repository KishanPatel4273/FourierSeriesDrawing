from Complex import *
from Vector import Vector2f
from Vector import add_vector
import math

class FourierVector:
	#c-complex
	def __init__(self, scaler, frequency, center_x, center_y):
		self.frequency = frequency
		self.radius = scaler.getMagnitude()
		self.center = Vector2f(center_x, center_y)
		self.scaler = scaler

	def getCenter(self):
		return self.center

	def setCenter(self, new_center):
		self.center = new_center

	def getRadius(self):
		return self.radius

	#center at origin
	def getVector(self, time):
		#e^-2pifti
		r = multiply_complex(self.scaler ,expi(-2*math.pi*self.frequency*time))
		return add_vector(Vector2f(r.getReal(), r.getImaginary()), self.getCenter())

	def __str__(self):
		return "[" + self.scaler.__str__() + "] * [" + "expi(-2*pi*" + str(self.frequency) + "*t*i)] + [" + self.center.__str__() + "]"  
