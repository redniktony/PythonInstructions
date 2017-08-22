# Solution to module 6 exercise: if statements

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

##############################################
    
# exercise Q2:
def getRadius():
    '''
        read in from the user the radius, check for valid radius,
        and return one of two values
        input: nothing
        return: radius if valid
                -1 if not valid
    '''
    radius = int(input("Enter a radius: "))

    # We discussed 3 different ways to test for
    # invalid / valid radius and then branch out.
    # Un-comment out each of the 3 ways, one at a time,
    # so you can see that they all produce a similar result.

    '''
    # 1. testing for invalid radius
    if radius < 1 or radius > 150:
        print ("invalid radius")
        return -1
    else:    # radius is valid
        return radius
    '''
    """
    # 2. testing for valid radius
    if radius >= 1 and radius <= 150:
        return radius
    else:   # radius is invalid
        print ("invalid radius")
        return -1   
    """
    # 3. testing for valid radius
    if 1 <= radius <= 150:    # short cut of case 2
        return radius
    else:   # radius is invalid
        print ("invalid radius")
        return -1   
    
    # We also discussed this condition:
    #    if radius < 1 and radius > 150:
    # which seems like a reasonable statement for
    # testing for invalid radius, but logically there's
    # no number that can be both   < 1  AND   > 150   at
    # the same time. So this condition is never useful as a test.
    # Moral of the story: when your code doesn't seem to
    # make the right decision, check your "and" vs "or"


# exercise Q4:
def getColor():
    '''
        read in from the user the color red, green, or blue,
        check for valid color, and return one of two values
        input: nothing
        return: color if valid
                "unknown if not valid
    '''
    color = input("Enter a color of red, green, or blue: ")

    # there are 2 ways to write the code to check for valid color.
    # Uncomment one block at a time to see that it runs.
    '''
    # 1. check each valid color with if elif (used to choose one choice
    # out of many choices)
    if color == "blue":
        return color
    elif color == "red":
        return color
    elif color == "green":
        return color
    else:       # anything else is invalid color
        print "Invalid color"
        return "unknown"
    '''

    # 2. check for invalid color
    if color != "green"   and   color != "red"  and   color != "blue":
        print ("Invalid color")
        return "unknown"
    else:   # valid color
        return color
    

# test driver code

from turtle import *
t = Turtle()

# uncomment out the block for Q3 or Q5 to run it.
'''
# exercise Q3
r = getRadius()          # call getRadius, store return value in r
if r != -1:              # if getRadius doesn't return -1 (valid radius)
    drawCircle(t, r, "orange")
'''

'''
# exercise Q5
r = getRadius()          # call getRadius and catch return value
if r != -1:              # if return value shows valid size
    c = getColor()            # then call getColor and catch return value
    if c != "unknown":        # if return value shows valid color
        drawCircle(t, r, c)         # then draw circle

                         # Note that the above is a nested if statement:
                         # inside the True block of if r!= -1 is another if statmement.
                         # Note also that there is no else block. The error printing
                         # is already done by the getRadius or getColor functions.                   
'''

# exception handling:
num1 = 5
num2 = 0
try:
    num1 = num1 / num2  # put the division in the try block because it's possible
                        # that num2 is 0, and divide by 0 is not possible.
                        # When the CPU cannot run the instruction successfully, it will
                        # "throw" an exception.
                        # If we don't "catch" the exception with try...except, then
                        # the exception message will, by default, be printed to screen
                        # and the program will stop.
except:
    print ("Can't divide by 0. Give me another num2 value")
                        # By using try...except, we tell Python to catch the exception,
                        # and then we can handle the exception however we want, and the
                        # program will keep running.

print(num1, num2)

# Two test cases that you should run to test the exception handling:
# 1. set:  num2 = 2
# Here is the order of statements being run:
#   num1 / num2 => 2.5 is result
#   store 2.5 into num1
#   no exception, skip the except block
#   print num1 and num2:   2.5  2
#   end of program

# 2. set:  num2 = 0
# Here is the order of statements being run:
#   num1 / num2 => exception
#   nothing to store into num1, jump to except block
#   print "Can't divide by 0... " message
#   print num1 and num2:   5  2
#   end of program

