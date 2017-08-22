# exercise 5 solution
# functions using turtle graphics

from turtle import * # bring in turtle data and methods so we can use them

# 1a. drawCircle
def drawCircle(t, radius, input_color):
    ''' draw a circle of specified radius and color'''
    t.color(input_color)    # set color to input color
    t.pensize(5)            # set the pen size to thickness of 5
    t.circle(radius)        # draw circle with input radius
       
# 2a. fillCircle
def fillCircle(fred, radius, border_color, fill_color):
    ''' fill a circle of specified radius and border color / fill color '''
    fred.begin_fill()       # tell turtle that we'll fill the following shape
    drawCircle(fred, radius, border_color)    # draw the circle with border color
    fred.fillcolor(fill_color)    # change the color to fill color
    fred.end_fill()         # tell turtle to fill the shape

# 3a. drawTriangle
def drawTriangle(t, length, input_color):
    ''' draw a triange of specified length and color '''
    t.color(input_color)   # set color to input_color
    t.fd(length)           # draw first side
    t.left(120)            # turn to 2nd side
    t.fd(length)           # draw 2nd side
    t.left(120)            # turn to 3rd side
    t.fd(length)           # draw 3rd side
 


# test driver code
t = Turtle()      # create turtle object so we can use it to draw
t.speed(20)       # set speed to 20 so it the turtle draws faster

# 1b. go to quadrant 1 and call drawCircle
t.up()            # pen goes up
t.goto(100, 200)  # move to quadrant 1
t.down()          # pen goes down
                  # Note: without the pen up/pen down: the turtle will draw a line
                  # as it moves from (0,0) to (100,200)
drawCircle(t, 50, "blue")     # draw circle


# 2b. go to quadrant 4 and call fillCircle
t.up()
t.goto(100, -200) # go to quadrant 4
t.down()
fillCircle(t, 80, "purple","green")   # fill circle

# 3b. go to original position and call drawTriangle
t.up()
t.home()          # go to original position (shorter than: t.goto(0,0)
t.down()
drawTriangle(t, 50, "red")    # draw triangle

