import drawSvg as draw
from pieces import *
from patterns import *

d = draw.Drawing(600, 600)

#linearFoldA(0, 0, 100, 250, 1.2)
#linearFoldB(0, 250, 100, 250, 2)

#linearFoldPage(d, 50, 600, 3)

#makeComplexWaterbomb(
makeSimpleWaterbomb(d, 100, 100)
#makeGradiant(d, 100, 100)
d.saveSvg('pattern.svg')

