from Complex import *
from Vector import *
import math

class Render:
	#origin is (x, y) in terms of bottom left is (0,0)
	def __init__(self, x, y, width, height):
		self.width = width
		self.height = height
		self.x = x
		self.y = y 
		self.minX = int(self.x - width/2)
		self.maxX = int(self.x + width/2)
		self.minY = int(self.y - height/2)
		self.maxY = int(self.y + height/2)

	def plot_pixel(self, pixels, x, y, color, thickness = 1):
		if thickness != 1:
			self.fill_circle(pixels, x, y, thickness, color)
		#redefines the origin (bottom left corner is 0,0)
		y = int(self.height - y - self.y)
		x = int(x + self.x)
		if thickness == 1 and 0 <= x and x < self.width and 0 <= y and y < self.height:
			pixels[x,y] = color

	def plot_vector_pixel(self, pixels, v, color):
		self.plot_pixel(pixels, v.getX(), v.getY(), color)

	def draw_line(self, pixels, x1, y1, x2, y2, color, thickness = 1):
		dx = x2 - x1
		dy = y2 - y1
		min_y =  min(int(y1),int(y2))
		max_y = max(int(y1),int(y2))+1
		if dx == 0:#vertical
			for y in range(min_y, max_y):
				self.plot_pixel(pixels, x1, y, color, thickness)
			return
		min_x =  min(int(x1),int(x2))
		max_x = max(int(x1),int(x2))+1
		if dy == 0:#horizontal
			for x in range(min_x, max_x):
				self.plot_pixel(pixels, x, y1, color, thickness)
			return
		slope = dy / dx
		if x1 < self.minX:x1 == self.minX
		if x2 < self.minX:x2 == self.minX
		if y1 < self.minY:y1 == self.minY
		if y2 < self.minY:y2 == self.minY
		if x1 >= self.maxX:x1 == self.maxX - 1
		if x2 >= self.maxX:x2 == self.maxX - 1
		if y1 >= self.maxY:y1 == self.maxY - 1
		if y2 >= self.maxY:y2 == self.maxY - 1
		if abs(slope) > 1:# plot in y
			for y in range(min_y, max_y):
				x = int((y-y1)/slope + x1)  
				self.plot_pixel(pixels, x, y, color, thickness)
		else:# plot in x
			for x in range(min_x, max_x):
				y = int(slope*(x-x1) + y1)
				self.plot_pixel(pixels, x, y, color, thickness)

	def draw_vertical_line(self, pixels, x, y1, y2, color, thickness = 1):
		min_y =  min(int(y1),int(y2))
		max_y = max(int(y1),int(y2))+1
		for y in range(min_y, max_y):
			self.plot_pixel(pixels, x, y, color, thickness)

	def draw_horizontal_line(self, pixels, x1, x2, y, color):
		min_x =  min(int(x1),int(x2))
		max_x = max(int(x1),int(x2))+1
		for x in range(min_x, max_x):
				self.plot_pixel(pixels, x, y, color)

	#draw line between two vector2fs
	def draw_vector_line(self, pixels, v, u, color, thickness = 1):
		self.draw_line(pixels, v.getX(), v.getY(), u.getX(), u.getY() ,color, thickness)

	def draw_elipse(self, pixels, center_x, center_y, a, b, color):#x2/a2 + y2/b2 = 1
		if a == 0 or b == 0:
			return
		for y in range(-b,b+1):
			x = (a**2 * (1-(y**2/b**2)))**0.5
			self.plot_pixel(pixels, center_x + x, center_y + y, color)
			self.plot_pixel(pixels, center_x - x, center_y + y, color)		
		for x in range(-a,a+1):
			y = (b**2 * (1-(x**2/a**2)))**0.5
			self.plot_pixel(pixels, center_x + x, center_y + y, color)
			self.plot_pixel(pixels, center_x + x, center_y - y, color)	

	def fill_elipse(self, pixels, center_x, center_y, a, b, color):
		if a == 0 or b == 0:
			return
		a2 = a**2
		b2 = b**2
		for y in range(-b,b+1):
			x = (a2 * (1-(y**2/b2)))**0.5
			self.draw_horizontal_line(pixels, center_x + x, center_x - x, center_y + y, color)
		for x in range(-a,a+1):
			y = (b2 * (1-(x**2/a2)))**0.5
			self.draw_vertical_line(pixels, center_x + x, center_y + y, center_y - y, color)

	def draw_circle(self, pixels, center_x, center_y, radius, color):
		self.draw_elipse(pixels, center_x, center_y, int(radius), int(radius), color)

	def fill_circle(self, pixels, center_x, center_y, radius, color):
		r2 = radius**2
		radius = int(radius)
		for x in range(-radius,radius+1):
			y = (r2 * (1-(x**2/r2)))**0.5
			self.draw_vertical_line(pixels, center_x + x, center_y + y, center_y - y, color)
	def render_fourierVector(self, pixels, fourier_vector, time, color, plot=False, pixels_drawing=[], ring = True):
		if ring:
			self.draw_circle(pixels, fourier_vector.getCenter().getX(), fourier_vector.getCenter().getY(), fourier_vector.getRadius(), color)
		p = fourier_vector.getVector(time)
		self.draw_vector_line(pixels, fourier_vector.getCenter(), p, color)
		if plot:	
			pixels_drawing.append(p)

	#Fourier Vectors - list of fourier vectors
	#color_vectors - rgbint
	#pixels_drawing - empty list, to store the points of the image
	def render_fourierDrawing(self, pixels, fourier_vectors, time, color_vectors, color_drawing=123435, pixels_drawing=[]):
		self.render_fourierVector(pixels, fourier_vectors[0], time, color_vectors)
		for i in range(1,len(fourier_vectors)):
			fourier_vectors[i].setCenter(fourier_vectors[i-1].getVector(time))
			if i == len(fourier_vectors)-1:
				self.render_fourierVector(pixels, fourier_vectors[i], time, color_vectors, plot=True, pixels_drawing=pixels_drawing)
			else:
				self.render_fourierVector(pixels, fourier_vectors[i], time, color_vectors)
		for i in range(len(pixels_drawing)-1):
			self.draw_vector_line(pixels, pixels_drawing[i], pixels_drawing[i+1], color_drawing, thickness = 1)
			#signals
			#pixels_drawing[i].addX(200/600)

	def render_list_points(self, pixels, p, color):
			for i in range(len(p)):
				self.plot_pixel(pixels, p[i][0], p[i][1], color)

	def render_list_vector2f(self, pixels, p, color):
			for i in range(len(p)):
				self.plot_vector_pixel(pixels, p[i], color)

	def draw_point_triangle(self, pixels, x1, y1, x2, y2, x3, y3, color):
		self.draw_line(pixels, x1, y1, x2, y2, color)
		self.draw_line(pixels, x1, y1, x3, y3, color)
		self.draw_line(pixels, x2, y2, x3, y3, color)

	def draw_vector_triangle(self, pixels, a, b, c, color):
		self.draw_vector_line(pixels, a, b, color)
		self.draw_vector_line(pixels, a, c, color)
		self.draw_vector_line(pixels, b, c, color)
