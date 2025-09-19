import turtle 


smiley = turtle.Turtle()


smiley.penup() 
smiley.goto(0, -100)
smiley.pendown() 
smiley.fillcolor('yellow')
smiley.begin_fill() 
smiley.circle(100) 
smiley.end_fill() 


def eye(col, rad): 
    smiley.down() 
    smiley.fillcolor(col) 
    smiley.begin_fill() 
    smiley.circle(rad) 
    smiley.end_fill() 
    smiley.up() 

smiley.penup() 
smiley.goto(-40, 50) 
eye('white', 15) 
smiley.goto(-37, 55) 
eye('black', 5) 

smiley.goto(40, 50)
eye('white', 15) 
smiley.goto(37, 55) 
eye('black', 5) 


smiley.penup() 
smiley.goto(-40, 0) 
smiley.pendown() 
smiley.right(90) 
smiley.circle(40, 180)



turtle.done()
