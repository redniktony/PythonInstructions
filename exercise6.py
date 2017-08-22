# exercise 6: if statements

# drawCircle
def drawCircle(t, radius, color):
    ''' draw a circle of specified radius and color'''
    t.color(color)
    t.circle(radius)

# fillCircle
def fillCircle(t, radius, borderColor, fillColor):
    ''' draw a circle of specified radius and colors'''
    t.begin_fill()
    t.pensize(4)
    drawCircle(t, radius, borderColor)
    t.pensize(1)
    t.fillcolor(fillColor)
    t.end_fill()

# drawTriangle
def drawTriangle(t, length, color):
    ''' draw a circle of specified radius and color'''
    t.color(color)
    t.left(360 / 3)
    t.forward(length)
    t.left(360 / 3)
    t.forward(length)
    t.left(360 / 3)
    t.forward(length)



# test driver code

from turtle import *
t = Turtle()

