import drawSvg as draw

def waterbombOneA (d, x, y, w, h): 
	d.append(draw.Line(x,y+h/2,x+w,y+h/2,
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x,y+h,x+w,y+h,
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x,y,x,y+h,
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x,y,x+w,y+h,
            stroke='blue', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x,y+h,x+w,y,
			stroke='blue', stroke_width=1, fill='red', fill_opacity=0.2))

def waterbombOneB (d, x, y, w, h): 
	d.append(draw.Line(x,y+h/2,x+w,y+h/2,
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x,y+h,x+w,y+h,
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x,y,x,y+h,
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))

	d.append(draw.Line(x,y+h/2,x+w/2,y,
            stroke='blue', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x+w/2,y,x+w,y+h/2,
			stroke='blue', stroke_width=1, fill='red', fill_opacity=0.2))

	d.append(draw.Line(x,y+h/2,x+w/2,y+h,
            stroke='blue', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x+w/2,y+h,x+w,y+h/2,
			stroke='blue', stroke_width=1, fill='red', fill_opacity=0.2))

def waterbombTwo (d, x, y, w, h): 
	d.append(draw.Line(x,y,x+w,y+h,
            stroke='blue', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x,y+h,x+w,y,
			stroke='blue', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x,y+h/2,x+w,y+h/2,
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x,y+h,x+w,y+h,
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))

def linearFoldA(d, x,y,w,h, point):
	d.append(draw.Line(x+w/2,y,x+w/2,y+(h/point)+(w/2),
            stroke='blue', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x+w/2,y+(h/point)+(w/2),x+w/2,y+h,
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))

	d.append(draw.Line(x,y+h/point,x+w/2,y+(h/point)+(w/2),
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x+w/2,y+(h/point)+(w/2),x+w,y+(h/point),
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))

	d.append(draw.Line(x+w,y,x+w,y+(h/point),
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x+w,y+(h/point),x+w,y+h,
            stroke='blue', stroke_width=1, fill='red', fill_opacity=0.2))


def linearFoldB(d, x,y,w,h, point):
	d.append(draw.Line(x+w/2,y,x+w/2,y+(h/point)+(w/2),
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x+w/2,y+(h/point)+(w/2),x+w/2,y+h,
            stroke='blue', stroke_width=1, fill='red', fill_opacity=0.2))

	d.append(draw.Line(x,y+h/point+w,x+w/2,y+(h/point)+(w/2),
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x+w/2,y+(h/point)+(w/2),x+w,y+(h/point)+w,
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))

	d.append(draw.Line(x+w,y,x+w,y+(h/point)+w,
            stroke='blue', stroke_width=1, fill='red', fill_opacity=0.2))
	d.append(draw.Line(x+w,y+(h/point)+w,x+w,y+h,
            stroke='red', stroke_width=1, fill='red', fill_opacity=0.2))