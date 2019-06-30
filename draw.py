import drawSvg as draw
from patterns import *


d = draw.Drawing(600, 600)
# radius of the circle



#linearFoldA(0, 0, 100, 250, 1.2)
#linearFoldB(0, 250, 100, 250, 2)

#linearFoldPage(d, 50, 600, 3)
t = Pattern(d)


#t.makeGradiantX(100, 100, 5, 10, Pieces.waterbombOneA);
#t.makeComplexWaterbomb(100, 100, 0,0, Pieces.waterbombOneA, Pieces.waterbombOneB)
t.makeSimpleWaterbomb(100, 100, 0, Pieces.waterbombTwo)
#makeComplexWate	rbomb(
#makeSimpleWaterbomb(d, 100, 100)
#makeGradiant(d, 100, 100)
d.saveSvg('pattern.svg')

