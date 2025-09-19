#draw the kite using turtle in python in computer graphics
import turtle

def draw_kite():
    turtle.speed(3)
    turtle.color("blue")
    turtle.begin_fill()
    
    # Draw the kite shape (diamond/rhombus)
    # Start from the top point and go clockwise
    turtle.setheading(90)  # Point upward
    turtle.goto(0, 100)    # Top point
    turtle.goto(60, 0)     # Right point
    turtle.goto(0, -80)    # Bottom point
    turtle.goto(-60, 0)    # Left point
    turtle.goto(0, 100)    # Back to top point
    
    turtle.end_fill()
    
    # Draw small triangle at bottom of kite (stabilizer)
    turtle.penup()
    turtle.goto(0, -80)    # Start from bottom point of kite
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.goto(-15, -120)  # Left point of triangle
    turtle.goto(15, -120)   # Right point of triangle
    turtle.goto(0, -80)    # Back to bottom of kite
    turtle.end_fill()
    
    # Draw the cross lines inside the kite
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.color("white")
    turtle.pensize(2)
    turtle.goto(0, -80)    # Vertical line
    
    turtle.penup()
    turtle.goto(-60, 0)
    turtle.pendown()
    turtle.goto(60, 0)     # Horizontal line
    
    # Reset pen settings for tail
    turtle.pensize(1)
    turtle.color("red")
    
    
    
    
    
    # Hide the turtle and finish
    turtle.hideturtle()
    turtle.done()


draw_kite()