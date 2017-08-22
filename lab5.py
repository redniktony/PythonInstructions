from turtle import *

def initDraw():
    t = Turtle();
    return t

def setPen(t, x, y, borderColor, penColor):
    t.penup()
    t.home()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(borderColor)
    t.pencolor(penColor)
    return

def drawSquare(t, x, y, length, borderColor, penColor):
    setPen(t, x - length / 2, y + length / 2, borderColor, penColor)
    t.begin_fill()
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.end_fill()
    return

def drawRectangle(t, x, y, length, width, borderColor, penColor):
    setPen(t, x - length / 2, y + width / 2, borderColor, penColor)
    t.begin_fill()
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.end_fill()
    return

def drawSemicircle(t, x, y, radius, borderColor, penColor):
    setPen(t, x, y - radius, borderColor, penColor)
    t.begin_fill()
    t.circle(radius, 180)
    t.left(90)
    t.forward(radius * 2)
    t.end_fill()
    return



def draw():
    t = initDraw()
    drawSemicircle(t, 100, 100, 50, "pink", "yellow")
    drawRectangle(t, -200, 0, 50, 100, "violet", "blue")
    drawSquare(t, 300, 0, 100, "spring green", "peach puff")
    setPen(t, -50, -150, "white", "black")
    t.write("Yanxi Zheng", font = 25)
    return

draw()
