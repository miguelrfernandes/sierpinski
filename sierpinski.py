# import turtle
from turtle import *
from random import random
from math import cos, sin

MAGNIFICATION = 2
SPEED = 2

canvas = Screen().getcanvas()
# set up screen
setup(800, 800)
screensize(800 * MAGNIFICATION, 800 * MAGNIFICATION)

#Sierpinski Triangle
def sierpinski(length, depth):
    if depth == 0:
        (r, g, b) = (random(), random(), random())
        while(r < 0.5 or g < 0.5 or b < 0.5):
            (r, g, b) = (random(), random(), random())
        color(r,g,b)

        for i in range(0,3):
            forward(length)
            left(120)
            angle = i * 120
            x = xcor() + length * cos(angle)
            y = ycor() + length * sin(angle)
            canvas.create_line(xcor(), ycor(), x, y)
            canvas.xview_scroll(int(cos(angle) * length), "p")
            canvas.yview_scroll(int(sin(angle) * length), "p")
    else:
        sierpinski(length/2, depth-1)
        forward(length/2)
        sierpinski(length/2, depth-1)
        backward(length/2)
        left(60)
        forward(length/2)
        right(60)
        sierpinski(length/2, depth-1)
        left(60)
        backward(length/2)
        right(60)


# set up turtle
speed(SPEED)
hideturtle()
penup()
goto(-200, -100)


bgcolor("black")
color('red', 'yellow')
width(0.5)
pendown()
sierpinski(400, 3)

# save image
ts = getscreen()
ts.getcanvas().postscript(file="sierpinski.eps")

done()
