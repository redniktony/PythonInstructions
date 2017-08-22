# Assignment 10:
# Transcript class that prints class list and GPA for one quarter
class Transcript:
    def __init__(self, quarter, classes):
        '''
        initialize  the class list and quarter attributes with the input values
        input: a string that is the name of the quarter
        a list of classes
        return: nothing
        '''
        self.quarter = quarter
        self.classes = classes
        return

    def __str__(self):
        '''
        convert object to a string
        This method is called by Python whenever it needs a string from the object
        input: a string that is the name of the quarter
        return: a string to identify that the object is a transcript for a specific quarter
        '''
        return "Transcript for " + str(self.quarter)

    def print(self):
        '''
        prints the quarter on the first line
        for each class in the class list, print the class name on the first line,
        then print the units and the letter grade on the second line
        prints the total number of classes
        prints the GPA

        input: nothing
        return: nothing
        '''
        
        print("\t" + self.quarter)
        i = 0
        while i < len(self.classes):
            print("Class name:", self.classes[i][0])
            print("Units:", self.classes[i][1], "\tGrade:", self.classes[i][2],"\n")
            i = i + 1
        print("Total number of course: " + str(len(self.classes)))
        
        print("GPA: " + self.calcGPA() + "\n\n")
        return 

    def calcGPA(self):
        '''
        calculates the GPA from the data in the class list and returns the gpa
        To calculate the GPA:

        multiply the number of units and the numeric grade for each class
        sum up all the results of the previous step, then divide by the total number
        of units
        input: units and grades
        return: gpa
        '''
        i = 0
        self.unit = 0
        self.gpa = 0
        while i < len(self.classes):
            self.gpa = self.gpa + float(self.classes[i][1]) * float(self.getNumericGrade(self.classes[i][2]))
            self.unit = float(self.unit) +  float(self.classes[i][1])
            i = i + 1
        self.gpa = str(round(self.gpa / self.unit, 2))
        return self.gpa

    def getNumericGrade(self, grade):
        '''
        use the letter grade equivalence:
        input: nothing
        return:  an equivalent numeric grade for the input letter grade 
        '''
        
        return{
            'A+':4,
            'B+':3.3,
             'C+':2.3,
            'D+':1.3,
            'F':0,
            'A':4,
            'B':3,
            'C':2,
            'D':1,
            'A-':3.7,
            'B-':2.7,
            'D-':0.7,
            }[grade]



# test driver code
# first Transcritpt object
classList = [ ['CIS 40', 4.5, 'A'], ['Math 10', 5, 'B+'], ['Econ 1', 4, 'B'] ]
w17 = Transcript('Winter 17', classList)
print(w17)
w17.print()

# Second Transcript object
classList = [ ['Math 114', 5, 'C+'], ['PE 32', 2, 'A'] ]
f16 = Transcript('Fall 16', classList)
print(f16)
f16.print()
