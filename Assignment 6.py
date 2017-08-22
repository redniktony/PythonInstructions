"""
Yanxi Zheng - Assignment 6
"""

from random import *   


"""
getPrice function is used to return a random price number
"""
def getPrice():                             
    price = uniform(0, 100)
    price = round(price, 2)
    print("The price is: $" + str(price))
    return price


"""
calcPayment function is used to calculate the payment
"""
def calcPayment(price):
    try:                                            #try to catch the error for non numeric value
        payment = float(input("Enter your payment:"))   
    except:
        print("You must enter a numeric value")
    if payment >= price:                            #Compare the payment and price
        payment -= price
        payment = round(payment, 2)
        print("Here's your change of $" + str(payment))
        return
    elif payment >= 0:                            #Compare price with 0
        price -= payment
        price = round(price, 2)
        print("That's not enough. You need $" + str(price) + " more")
        return
    else:
        print("Payment must be a positive value larger than price")


        
calcPayment(getPrice())  #call the function
