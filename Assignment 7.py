from turtle import *

def driver():   #driver is a function to drive all the funtions
    t = Turtle()
    t.color("red")
    size = getSize()
    while size != 0: 
        num = getNumSides()
        t.begin_fill()
        drawPolygon(t, size, num)
        t.end_fill()
        size = getSize()
    return

def drawPolygon(t, size, num):  #drawPolygon is a function to draw polygon
    for i in range(num):
        t.left(360/num)
        t.forward(size)
    return

def getSize():  #getSize is a function to get size
    size = int(input("Enter size of polygon (50-150) :"))
    while 50 > size or size > 150 or size == 0:
        if size == 0:
            return size
        print("Error: size must be between 50 and 150")
        size = int(input("Enter size of polygon (50-150) :"))
    return size

def getNumSides():  #getNumSides is a function to get number of side
    num = int(input("Enter number of sides of polygon (3-10) :"))
    while 3 > num or num > 10:
        print("Error: size must be between 3 and 10")
        num = int(input("Enter number of sides of polygon (3-10) :"))
    return num


driver()  #Call driver function
