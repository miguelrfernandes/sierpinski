# import turtle
from turtle import *
from random import random

# Koch Snowflake
def koch(length, depth):
    if depth == 0:
        (r,g,b) = (0,0,0)
        while(r < 0.5 or g < 0.5 or b < 0.5):
            (r,g,b) = (random(), random(), random())
        color(r,g,b)
        forward(length)
    else:
        koch(length/3, depth-1)
        left(60)
        koch(length/3, depth-1)
        right(120)
        koch(length/3, depth-1)
        left(60)
        koch(length/3, depth-1)

# set up screen
setup(600,600)
# set up turtle
speed(0)
hideturtle()
penup()
goto(-200, -100)

# set background color to transparent
bgcolor("black")
width(0.5)
pendown()

koch(400, 5)

# save image
ts = getscreen()
ts.getcanvas().postscript(file="koch.eps")

done()