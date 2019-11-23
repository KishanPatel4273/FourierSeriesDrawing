import math
class Complex():
	def __init__(self, real, imaginary):
		self.complex = [real, imaginary]

	def getReal(self):
		return self.complex[0]

	def getImaginary(self):
		return self.complex[1]
	
	def getComplex(self):
		return self.complex

	def getMagnitude(self):
		return (self.getReal()**2 + self.getImaginary()**2)**0.5

	def __str__(self):
		return "(" + str(self.complex[0]) + " + " + str(self.complex[1]) + "i)"

def add_complex(z,w):
	return Complex(z.getReal() + w.getReal(), z.getImaginary() + w.getImaginary())

def scale_complex(s,z):
	return Complex(s*z.getReal(), s*z.getImaginary())

def expi(theta):
	return Complex(math.cos(theta), math.sin(theta))

def multiply_complex(z, w):
	return Complex(z.getReal()*w.getReal() - z.getImaginary()*w.getImaginary(), z.getReal()*w.getImaginary() + z.getImaginary()*w.getReal())
