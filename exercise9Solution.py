# Partial solution to module 9 exercise

# 1. Create a list called L1 with the value 'x', 'y', 'z'
#   Show the type of L1
L1 = ['x', 'y', 'z']
print(L1)           # at the shell we don't need print:  >>> L1     
print(type(L1))     # at the shell we don't need print:  >>> type(L1)
print()

# 2. Create a list called L2 with the values 10 - 25
#   Print the first element of L2
#   Print the fifth element of L2
#   Find 2 ways to print the last element of L2
#   Find 2 ways to print the next to last element of L2
L2 = list(range(10,26))   # range output: 10,11,12,...,25
print(L2)
print(L2[0])    # first element at index 0
print(L2[4])    # fifth element at index 4 (counting starts at 0)
print(L2[-1], L2[15])     # last element, 2 ways
print(L2[-2], L2[14])     # next to last element, 2 ways
print()

#################  Add to list    ###########################
	
#3. Print L1 and L2 together as one list
#   Does L1 or L2 change? 
#   Create L3, which is L1 and L2 combined together as one list
#   Find 2 ways to append L1 to L2, so L2 has elements of L2 followed
#   by elements of L1 
print(L1, L2)   # print 2 different lists: L1 then L2
print(L1 + L2)  # print 1 list, and L1 and L2 don't change
L3 = L1 + L2    # create new L3 which is made of L1 and L2

#L2.extend(L1)  # first way to add L1 to the end of L2
L2 = L2 + L1    # second way to add L1 to the end of L2
print(L2)
print()


#4. Print L3
print(L3)
#   For L3, print elements at index 5 to 9
print(L3[5:10])
#   For L3, print all elements except the first 4
print(L3[4:])     # start at 4, end at last index
#   For L3, print the first 4 elements
print(L3[:4])     # start at 0, end at 3
#   For L3, print all elements except the last 4
print(L3[:-4])    # start at 0, end at -5
#   For L3, print the last 4 elements
print(L3[-4:])    # start at -4, end at last index
#   Does L3 change?
# L3 does not change because slice is an operator
print()

####### and do step 5 to wrap up how to add to a list
#5. Print L1
print(L1)
#   Append 'end' to L1
L1.append('end')
print(L1)
#   Add 'start' to the beginning of L1
L1.insert(0, 'start')
print(L1)
#   Add 'middle' to the middle of L1
L1.insert(int(len(L1)/2), 'middle')
print(L1)
#   What happens if we run:  L1.extend('final')
#L1.extend('final')     # extend is used with a list, therefore
                        # 'final' is turned into a list of 5 characters
                        # and the 5 characters are added to L1 as 5
                        # separate elements
#print(L1)
#   Does L1 change?
# yes because append and insert are methods
print()



################# remove from list  ################
#6. Print L2
print(L2)
#   Remove the first element of L2
L2.pop(0)
print(L2)
#   Find 2 ways to remove the last element of L2
L2.pop(-1)             # last element
#L2.pop(len(L2)-1)      # last element index is 1 less than length of list
L2.pop()     # shortest way, use this one
print(L2)
#   Remove the 5th element of L2
L2.pop(4)
print(L2)
#   Remove the element 'x'
L2.remove('x')
print(L2)
#   Remove the element 'z'
#L2.remove('z')     # causes exception because 'z' is not in the list.
                    # Moral of the story: Check first before running remove
#   Does L2 change?
# yes because pop and remove are methods
print()


##################  copy and sort list  ############
#7. Print L1
print(L1)
#   copy L1 to L1Copy
#L1Copy = L1     #### this creates another name for L1. It is NOT A COPY!
L1Copy = L1[:]   # This tells Python to copy from first to last elements
                 # into L1Copy, creating a new list
print(L1)
print(L1Copy)
#   sort L1
L1.sort()
#   Does L1 change?
print(L1)       # yes, it's sorted
#   Does L1Copy change?
print(L1Copy)   # no, it's a different list than L1 and was not sorted
print()	

##################   search list  ###################
#8. Print L3
print(L3)
#   Check if 22 is in L3
print(22 in L3)
#   Check if 28 is in L3
print(28 in L3)
#   Check the index of 22
print(L3.index(22))
#   Check the index of 28
# print(L3.index(28))  # causes exception because 28 is not in the list.
                       # Moral of the story: Check first before running index
print()

#############  list and string  ###################
#9. Print L1
#   Remove all but the last 3 elements of L1
L1 = L1[-3:]
print(L1)
#   Convert L1 into a string with value 'xyz'
#L1.split()
outStr = ''
print(outStr.join(L1))
#   Create a string called myStr with the data "lists are fun"
myStr = "lists are fun"
#   Convert myStr into a list L4
L4 = myStr.split()
print(L4)
#   Review: "split" the first word to print each character on one line
for character in L4[0]:
    print (character)


