#Teng Ma an YanxiZheng

def printList(task): #To print all the tasks in the list
    print("Tasks:")
    print("-----")
    for i in task:
        k = task.index(i) + 1
        print(k,i)
    return

def add(task):     #To add the task in the list
    element = str(input("Enter a task to add "))
    num = int(input("Add after task number? " ))
    if num > len(task) or num < 0:
        print("Between 0 and", len(task), "only")
    else:
        task.insert(num, element)
        print("")
        printList(task)

    con = str(input("Continue to add? y/n: "))
    return con


def delete(task):       #To delete the task in the list
    num = str(input("Delete task number? "))
    num = num.split()
    
    if len(num) == 1:
        num = int(num[0])
        if num > len(task) or num <= 0:
            print("No task number", num)
            con = str(input("Continue to delete? y/n: "))
            return con
        else:
            num = num - 1
            task.pop(num)
           
    elif len(num) == 3:
        a = int(num[0]) - 1
        b = int(num[2]) - 1
        if a >= 0 and b < len(task):
            for i in range(b, a - 1, -1):
                task.pop(i)
    
    print("")
    printList(task)
    con = str(input("Continue to delete? y/n: "))
    return con

def search(task):           #To search the task in the list
    element = str(input("Enter task to search "))
    if element in task:
        print(element, "is task number", str(task.index(element)+1))
    else:
        print("No such task")

    con = str(input("Continue to search? y/n: "))           
    return con

def driver(): #To run all the procedure
    task = ['game', 'program', 'lunch']
    printList(task)

    
    con = add(task)
    while con == 'y':
        con = add(task)
          
    con = delete(task)
    while con == 'y':
        con = delete(task)
    
    con = search(task)
    while con == 'y':
        con = search(task)
    
    return
        

driver()
