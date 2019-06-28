import drawSvg as draw

def waterbombOneA (d, x, y, w, h): 
	d.append(draw.Line(x,y+h/2,x+w,y+h/2,
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x,y+h,x+w,y+h,
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x,y,x,y+h,
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x,y,x+w,y+h,
            stroke=mountain, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x,y+h,x+w,y,
			stroke=mountain, stroke_width=1, fill=valey, fill_opacity=0.2))

def waterbombOneB (d, x, y, w, h): 
	d.append(draw.Line(x,y+h/2,x+w,y+h/2,
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x,y+h,x+w,y+h,
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x,y,x,y+h,
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))

	d.append(draw.Line(x,y+h/2,x+w/2,y,
            stroke=mountain, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x+w/2,y,x+w,y+h/2,
			stroke=mountain, stroke_width=1, fill=valey, fill_opacity=0.2))

	d.append(draw.Line(x,y+h/2,x+w/2,y+h,
            stroke=mountain, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x+w/2,y+h,x+w,y+h/2,
			stroke=mountain, stroke_width=1, fill=valey, fill_opacity=0.2))
def isMountain(m):
	if(m):
		return 'red'
	else:
		return 'blue'

def isValey(m):
	if(m):
		return 'blue'
	else:
		return 'red'
def waterbombTwo (d, x, y, w, h, m): 
	d.append(draw.Line(x,y,x+w,y+h,
            stroke=isMountain(m), stroke_width=1, fill_opacity=0.2))
	d.append(draw.Line(x,y+h,x+w,y,
			stroke=isMountain(m), stroke_width=1, fill_opacity=0.2))
	d.append(draw.Line(x,y+h/2,x+w,y+h/2,
            stroke=isValey(m), stroke_width=1, fill_opacity=0.2))
	d.append(draw.Line(x,y+h,x+w,y+h,
            stroke=isValey(m), stroke_width=1, fill_opacity=0.2))

def linearFoldA(d, x,y,w,h, point):
	d.append(draw.Line(x+w/2,y,x+w/2,y+(h/point)+(w/2),
            stroke=mountain, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x+w/2,y+(h/point)+(w/2),x+w/2,y+h,
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))

	d.append(draw.Line(x,y+h/point,x+w/2,y+(h/point)+(w/2),
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x+w/2,y+(h/point)+(w/2),x+w,y+(h/point),
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))

	d.append(draw.Line(x+w,y,x+w,y+(h/point),
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x+w,y+(h/point),x+w,y+h,
            stroke=mountain, stroke_width=1, fill=valey, fill_opacity=0.2))


def linearFoldB(d, x,y,w,h, point):
	d.append(draw.Line(x+w/2,y,x+w/2,y+(h/point)+(w/2),
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x+w/2,y+(h/point)+(w/2),x+w/2,y+h,
            stroke=mountain, stroke_width=1, fill=valey, fill_opacity=0.2))

	d.append(draw.Line(x,y+h/point+w,x+w/2,y+(h/point)+(w/2),
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x+w/2,y+(h/point)+(w/2),x+w,y+(h/point)+w,
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))

	d.append(draw.Line(x+w,y,x+w,y+(h/point)+w,
            stroke=mountain, stroke_width=1, fill=valey, fill_opacity=0.2))
	d.append(draw.Line(x+w,y+(h/point)+w,x+w,y+h,
            stroke=valey, stroke_width=1, fill=valey, fill_opacity=0.2))