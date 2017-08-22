from turtle import *


class MastermindOutput:
    def __init__(self):
        self.t = Turtle()
        self.t.home()
        self.t.ht()
        self.t.penup()

    def drawUserGuess(self, color, times):
        self.t.goto(-150, 300 - (times * 70))
        i = 0
        while i < len(color):
            self.drawCircle(self.convert(color[i]), 30)
            self.t.forward(60)
            i += 1
            
    def convert(self, color):
        return {
            'r': 'red',
            'g': 'green',
            'b': 'blue',
            'y': 'yellow',
            'p': 'purple',
            'o': 'orange',
        }[color]

    def drawHints(self,hinta, hintb, times):
        self.t.goto(100, 300 - (times * 70))
        i = 1
        j = 1
        while i <= hinta:
            self.drawCircle("black", 10)
            self.t.forward(30)
            i += 1
 
            
        while j <= hintb:
            self.drawCircle("grey", 10)
            self.t.forward(30)
            j += 1

           

    def drawCircle(self, color, radius):
        self.t.pendown()
        self.t.fillcolor(color)
        self.t.begin_fill()
        self.t.color(color)
        self.t.circle(radius)
        self.t.end_fill()
        self.t.penup()

    def clean(self):
        self.t.clear()
        
        
