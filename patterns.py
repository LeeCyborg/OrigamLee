import drawSvg as draw
from pieces import *
import random
import math



class Pattern(Pieces):
	def __init__(self, where):
		self.d = where

	def makeCanvas():
		pass

	def makeSimple(self, width, height, m, piece):	
		for x in range(0, self.d.width, width):
			for y in range(0, self.d.height, height):
				piece(self, self.d, x, y, width, height, m, 0)
	def  makeGradiantX (self, width, height, factor, interations, piece):
		currentX = 0
		for x in range(1, interations, 1):
			for y in range(1, interations, 1):
				piece(self, self.d, currentX, y*height, x*width/factor, height, 1, 0)
			currentX = currentX+(x*width/factor)
	def  makeGradiantY (self, width, height, factor, interations):
		currentY = 0
		for y in range(1, interations, 1):
			for x in range(1, interations, 1):
				Pieces.waterbombTwo(self, self.d, x*width, currentY, width, y*height/factor, 1, 0)
			currentY = currentY+(y*height/factor)

	def makeComplex(self, width, height, factor, iterations, pieceA, pieceB):
		for x in range(0, self.d.width, width*2):
			for y in range(0, self.d.height, height):
				pieceA(self, self.d, x, y, width, height, 0, 0)
				pieceB(self, self.d, x+width, y, width, height, 0, 0)
#fix
	def  makeGradiantXY (self, width, height, factor, interations):
		currentX = 0
		for x in range(1, interations, 1):
			mod = 0
			for y in range(1, interations, 1):
				Pieces.waterbombTwo(self, self.d, currentX, y*height+(mod), x*width/factor, height, 1, mod)
				mod = mod+30
			currentX = currentX+(x*width/factor)

	def linearFoldPage(self, width, height, point):
		currentX = 0 	
		for x in range(0, 10, 1):
				#linearFold(x, 0, width, height, point)
				Pieces.linearFoldA(self, self.d, currentX, 0, x*width/3, height, point)
				currentX = currentX+(x*width/3)

	def radialPattern(self, width, height, iterations):
		for x in range(1, 20, 1):
			circle_r = 100
			circle_x = 50
			circle_y = 70
			alpha = 2 * math.pi * 0.4
			r = circle_r * math.sqrt(4)
			x = r * math.cos(alpha) + circle_x
			y = r * math.sin(alpha) + circle_y
			d.append(draw.Circle(x, y, 3,
				fill='red', stroke_width=2, stroke='black'))


##to be modified 





