from turtle import Turtle, Screen
from itertools import cycle

ANGLE = 8

colors = ["orange", "yellow", "tan", "pink", "coral"]

def spiral(turtle, radius, color_names):
    colors = cycle(color_names)

    for _ in range(360 // ANGLE):
        turtle.color(next(colors))
        turtle.circle(radius)
        turtle.left(ANGLE)

yertle = Turtle(visible=False)
yertle.speed("fastest")

spiral(yertle, 50, colors)

screen = Screen()
screen.exitonclick()