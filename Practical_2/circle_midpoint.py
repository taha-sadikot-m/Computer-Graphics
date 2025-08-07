import turtle
import math



def Mid_point_Circle(x_center, y_center, radius):
    points = []

    x = 0
    y = radius

    d = 1 - radius 

    while x <= y:
        points.append((x_center + x, y_center + y))
        points.append((x_center - x, y_center + y))
        points.append((x_center + x, y_center - y))
        points.append((x_center - x, y_center - y))
        points.append((x_center + y, y_center + x)) 
        points.append((x_center - y, y_center + x)) 
        points.append((x_center + y, y_center - x)) 
        points.append((x_center - y, y_center - x)) 

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1  
        x += 1  
    return points



def draw_circle(points):
    circle = turtle.Turtle()
    circle.speed(1000)
    circle.penup()
    circle.goto(points[0][0], points[0][1])
    circle.pendown()
    
    for point in points[1:]:
        circle.goto(point[0], point[1])
    
    circle.penup()
    
    circle.goto(points[0][0], points[0][1])
    circle.dot(8, 'green')  # Center point
    turtle.done()




x1,y1 = map(float, input("Enter the coordinates of the center (x1, y1): ").split())

radius = float(input("Enter the radius of the circle: "))
points = Mid_point_Circle(x1, y1, radius)
draw_circle(points)