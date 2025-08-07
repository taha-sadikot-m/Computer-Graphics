import matplotlib.pyplot as plt
import numpy as np
import turtle




def Besherman_circle(x_center, y_center, radius):
    points = []
    x = 0
    y = radius 
    d = 3 - (2 * radius) 

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
            d = d + (4 * x) + 6
        else:
            y -= 1 
            d = d + (4 * (x - y)) + 10     
        x += 1
        
    return list(set(points)) 




def draw_circle(points): 
    circle  = turtle.Turtle()
    circle.speed(1000)  
    circle.penup()
    circle.goto(points[0][0], points[0][1])
    circle.pendown()
    for point in points[1:]:
        circle.goto(point[0], point[1])
    circle.penup()
   
    circle.goto(points[0][0], points[0][1])
    circle.dot(8, 'green') 
    circle.fillcolor('yellow')
    circle.begin_fill() 
    circle.end_fill()  

    turtle.done()






x1,y1 = map(float, input("Enter the coordinates of the center (x1, y1): ").split())

radius = float(input("Enter the radius of the circle: "))

points = Besherman_circle(x1, y1, radius)
draw_circle(points)
