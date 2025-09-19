import turtle
fish_scr = turtle
fish_scr.speed(10)


def Draw_Fish(i,j):
    fish_scr.penup()
    fish_scr.goto(i,j)
    fish_scr.left(45)
    fish_scr.pendown()
    
    # Draw fish body with orange color
    fish_scr.color('orange', 'orange')
    fish_scr.begin_fill()
    fish_scr.forward(100)
    fish_scr.right(135)
    fish_scr.forward(130)
    fish_scr.right(130)
    fish_scr.forward(90)
    fish_scr.left(90)
    fish_scr.right(90)
    fish_scr.circle(200,90)
    fish_scr.left(90)
    fish_scr.circle(200,90)
    fish_scr.end_fill()
    
    # Draw fish eye with white background and black center
    fish_scr.penup()
    fish_scr.left(130)
    fish_scr.forward(200)
    fish_scr.pendown()
    fish_scr.color('white', 'white')
    fish_scr.begin_fill()
    fish_scr.circle(10,360)
    fish_scr.end_fill()
    
    # Draw black center of eye
    fish_scr.penup()
    fish_scr.forward(5)
    fish_scr.pendown()
    fish_scr.color('black', 'black')
    fish_scr.begin_fill()
    fish_scr.circle(3,360)
    fish_scr.end_fill()
    
    # Reset position for fin
    fish_scr.penup()
    fish_scr.backward(5)
    fish_scr.right(270)
    fish_scr.forward(50)
    fish_scr.pendown()
    
    # Draw fish fin with blue color
   
    fish_scr.begin_fill()
    fish_scr.left(90)
    fish_scr.circle(100,45)
    fish_scr.right(45)
    
    
    # Reset turtle position and orientation
    fish_scr.penup()
    fish_scr.forward(300)
    fish_scr.left(135)
    fish_scr.pendown()
    fish_scr.right(180)

Draw_Fish(0,0)
Draw_Fish(150,150)
Draw_Fish(150,-150)

fish_scr.done()