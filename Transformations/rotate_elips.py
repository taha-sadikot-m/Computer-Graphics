import turtle
import math

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


def rotate_points(points,x_center,y_center,angle):
	rotated_points = []
	radians = math.radians(angle)
	sin_value = math.sin(radians)
	cos_value = math.cos(radians)

	for x, y in points:
		'''
		x_shifted = x - x_center
		y_shifted = y - y_center

		x_rotated = (x_shifted * cos_value) - (y_shifted * sin_value) + x_center
		y_rotated = (x_shifted * sin_value) + (y_shifted * cos_value) + y_center
		'''
		x_rotated = (x* cos_value) - (y * sin_value) 
		y_rotated = (x * sin_value) + (y * cos_value) 

		rotated_points.append((x_rotated, y_rotated))
	return rotated_points



def draw_ellipse(points, ellipse):
	
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
	



turtle_pen  = turtle.Turtle()
x1, y1 = map(float, input("Enter the coordinates of the center (x1, y1): ").split())
rx = float(input("Enter the x-radius (rx) of the ellipse: "))
ry = float(input("Enter the y-radius (ry) of the ellipse: "))

rotation_degree = float(input("Enter the rotation degree of the ellipse: "))


points = midpoint_ellipse(x1, y1, rx, ry)
draw_ellipse(points, turtle_pen)

new_points = rotate_points(points, x1, y1, rotation_degree)
draw_ellipse(new_points, turtle_pen)

turtle.done()
