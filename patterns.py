import drawSvg as draw
from pieces import Pieces
import math


class Pattern(Pieces):
    def __init__(self, drawing):
        self.d = drawing

    def makeCanvas():
        pass

    def makeSimple(self, width, height, m, piece):
        for x in range(0, self.d.width, width):
            for y in range(0, self.d.height, height):
                piece(self, self.d, x, y, width, height, m, 0)

    def makeGradientX(self, width, height, factor, iterations, piece):
        currentX = 0
        for x in range(1, iterations, 1):
            for y in range(1, iterations, 1):
                piece(self, self.d, currentX, y*height,
                      x*width/factor, height, 1, 0)
            currentX = currentX+(x*width/factor)

    def makeGradientY(self, width, height, factor, iterations, piece):
        currentY = 0
        for y in range(1, iterations, 1):
            for x in range(1, iterations, 1):
                piece(self, self.d, x*width,
                      currentY, width, y*height/factor, 1, 0)
            currentY = currentY+(y*height/factor)

    def makeComplex(self, width, height, iterations, pieceA, pieceB):
        for x in range(0, self.d.width, width*2):
            for y in range(0, self.d.height, height):
                pieceA(self, self.d, x, y, width, height, 0, 0)
                pieceB(self, self.d, x+width, y, width, height, 0, 0)

    def makeGradientXY(self, width, height, factor, iterations, piece):
        currentX = 0
        for x in range(1, iterations, 1):
            currentY = 0
            for y in range(1, iterations, 1):
                piece(self, self.d, currentX, currentY, x*width/factor, y*height/factor, 1, 0)
                currentY = currentY+(y*height/factor)
            currentX = currentX+(x*width/factor)

    def makeComplexGradientXY(self, width, height, factor, pieceA, pieceB):
        currentX = 0
        for x in range(0, self.d.width, width*2):
            currentY = 0
            for y in range(0, self.d.height, height):
                pieceA(self, self.d, currentX, currentY, x/factor, y/factor, 0, 0)
                pieceB(self, self.d, currentX + (x/factor), currentY, x/factor, y/factor, 0, 0)
                currentY = currentY+(y/factor)
            currentX = currentX+2*(x/factor)

    def linearFoldPage(self, width, height, point, m=0):
        currentX = 0
        for x in range(0, 10, 1):
            Pieces.linearFoldA(self, self.d, currentX, 0,
                               x*width/point, height, point, m)
            currentX = currentX+(x*width/point)

    def radialPattern(self, width, height, iterations):
        for x in range(1, 20, 1):
            circle_r = 100
            circle_x = 50
            circle_y = 70
            alpha = 2 * math.pi * 0.4
            r = circle_r * math.sqrt(4)
            x = r * math.cos(alpha) + circle_x
            y = r * math.sin(alpha) + circle_y
            self.d.append(draw.Circle(x, y, 3,
                                      fill='red', stroke_width=2, stroke='black'))


# to be modified
