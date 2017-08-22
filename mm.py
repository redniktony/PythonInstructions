from mOutput import *
from random import *

class Mastermind:
    def __init__(self):
        print("Welcome to Mastermind, the CIS 40 version!")
        seed()
        '''
        self.level = 0
        self.guess = ""
        '''
        self.out = MastermindOutput()
        self.counta = 0
        self.countb = 0
        self.color = []
        self.num = []
        self.num2 = 0
        return

    def levels(self):
        print("Your choices:")
        print("3. beginner level with 3 colors")
        print("4. expert level with 4 colors")
        self.level = int(input("Choose 3 or 4: "))
        while self.level != 3 and self.level != 4:
            print("Please choose number 3 or 4: ")
            self.level = int(input("Choose 3 or 4: "))
        print("Playing at level", self.level)
        return

    def dice(self):
           
        for i in range(self.level):
            self.num2 = randint(1, 6)
            while self.num2 in self.num:
                self.num2 = randint(1, 6)
            self.num.append(self.num2)
            self.color.append(self.convert(self.num[i]))
           

    def convert(self, color):
        return {
            1: 'r',
            2: 'g',
            3: 'b',
            4: 'y',
            5: 'p',
            6: 'o',
        }[color]

    def guessNum(self):
        print("r = red, g = green, b = blue, y = yellow, p = purple, o = orange")
        if self.level == 3:
            self.guess = str(input("Type different 3 letters in the order of your 3 choices: "))
            self.guess = list(self.guess)
            self.count = 1
            while self.checkRepeat() == False:
                self.guess = str(input("Type 3 different letters in the order of your 3 choices: "))
                self.guess = list(self.guess)
                self.count += 1
        else:
            self.guess = str(input("Type different 4 letters in the order of your 4 choices: "))
            self.guess = list(self.guess)
            self.count = 1
            while self.checkRepeat() == False:
                self.guess = str(input("Type 4 different letters in the order of your 4 choices: "))
                self.guess = list(self.guess)
                self.count += 1

    def checkRepeat(self):
        for i in range(self.level - 1):
            times = self.level - i - 1
            for j in range(times):
                if self.guess[i] == self.guess[j + i + 1]:
                    print("The letter repeat")
                    return False

    def checkGuess(self):
        self.counta = 0
        self.countb = 0
        for i in range(len(self.guess)):
            if self.guess[i] == self.color[i]:
                self.counta += 1
            
            elif self.guess[i] in self.color:
                self.countb += 1
                
        
        if self.countb == self.level:
            print("You win in", self.count, "tries!")

        return

    def play(self):
        attempts = 0
        self.levels()
        self.dice()
        while attempts <= 10 and self.counta != self.level:
            self.guessNum()
            self.checkGuess()
            attempts += 1
            self.out.drawUserGuess(self.guess, attempts)
            self.out.drawHints(self.counta, self.countb, attempts)
        if self.counta == self.level:
            print("You win in", attempts, "tries")
        else:
            print("Sorry. Actual pattern is ", self.color)

    def playLoop(self):
        self.play()
        answer = str(input("Play again? y/n: "))
        self.counta = 0
        self.countb = 0
        self.color = []
        self.num = []
        self.num2 = 0
        self.guess = []
        self.out.clean()
        while answer == "y":
            self.play()
            answer = str(input("Play again? y/n: "))
            self.counta = 0
            self.countb = 0
            self.color = []
            self.num = []
            self.num2 = 0
            self.guess = []
            self.out.clean()
        return


m = Mastermind()
m.playLoop()
