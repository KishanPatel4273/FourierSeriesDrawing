class Rectangle:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height


	def addX(self, x):
		self.x += x

	def addY(self, y):
		self.y += y

	def setWidth(self, width):
		self.width = width

	def setHeight(self, height):
		self.height = height

	def render_rectangle(self, pixels, color):
		for x in range(self.x, self.x + self.width + 1):
			for y in range(self.y, self.y + self.height + 1):
				pixels[x,y] = color

