# Exercise 8 partial solution

# Q1. create a file with 3 language names
# step 1:
fh = open("languages.txt","w")     # open file handle to languages.txt for writing
                                   # if file doesn't exist, new file is created
                                   # if file exists, it gets overwritten

# step 2:
fh.write("English\n")     # write 3 lines of text
fh.write("whale\n")       # note that we need \n so we can have 3 lines
fh.write("Klingon\n")
# can also use 1 line to write to file:
#    fh.write("English\nwhale\nKlingon\n")
# Use one line or more than one line, whichever is more clear to you.

# step 3:
fh.close()         # close file handle


# Q3. print the 3 languages from the file
# step 1:
fh = open("languages.txt")  # open file handle to languages.txt for reading

# There are 2 ways to read from a file, run each of the ways below by
# commenting out the other way.

# step 2, first way:
print(fh.read(), end='')   # read entire file as 1 line, then print.
                           # The  end=""   tells print not to automatically add \n
                           # after printing everything
'''                        
# step 2, second way:
for line in fh:            # use a loop to read in each line,
    print(line, end="")    # then print each line, making sure than default \n is
                           # not printed (just like above)
'''

print()     # print a blank line
# step 3:
fh.close()


# Q4. add 1 more language to the file and print entire file
fh = open("languages.txt","a")     # open file handle to languages.txt for appending
                                   # if file doesn't exist, new file is created
                                   # if file exists, it gets appended

# step 2:
fh.write("Python\n")     # add 1 more line of text

# step 3:
fh.close()         # close file handle

# now print entire file:
fh = open("languages.txt")  # open file handle to languages.txt for reading
 
# step 2:
count = 1
for line in fh:            # use a loop to read in each line,
    print(count, line, end="")    # then print each line
    count = count + 1

print()    # print blank line

# step 3:
fh.close()


# Q5. Create 3 strings with food names
food1 = "pizza"
food2 = "sausage"
food3 = "veggie"

# Q6. Create a string from 2 of the foods
lunch = food1 + " " + food3     # add space in between the words
print(lunch)

# Q7. print True or False whether a certain food is in lunch
print (food1 in lunch)      # print: True
print (food2 in lunch)      # print: False

# Q8. print whether 'z' is in lunch, and if it's in the 1st or 2nd word
print ("'z' is found at position", lunch.find('z'))
                                  # find will give the position of first 'z'

# if the position of 'z' is less than (or before) position of space
# then 'z' is in the first word
# otherwise 'z' is in the second word
if lunch.find('z') < lunch.find(' '):
    print ("'z' is in first word")
else:
    print ("'z' is in second word")

# Q9. replace 'z' with 'Z'
lunch = lunch.replace('z', 'Z')   # don't forget to store back in the string
print(lunch)


