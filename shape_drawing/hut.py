#write a turtle program in computer graphics to draw a hut

import turtle

def draw_hut():
    # Draw the base of the hut
    turtle.fillcolor("brown")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(200)
        turtle.right(90)
    turtle.end_fill()
    
    # Draw the roof of the hut (moved down 200px)
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.goto(0, 0)
    turtle.goto(100, 100)
    turtle.goto(200, 0)
    turtle.goto(0, 0)
    turtle.end_fill()
    
    # Draw the door (moved down 200px)
    turtle.penup()
    turtle.goto(75, -200)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()
    
    # Draw windows (moved down 200px)
    for x in [30, 130]:
        for y in [-150, -100]:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.fillcolor("blue")
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(30)
                turtle.right(90)
            turtle.end_fill()
    
    # Hide the turtle and finish
    turtle.hideturtle()
    turtle.done()


draw_hut()

