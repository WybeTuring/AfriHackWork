# Checking if a string is a palindrome
def palindrome(word):
    if word == word[::-1]: # Take note that with slicing, if you change the step to -1, python automatically reverses the direction of iteration
        return ("Palindrome")
    else:
        return ("Not Palindrome")

# Replacing the vowels in a word
def replace(word):
    word = word.replace("a", "@")
    word = word.replace("e", "3")
    word = word.replace("i", "1")
    word = word.replace("o", "0")
    word = word.replace("u", "+")
    return word

# Solving quadratic equations
def quadSolve(a,b,c):
    from math import sqrt
    if a:
        if ((b**2) - 4*a*c) < 0: return (" Sorry, this equation has complex roots")
        return [(-b + sqrt((b**2) - 4*a*c)) /(2*a), (-b - sqrt((b**2) - 4*a*c)) /(2*a)]       
    else: return -c / b        

# Factorial experiment
def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(10))
# Drawing the faces
import graphics
def drawFace(center, size, win): # def drawFace(center1, center2, size, win)
    C = graphics.Point(center[0], center[1]) # C = graphics.Point(center1, center2)
    gwin = graphics.GraphWin(win, 500, 500)
    face = graphics.Circle(C, size)
    face.draw(gwin)
    # Creating the left eye
    graphics.Circle(graphics.Point(C.getX() - 10, C.getY() - 10) , 5).draw(gwin)
    # Creating the right eye
    graphics.Circle(graphics.Point(C.getX() + 10, C.getY() - 10) , 5).draw(gwin)
    gwin.getMouse()
    gwin.close()

# drawFace((200, 150), 60, "KarlWin")
print(quadSolve(5,2,1))
