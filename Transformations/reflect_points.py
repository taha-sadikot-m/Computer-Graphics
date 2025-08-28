import turtle

def midpoint_ellipse(x_center, y_center, rx, ry):
	points = []
	x = 0
	y = ry
	rx2 = rx * rx
	ry2 = ry * ry
	tworx2 = 2 * rx2
	twory2 = 2 * ry2
	px = 0
	py = tworx2 * y

	# Region 1
	d1 = ry2 - (rx2 * ry) + (0.25 * rx2)
	while px < py:
		points.append((x_center + x, y_center + y))
		points.append((x_center - x, y_center + y))
		points.append((x_center + x, y_center - y))
		points.append((x_center - x, y_center - y))
		x += 1
		px += twory2
		if d1 < 0:
			d1 += ry2 + px
		else:
			y -= 1
			py -= tworx2
			d1 += ry2 + px - py

	# Region 2
	d2 = (ry2) * ((x + 0.5) ** 2) + (rx2) * ((y - 1) ** 2) - (rx2 * ry2)
	while y >= 0:
		points.append((x_center + x, y_center + y))
		points.append((x_center - x, y_center + y))
		points.append((x_center + x, y_center - y))
		points.append((x_center - x, y_center - y))
		y -= 1
		py -= tworx2
		if d2 > 0:
			d2 += rx2 - py
		else:
			x += 1
			px += twory2
			d2 += rx2 - py + px
	return list(set(points))


def mirror_points(points,axis):
	mirrored = []
	for x, y in points:
		if axis == 'x':
			mirrored.append((x, -y))
		elif axis == 'y':
			mirrored.append((-x, y))
		elif axis == 'xy':
			mirrored.append((-x, -y))
	return mirrored

def draw_ellipse(points,ellipse):
	ellipse.speed(1000)
	ellipse.penup()
	ellipse.goto(points[0][0], points[0][1])
	ellipse.pendown()
	for point in points[1:]:
		ellipse.goto(point[0], point[1])
	ellipse.penup()
	ellipse.goto(points[0][0], points[0][1])
	ellipse.dot(8, 'green')
	ellipse.fillcolor('yellow')
	ellipse.begin_fill()
	ellipse.end_fill()



ellipse = turtle.Turtle()
x1, y1 = map(float, input("Enter the coordinates of the center (x1, y1): ").split())
rx = float(input("Enter the x-radius (rx) of the ellipse: "))
ry = float(input("Enter the y-radius (ry) of the ellipse: "))

axis = input("Enter the axis of reflection (x, y, xy): ")


points = midpoint_ellipse(x1, y1, rx, ry)
draw_ellipse(points, ellipse)

mirrored_points = mirror_points(points, axis)
draw_ellipse(mirrored_points, ellipse)

turtle.done()

