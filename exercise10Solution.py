# exercise 10: class Circle definition

from turtle import *

class Circle:
    def __init__(self, size):
        '''
        initialize attributes of Circle object
        input: current object and size of object
        return: nothing
        '''
        self.size = size      # set size of object to input size
        self.x = 0            # starting position at (0,0)
        self.y = 0            #   (x,y) could be initialized to other values
        self.t = Turtle()          # create turtle object
        #t.color("blue")
        self.color = "blue"   # set color to blue, could be other colors

    def __str__(self):
        '''
        convert object to a string
        This method is called by Python whenever it needs a string from the object
        input: current object
        return: nothing
        '''
        return self.color     # return the color of the object
        # extra credit:
        # change the return value so that the print in the driver code
        # will print:  blue 40
        return self.color + ' ' + str(self.size)

    def draw(self):
        '''
        draw a circle with the object color, size, and coordinates
        input: nothing
        return: nothing
        '''
        self.t.color(self.color)       # set turtle color to object's color
        self.t.circle(self.size)       # set turtle size to object's size
        # optional: move the turtle to correct location if it's not already
        #           done by setPosition
        #self.t.penup()   
        #self.t.goto(self.x, self.y)
        #self.t.pendown()

    def fill(self):
        '''
        draw a filled circle with the object color, size, and coordinates
        input: nothing
        return: nothing
        '''
        self.t.begin_fill()
        self.draw()           # call the object's draw method
                              # so we don't have to repeat the code of draw()
        self.t.end_fill()

    def setPosition(self, x, y):
        '''
        set object's position attributes 
        input: x and y coordinates (int)
        return: nothing
        '''
        self.x = x
        self.y = y
        # set the object's turtle object to the new position
        self.t.penup()
        self.t.goto(x,y)   # only because we're inside setPosition
        self.t.pendown()
        

    def setColor(self, color):
        '''
        set object's color attribute
        input: color (string)
        return: nothing
        '''
        self.color = color

'''
It's important to test each method as we add the code for it.
Don't write the entire class with all methods, and then test.
It will be more of a headache to debug than to test each method.

testing code as we write each method
myCircle = Circle(40)     # test __init__
print(myCircle)           # test __str__
myCircle.draw()           # test draw
myCircle.fill()           # test fill
'''

# driver code:
myCircle = Circle(40)           # create circle of size 40
myCircle.setPosition(50, 50)    # set position
myCircle.setColor("red")        # set color
myCircle.fill()                 # draw filled circle
print(myCircle)                 # print description of object

myCircle.setPosition(0,0)       # set position
myCircle.setColor("blue")       # set color
myCircle.draw()                 # draw circle

'''
Note that we invested time to create a class Circle
so that we can take advantage of having an easy way to draw circles.
After the Circle class is created, we can use it any time we want
to draw circles.

As the user of the Circle class, we only need to set the color and
position, and then call draw() or fill(). We don't need to know any
of the details of how the circle is drawn.

This is similar to how we use the list class. After we create the list
object, we can start calling append() or pop() without having to know
how to append or how to pop data from the list.

Using classes such as list or Circle allows us to build on existing code
(that are in the classes) so that we can solve problems faster.
And that's what makes Python so great - and popular.
'''
