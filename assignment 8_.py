#Teng Ma and Yanxi Zheng

def addClass():  #prompt the user for a class number, class name, class day and timappend the new class information
    file = open("lab8input.txt", "a")
    cla = str(input("Enter class number to add: "))
    name = getName()
    file.write(cla + '\t' + name + '\t' + getDayOrTime() + "\n")
    print("Added " + name + "\n")
    file.close()
    return

def getName():   #prompt the user for a class name keyword for searching
    name = str(input("Enter class number: "))
    return name

def getDayOrTime(): #prompt the user for a day or time of the class to be searched
    dayTime = str(input("Enter class day and time: "))
    return dayTime

def searchClass(): #accept 2 input arguments: the name and the day/time values
    count = 0
    file = open("lab8input.txt")
    cla = str(input("Enter class name to search: "))
    dayTime = str(input("Enter class day and time: "))

    print("Class(es) matching " + cla + " and " + dayTime)
    for line in file:
        if line.find(cla)!= -1 and line.find(dayTime)!=-1:
            print(line, end="")
            count = count +1
    if count != 0:
        print("Total:" , count , "classes")
    else:
        print("No match")

    file.close()
    return

def driver():
    addClass()
    searchClass()
    c = str(input("Continue? y/n: "))
    while c == "y":
        searchClass()
        c = str(input("Continue? y/n: "))

driver()
