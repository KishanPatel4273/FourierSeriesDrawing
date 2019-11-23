from Vector import *
from FourierVector import *
from FourierDrawing import *
from Complex import *
from Rectangle import *
from Render import *
import math
import numpy as np
import time

class Screen:
	def __init__(self, x, y, width, height, n):
		self.width = width
		self.height = height
		self.render = Render(x, y, width, height)	
		self.time = 0	
		self.sigma = [[-200,-200], [0,0], [-200,200], [100,200], [100, 100] , [90, 100], [90,190], [-180, 190], [10, 0], [-180, -190], [90, -190], [90, -100], [100, -100], [100,-200],]
		self.p = [[-7,19],[-8,32],[-6,46],[-6,62],[-6,75],[-7,88],[0,98],[9,94],[18,86],[30,76],[36,68],[39,59],[37,46],[32,38],[27,29],[21,23],[12,19],[5,16],[-10,17],[-19,21],
		[-28,30],[-34,36],[-41,47],[-46,61],[-40,70],[-37,82],[-46,87],[-50,79],[-52,67],[-50,54],[-46,43],[-40,35],[-36,28],[-30,21],[-23,13],[-14,8],[-1,6],[9,9],[18,13],[28,19],
		[33,25],[40,33],[47,46],[48,61],[43,79],[34,91],[22,100],[13,105],[0,108],[-11,108],[-15,100],[-16,93],[-16,84],[-15,73],[-16,61],[-14,50],[-14,40],[-14,31],[-14,20],[-15,8],
		[-14,-5],[-10,-17],[-14,-24],[-12,-33],[-13,-42],[-16,-48],[-15,-55],[-13,-64],[-14,-73],[-13,-86],[-12,-90],[-5,-92],[1,-86],[3,-72],[2,-55],[1,-39],[1,-26],[1,-16],[1,-5],[0,11],]
		self.fv = FourierDrawing(self.sigma, n, Vector2f(50,150)).getFourierVectors()
		self.drawing = []
		self.start_time = time.time()
		self.old_time = self.start_time

	def tick_screen(self):
		if self.time == 1:
			print("bocken")
		#pressed = pygame.key.get_pressed()
        #if pressed[pygame.K_UP]: self.a.addY(-3)
        #if pressed[pygame.K_DOWN]: self.a.addY(3)
        #if pressed[pygame.K_LEFT]: self.a.addX(-3)
        #if pressed[pygame.K_RIGHT]: self.a.addX(3)

	def render_screen(self, pixels):
		self.time += 1/60 * 1/(10/2)# f = fps * 1/n 
				

		#print(self.passed_time())
		self.render.render_fourierDrawing(pixels, self.fv, self.time, 0, color_drawing=255, pixels_drawing=self.drawing)
		#print(self.passed_time())
		#print('-------------------')
		
		

		#self.render.draw_line(pixels, -50, 0, 50, 0, 255000)
		#self.render.draw_line(pixels, 0, -50, 0, 50, 255000)

	def passed_time(self):
		temp_time = self.old_time
		self.old_time = time.time()
		return self.old_time - temp_time
