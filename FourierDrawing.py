from Complex import *
from Vector import *
from FourierVector import *
import math
import numpy as np

#self.p = [[100,100],[0,200],[-100, 100],[-100,-100], [0,-200], [100,-100]]
		#self.p = [[0,100],[100,0],[-100,0],[0,-100],[100,0],[200,-100],[-200,-100],[-100,0]]
		#self.sigma = [[-200,-200], [0,0], [-200,200], [100,200], [100, 100] , [90, 100], [90,190], [-180, 190], [10, 0], [-180, -190], [90, -190], [90, -100], [100, -100], [100,-200],]
		#self.p = [[0,0],[100,100],[100,-100],[200,-100],[300,0], [400,-100], [100,100],[-100, 100],[-100,-100]]
#		self.p = [[-7,19],[-8,32],[-6,46],[-6,62],[-6,75],[-7,88],[0,98],[9,94],[18,86],[30,76],[36,68],[39,59],[37,46],[32,38],[27,29],[21,23],[12,19],[5,16],[-10,17],[-19,21],
#[-28,30],[-34,36],[-41,47],[-46,61],[-40,70],[-37,82],[-46,87],[-50,79],[-52,67],[-50,54],[-46,43],[-40,35],[-36,28],[-30,21],[-23,13],[-14,8],[-1,6],[9,9],[18,13],[28,19],
#[33,25],[40,33],[47,46],[48,61],[43,79],[34,91],[22,100],[13,105],[0,108],[-11,108],[-15,100],[-16,93],[-16,84],[-15,73],[-16,61],[-14,50],[-14,40],[-14,31],[-14,20],[-15,8],
#[-14,-5],[-10,-17],[-14,-24],[-12,-33],[-13,-42],[-16,-48],[-15,-55],[-13,-64],[-14,-73],[-13,-86],[-12,-90],[-5,-92],[1,-86],[3,-72],[2,-55],[1,-39],[1,-26],[1,-16],[1,-5],[0,11],]
#		self.p = [[-78,-51],[-71,-33],[-58,-16],[-43,4],[-32,24],[-21,41],[-12,59],[-1,66],[6,48],[16,32],[24,20],[36,5],[46,-11],[50,-24],[60,-45],[67,-62],[65,-73],[53,-67],[36,-60],[23,-52],
#[-1,-41],[-13,-31],[-36,-19],[-60,-4],[-79,12],[-97,29],[-90,35],[-69,33],[-53,37],[-37,35],[-16,33],[4,31],[21,30],[35,30],[54,29],[70,25],[57,18],[41,6],[15,-9],[-8,-19],
#[-25,-31],[-50,-40],[-62,-52],[-72,-63],]

#gives FourierVectors to draw image with lines
class FourierDrawing:
	#p points in order of image
	#2n+1 = # of rotators
	def __init__(self, p, n, center=Vector2f(0,0)):
		self.p = p
		self.n = n
		self.lengths_of_image = self.lengths_of_image()
		self.sum_of_L = sum(self.lengths_of_image)
		self.center = center

	#gets distance from point p1 to point p2
	def length_of_line(self, p1, p2):
		return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5

	'''
	time to go from p1 to p2 is t=1
	gets the point that lies on the line formed by p1 and p2 at given time
	'''
	def line(self, p1, p2, time):
		xt = (p2[0]-p1[0])*time
		yt = (p2[1]-p1[1])*time
		return Complex(p1[0]+xt, p1[1]+yt)

	'''
	gets the length of the image
	adds up the length of the line segments up
	'''
	def lengths_of_image(self):#
		length = []
		for i in range(len(self.p)):
			if i == len(self.p)-1:
				length.append(self.length_of_line(self.p[i], self.p[0]))
			else:
				length.append(self.length_of_line(self.p[i], self.p[i+1]))
		return length

	'''
	makes the drawing to a function
	repeats every t=1
	gets point on image(line segments) at given time 
	'''
	def I(self, time):
		L = self.lengths_of_image
		distance = self.sum_of_L*time
		index = 0#line segment to get point from
		for i in range(len(L)+1):
			if sum(L[0:i]) >= distance:#then i-1 is index
				index = i-1
				if i == 0:
					index = 0
				break
		sum_to_index = sum(L[0:index])
		if index == len(L)-1:
			t = self.sum_of_L - sum_to_index 
		else:
			t = sum(L[0:index+1]) - sum_to_index
		dt = self.sum_of_L*time - sum_to_index
		ldt = dt/t
		if index == len(L)-1:
			return self.line(self.p[index], self.p[0], ldt)
		else:
			return self.line(self.p[index], self.p[index+1], ldt)

	'''
	integrates the form 0 to 1 the image(t) * and expi(2 pi f t)
	applies the Fourier Transform  
	'''
	def integrate(self, frequency, dt=.001):
		I = Complex(0,0)
		for t in range(0,int(1/dt)+1):#t-[0,1]
			s = scale_complex(dt, multiply_complex(self.I(t*dt), expi(2*math.pi*frequency*(t*dt))))
			I = add_complex(I, s)
		return I

	'''
	orders the Fourier vectors by their radius
	'''
	def order(self, fv):
		for j in range(len(fv)):
			for i in range(len(fv)-1):
				if fv[i].getRadius() < fv[i+1].getRadius():
					temp = fv[i]
					fv[i] = fv[i+1]
					fv[i+1] = temp

	'''	
	generates the Fourier Vectors to draw the image
	'''
	def getFourierVectors(self):
		fv = []
		center = self.center
		i = 0
		for f in range(-self.n,self.n+1):
			fv.append(FourierVector(self.integrate(f), f, center.getVector()[0], center.getVector()[1]))
			center = fv[i].getVector(0) 
			i += 1
		self.order(fv)
		return fv