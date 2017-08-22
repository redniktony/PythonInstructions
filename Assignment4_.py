def indent(string, num):
    space = num * " "
    string = space + string
    print(string)
    return 

def center(string, screenWidth):
    if len(string) > screenWidth:
        print("The string is longer than the screen width!")
        return
    screenWidth = float(screenWidth / 2) - len(string)/2
    screenWidth = round(screenWidth)
    indent(string, screenWidth)
    return screenWidth

def centeredBox(string, screenWidth):
    starBar = (len(string) + 4) * "*"
    starMid = "* " + string + " *" 
    center(starBar, screenWidth)
    center(starMid, screenWidth)
    center(starBar, screenWidth)
    return 

indent("hello", 0)
indent("kitty", 26)
screenWidth = center("world", 20)
print("Indented by ", screenWidth , "spaces")
centeredBox("meow",50)
