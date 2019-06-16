from pieces import *

def  makeSimpleWaterbomb (d, width, height):
	for x in range(0, 600, width):
		for y in range(0, 600, height):
			waterbombTwo(d, x, y, width, height)
def makeComplexWaterbomb (d, width, height):
	for x in range(0, 600, width*2):
		for y in range(0, 600, height):
			waterbombOneA(d, x, y, width, height)
			waterbombOneB(d, x+width, y, width, height)
def linearFoldPage(d, width, height, point):
	currentX = 0
	for x in range(0, 10, 1):
			#linearFold(x, 0, width, height, point)
			linearFoldA(d, currentX, 0, x*width/3, height, point)
			currentX = currentX+(x*width/3)

def  makeGradiant (d, width, height):
	currentY = 0
	for y in range(1, 10, 1):
		for x in range(1, 10, 1):
			waterbombTwo(d, x*width, currentY, width, y*height/3)
		currentY = currentY+(y*height/3)