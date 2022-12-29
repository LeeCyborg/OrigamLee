import drawSvg as draw
from patterns import Pattern, Pieces

d = draw.Drawing(600, 600)
t = Pattern(d)

# t.linearFoldPage(50, 600, 3)
# t.makeGradientX(100, 100, 5, 10, Pieces.waterbombOneA)
# t.makeGradientY(100, 100, 5, 10, Pieces.waterbombOneA)
# t.makeGradientXY(100, 100, 5, 10, Pieces.waterbombTwo)
# t.makeComplexGradientXY(50, 50, 5, Pieces.waterbombOneA, Pieces.waterbombOneB)
# t.makeComplex(100, 100, 0, Pieces.waterbombOneA, Pieces.waterbombOneB)
t.makeSimple(100, 100, 0, Pieces.waterbombTwo)
d.saveSvg('pattern.svg')
