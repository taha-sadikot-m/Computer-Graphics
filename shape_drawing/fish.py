#draw  a fish using turtle in python in computer graphics
import turtle
def draw_fish():
    turtle.speed(3)
    turtle.color("orange")
    turtle.begin_fill()
    
    # Draw the body of the fish (oval shape)
    turtle.setheading(0)  # Point to the right
    turtle.circle(50, 90)  # Top half of oval
    turtle.circle(100, 90) # Right side of oval
    turtle.circle(50, 90)  # Bottom half of oval
    turtle.circle(100, 90) # Left side of oval
    
    turtle.end_fill()
    
    # Draw the tail of the fish
    turtle.penup()
    turtle.goto(-100, 0)  # Move to the back of the fish body
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.goto(-150, 30)  # Top point of tail
    turtle.goto(-150, -30) # Bottom point of tail
    turtle.goto(-100, 0)   # Back to body
    turtle.end_fill()
    
    # Draw the eye of the fish
    turtle.penup()
    turtle.goto(20, 20)   # Position for eye
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(5)      # Draw eye
    turtle.end_fill()
    
    # Hide the turtle and finish
    turtle.hideturtle()
    turtle.done()


draw_fish()