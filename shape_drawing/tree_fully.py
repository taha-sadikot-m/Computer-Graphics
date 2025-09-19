import turtle

tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(0)  # Reduced speed to see the drawing process (1-10, where 1 is slowest)
tina.setheading(90)
tina.penup()
tina.backward(200)
tina.pendown()
tina.getscreen().colormode(255)
tina.hideturtle()
tina.tracer(0) #to enable animation - this was making it draw instantly

def branch(d, a, s, cutoff=5):
    if d > cutoff:
        tina.right(a)
        tina.forward(d)
        branch(s * d, a, s, cutoff=cutoff)
        tina.backward(d)
        tina.left(a)

        tina.left(a)
        tina.forward(d)
        branch(s * d, a, s, cutoff=cutoff)
        tina.backward(d)
        tina.right(a)


def colorbranch(d, a, s, cutoff=5, color=(0,0,0)):
    tina.pencolor(color)
    if d > cutoff:
        tina.right(a)
        tina.forward(d)
        colorbranch(s * d, a, s, cutoff=cutoff, color=( int(color[0]-d)%255, color[1], color[2]))
        tina.backward(d)
        tina.left(a)

        tina.left(a)
        tina.forward(d)
        colorbranch(s * d, a, s, cutoff=cutoff, color=( color[0], int(color[1]-d)%255, color[2]))
        tina.backward(d)
        tina.right(a)


def skewcolorbranch(d, a, s, cutoff=5, color=(0,0,0)):
    tina.pencolor(color)
    if d > cutoff:
        tina.right(a*1.5)
        tina.forward(d)
        skewcolorbranch(s * d, a, s, cutoff=cutoff, color=( int(color[0]-d)%255, color[1], color[2]))
        tina.penup()
        tina.backward(d)
        tina.pendown()
        tina.left(a*1.5)

        tina.left(a/1.5)
        tina.forward(d)
        skewcolorbranch(s * d, a, s, cutoff=cutoff, color=( color[0], int(color[1]-d)%255, color[2]))
        tina.penup()
        tina.backward(d)
        tina.pendown()
        tina.right(a/1.5)


tina.forward(100)
skewcolorbranch(80, 30, .8, cutoff=5)
tina.backward(100)
# Removed getscreen().update() since we're not using tracer(0) anymore

tina.getscreen().exitonclick()