# Exercise 7 solution

# Q1. Print 1-12
# we don't want to repeat code:
# print("1")
# print("2")
# print("3")
# ...

# so we write a loop to get the computer to do work for us
# because we need to run a specific number of time (12 times):
# we use the for loop
for i in range(1,13):     # 1,2,3,4 ... 12
    print(i)

# Q2. count down sequence
for i in range(10,-1,-1):     # 10,9,8...0
    print(i)          # this statement is part of the loop
print ("blast off")   # this statement is not part of the loop
                      # because it should only run once

# Q3. write a function that sums up 1-n values
def addUp (n):
    '''
    add from 1 to n: 1 + 2 + 3 + 4 + ... + n
    input: integer n
    return: total
    '''
    # we can't guess what n is, so using an if statement won't work:
    # if n == 2:
    # total = 1 + 2
    # elif n == 3:
    # total = 1 + 2 + 3
    # elif n == 4:
    # total = 1 + 2 + 3 + 4
    # ...
    # but we notice that we keep adding into the total, up to n times

    # therefore we use a for loop
    total = 0    # before adding, total is 0
    for i in range(1,n+1):      # i: 1,2,3,4...n
        total = total + i       # i = 1, total = 1
                                # i = 2, total = 3
                                # i = 3, total = 6 ...
        # total is called a running sum: we're calculating the sum
        # as the code runs.
    return total

    
val = addUp(10)     # call addUp and store return value
print(val)          # print return value



#Q4
def drawTriangle(t, length, color):
    ''' draw a triangle of specified length and color'''
    t.color(color)
    for i in range(3):
        t.left(360 / 3)
        t.forward(length)

# steps for writing a loop:
# 1. recognize what statements need to be repeated.
# 2. put these statements together and indent them.
#    You are creating the loop body.
# 3. think about loop control: does it need to repeat
#    a certain number of times   or   until a condition becomes true?
#           (for)                            (while)
# 4. go to the line above the loop body and put in your loop control


#Q5
def drawPentagon(t, length, color):
    ''' draw a pentagon of specified length and color'''
    t.color(color)
    for i in range(5):
        t.left(360 / 5)
        t.forward(length)


# driver code for Q4 and Q5
from turtle import *
t = Turtle()
drawTriangle(t, 40, "red")
drawPentagon(t, 50, "blue")









