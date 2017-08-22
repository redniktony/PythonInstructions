# solution to exercise 4: functions

def maxAndMin():
    '''
    ask the user for 3 numbers and print the max and min
    input: nothing
    output (return): nothing
    '''
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    n3 = int(input("Enter third number: "))

    print("The max is", max(n1, n2, n3))
    print("The min is", min(n1, n2, n3))
    # or, in one line:
    # print("The max is", max(n1, n2, n3), "and the min is", min(n1, n2, n3))
    

def calcProduct(num1, num2):
    '''
    calculate the product of the 2 input
    input: 2 numbers
    return: product
    '''
    product = num1 * num2
    return product
    # or, in one line:
    # return num1 * num2



# driver code to call the functions and run them
# run first function
maxAndMin()

# set variables to 5 and 8
n1 = 5
n2 = 8
# call calcProduct and save return value (output) in a variable to print
product = calcProduct(n1, n2)
print(n1, "*", n2, "=", product)


