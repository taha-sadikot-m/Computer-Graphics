import turtle

def midpoint_ellipse(x_center, y_center, rx, ry): 
    points = []
    x = 0
    y = ry 

    # Initial decision parameter for Region 1
    p1 = (ry**2) - (rx**2 * ry) + (0.25 * rx**2) 
    
    # Increments for decision parameters
    tworysq = 2 * (ry**2) 
    tworxsq = 2 * (rx**2) 
    dx = 0
    dy = tworxsq * y

    # Region 1 (slope between 0 and -1)
    while dx <= dy: # Continue until the slope becomes less than -1
       
        # Plot points in all four quadrants due to symmetry
        points.append((x_center + x, y_center + y))
        points.append((x_center - x, y_center + y))
        points.append((x_center + x, y_center - y))
        points.append((x_center - x, y_center - y))

        if p1 < 0:
            x += 1
            dx += tworysq # Increment in x
            p1 += (tworysq * x) + (ry**2) 
        else:
            x += 1
            y -= 1
            dx += tworysq 
            dy -= tworxsq # Decrement in y
            p1 += (tworysq * x) - (tworxsq * y) + (ry**2) 


    # Initial decision parameter for Region 2
    p2 = (ry**2 * (x + 0.5)**2) + (rx**2 * (y - 1)**2) - (rx**2 * ry**2)

    # Region 2 (slope between -1 and 0)
    while y >= 0:

        # Plot points in all four quadrants due to symmetry
        points.append((x_center + x, y_center + y))
        points.append((x_center - x, y_center + y))
        points.append((x_center + x, y_center - y))
        points.append((x_center - x, y_center - y))

        if p2 > 0: # Check if midpoint is outside or on the ellipse boundary
            y -= 1
            dy -= tworxsq 
            p2 += (rx**2) - (tworxsq * y)
        else: # Check if midpoint is inside the ellipse boundary
            x += 1
            y -= 1
            dx += tworysq
            dy -= tworxsq
            p2 += (tworysq * x) - (tworxsq * y) + (rx**2) 

    return list(set(points))  # Remove duplicate points


def draw_ellipse_turtle(points):
    screen = turtle.Screen()
    screen.setup(800, 600)
    my_turtle = turtle.Turtle()
    my_turtle.speed(-100)
    my_turtle.hideturtle()
    my_turtle.penup() # Lift the pen to avoid drawing lines while moving to the first point
    
    # Draw points individually
    for point in points:
        my_turtle.goto(point[0], point[1])
        my_turtle.pendown()
        my_turtle.dot(10, 'blue')
        

    turtle.done()


# Take input and call functions
x_center = int(input("Enter the x-coordinate of the center of the ellipse: "))
y_center = int(input("Enter the y-coordinate of the center of the ellipse: "))
rx = int(input("Enter the x-radius of the ellipse: "))
ry = int(input("Enter the y-radius of the ellipse: "))

points = midpoint_ellipse(x_center, y_center, rx, ry)
draw_ellipse_turtle(points)
