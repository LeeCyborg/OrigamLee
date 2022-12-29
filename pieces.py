import drawSvg as draw


class Pieces:
    def __init__(self, where):
        pass

    def waterbombOneA(self, d, x, y, w, h, m, n):
        d.append(draw.Line(x, y+h/2, x+w, y+h/2,
                           stroke=self.isValley(m), stroke_width=1))
        d.append(draw.Line(x, y+h, x+w, y+h,
                           stroke=self.isValley(m), stroke_width=1))
        d.append(draw.Line(x, y, x, y+h,
                           stroke=self.isValley(m), stroke_width=1))
        d.append(draw.Line(x, y, x+w, y+h,
                           stroke=self.isMountain(m), stroke_width=1))
        d.append(draw.Line(x, y+h, x+w, y,
                           stroke=self.isMountain(m), stroke_width=1))

    def waterbombOneB(self, d, x, y, w, h, m, n):
        d.append(draw.Line(x, y+h/2, x+w, y+h/2,
                           stroke=self.isValley(m), stroke_width=1))
        d.append(draw.Line(x, y+h, x+w, y+h,
                           stroke=self.isValley(m), stroke_width=1))
        d.append(draw.Line(x, y, x, y+h,
                           stroke=self.isValley(m), stroke_width=1))

        d.append(draw.Line(x, y+h/2, x+w/2, y,
                           stroke=self.isMountain(m), stroke_width=1))
        d.append(draw.Line(x+w/2, y, x+w, y+h/2,
                           stroke=self.isMountain(m), stroke_width=1))

        d.append(draw.Line(x, y+h/2, x+w/2, y+h,
                           stroke=self.isMountain(m), stroke_width=1))
        d.append(draw.Line(x+w/2, y+h, x+w, y+h/2,
                           stroke=self.isMountain(m), stroke_width=1))
# model
# d location
# x y draw coord
# size of piece
# m is moountain?
# n diag factor

    def waterbombTwo(self, d, x, y, w, h, m, n):
        d.append(draw.Line(x, y, x+w, y+h+n,
                           stroke=self.isMountain(m), stroke_width=1))
        d.append(draw.Line(x, y+h, x+w, y,
                           stroke=self.isMountain(m), stroke_width=1))
        d.append(draw.Line(x, y+h/2, x+w, y+h/2+n,
                           stroke=self.isValley(m), stroke_width=1))
        d.append(draw.Line(x, y+h, x+w, y+h+n,
                           stroke=self.isValley(m), stroke_width=1))

    def linearFoldA(self, d, x, y, w, h, point, m=0):
        d.append(draw.Line(x+w/2, y, x+w/2, y+(h/point)+(w/2),
                           stroke=self.isMountain(m), stroke_width=1))
        d.append(draw.Line(x+w/2, y+(h/point)+(w/2), x+w/2, y+h,
                           stroke=self.isValley(m), stroke_width=1))

        d.append(draw.Line(x, y+h/point, x+w/2, y+(h/point)+(w/2),
                           stroke=self.isValley(m), stroke_width=1))
        d.append(draw.Line(x+w/2, y+(h/point)+(w/2), x+w, y+(h/point),
                           stroke=self.isValley(m), stroke_width=1))

        d.append(draw.Line(x+w, y, x+w, y+(h/point),
                           stroke=self.isValley(m), stroke_width=1))
        d.append(draw.Line(x+w, y+(h/point), x+w, y+h,
                           stroke=self.isMountain(m), stroke_width=1))

    def linearFoldB(self, d, x, y, w, h, point, m=0):
        d.append(draw.Line(x+w/2, y, x+w/2, y+(h/point)+(w/2),
                           stroke=self.isValley(m), stroke_width=1))
        d.append(draw.Line(x+w/2, y+(h/point)+(w/2), x+w/2, y+h,
                           stroke=self.isMountain(m), stroke_width=1))

        d.append(draw.Line(x, y+h/point+w, x+w/2, y+(h/point)+(w/2),
                           stroke=self.isValley(m), stroke_width=1))
        d.append(draw.Line(x+w/2, y+(h/point)+(w/2), x+w, y+(h/point)+w,
                           stroke=self.isValley(m), stroke_width=1))

        d.append(draw.Line(x+w, y, x+w, y+(h/point)+w,
                           stroke=self.isMountain(m), stroke_width=1))
        d.append(draw.Line(x+w, y+(h/point)+w, x+w, y+h,
                           stroke=self.isValley(m), stroke_width=1))

    def isMountain(self, m):
        if (m):
            return 'red'
        else:
            return 'blue'

    def isValley(self, m):
        if (m):
            return 'blue'
        else:
            return 'red'
