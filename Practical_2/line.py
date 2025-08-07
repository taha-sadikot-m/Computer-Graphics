#bashermen line drawning algorithm

import matplotlib.pyplot as plt
import turtle

def Bashermen_Line(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1

    d = 2*(dy-dx)
    x = x1
    y = y1

    points = []
    points.append((x, y))

    while x < x2:
        if d < 0:
            d += 2*dy
        else:
            y += 1
            d += 2*(dy-dx)
        x += 1
        points.append((x, y))

    return points


def draw_line(points):
    x_coords, y_coords = zip(*points)
    plt.plot(x_coords, y_coords, marker='o')
    plt.title("Bashermen Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.axis('equal')
    plt.show()

def draw_line_with_turtle(points):
    line = turtle.Turtle()
    line.speed(500)  # Fastest drawing speed
    line.color('blue')
    line.penup()
    line.goto(points[0][0], points[0][1])
    line.pendown()
    for point in points[1:]:
        line.goto(point[0], point[1])
    line.penup()
    # Optionally, mark the start and end points
    line.goto(points[0][0], points[0][1])
    line.dot(8, 'green')  # Start point
    line.goto(points[-1][0], points[-1][1])
    line.dot(8, 'red')    # End point
    turtle.done()

#take cordinateds as a input from user
x1,y1 = map(float, input("Enter the coordinates of the center (x1, y1): ").split())
x2,y2 = map(float, input("Enter the coordinates of the end point (x2, y2): ").split())

points = Bashermen_Line(x1, y1, x2, y2)
draw_line_with_turtle(points)