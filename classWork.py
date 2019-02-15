# Question 4 programming exercices chapter 6
# Calculating the sum of the natural numbers
def sumN(n):
    return (n*(n+1))/2

# Calculatinmg the sum of the cubes of the numbers
def sumNCubes(n):
    sumN = 0
    for i in range(1,n+1):
        sumN = sumN + i**3
    return sumN

def main():
    num = int(input("Please enter a natural number: "))
    print("The sum of the natural numbers up to", num, "is: ", sumN(num))
    print("The sum of the cubes of the natural numbers up to", num, "is:", sumNCubes(num))


# Question 3 programming exercices chapter 6
# Calculating the area of a sphere
def sphereArea(r):
    return (22/7)*4*(r**2)

# Calculating the volume of a sphere
def sphereVolume(r):
    return (22/7)*(r**3)*(4/3)

def main2():
    num = eval(input("Please enter the radius of the sphere: "))
    print("The surface area of the sphere is: ", sphereArea(num), "square units")
    print("The volume of the sphere is: ", sphereVolume(num), "cubic units")


# Question 6 programming exercices chapter 6
# calculating the area of a triangle using Heron's formular
def triangleArea(a, b, c):
    from math import sqrt
    k = (a + b + c) / 2
    return sqrt(k * (k - a) * (k - b) * (k - c))

def main3():
    sides = input("Enter the three sides, seperated with commas please: ").split(",")
    sides = [int(k) for k in sides]
    print("The area of the circle is: ", triangleArea(sides[0], sides[1], sides[2]), "square units.")

# FI's exercises
# Converting Ghana cedis to pounds
def cedisPound(c):
    return c / 6.54
# Converting Ghana cedis to dollars
def cedisDollars(c):
    return c / 5.28
# Converting Ghana cedis to euros
def cedisEuro(c):
    return c / 5.29

def main4():
    amt = eval(input("Please enter the amount in Ghana cedis: "))
    conv = open('convertions.txt', 'w')
    print(str(amt) + " GHC is:  " + str(round(cedisDollars(amt), 3)) + " Dollars", file = conv)
    print(str(amt) + " GHC is:  " + str(round(cedisEuro(amt), 3)) + " Euros", file = conv)
    print(str(amt) + " GHC is:  " + str(round(cedisPound(amt), 3)) + " Pounds", file = conv)
    conv.close()

