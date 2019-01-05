"""Author: Lemfon Karl Ndze'dzenyuy Date: 28th November 2018 Use: Determining the number of each denominator that can
be used to give a client his change after a purchase Description: This is an attempt to give all the possible
combinations that can be used. The methodology is to give priority to a certain denomination and get a maximum of the
denominator that can be used, and then proceeds to determine for the number of the other denominations. To optimize
this attempt and ensure that all the possible combinations are gotten, a function can be written that will determine
all the 9! possible ways of arranging the denominators and then running each through the process below. That should
give us an enormous 9*9! different possibilities """
print(
    "Enter the amout of change you are expecting\nPlease enter the number of pesewas as an attached decimal. \nE.g "
    "130.6 for GHC130, 60 pesewas\n :")
change = float(input())
denominations1 = [50, 20, 10, 5, 2, 1, 50, 20,
                  10]  # storing the denominators in a way that will ease the printing of the results
denominations2 = [1, 2, 5, 10, 20, 50, 100, 200,
                  500]  # storing the denominators in a way that will ease the indexing during the iterative
# calculations
counter = len(denominations1)
changeValues = []  # An empty string that will hold the numbers of every denomination that will be used.
# Calculating the maximum number of each denominator that can be used, giving priority to a given position and then
# working downwards This for
for i in range(0, counter):
    k = counter - (i + 1)
    tempValues = []  # Initializing an empty list that will be used when the iteration starts at each point
    money = change * 10
    while k >= 0:
        value = money // denominations2[k]
        money = money % denominations2[k]
        tempValues.append(value)
        k = k - 1
    changeValues.append(tempValues)
# At the end of this, the list changeValues is a list of lists. With each element representing the combination that
# has given proirity to a given position and then worked downwards print(changeValues)
print("\n")
# storing the various elements of changeValues in independent strings to ease printing
element1 = changeValues[0]
element2 = changeValues[1]
element3 = changeValues[2]
element4 = changeValues[3]
element5 = changeValues[4]
element6 = changeValues[5]
element7 = changeValues[6]
element8 = changeValues[7]
element9 = changeValues[8]


# This function ensures that the number of elements in each table correspond with the number of denominators by
# checking for and adding zeros before the table till it has as many elements as there are denominators
def normalize(element):
    l = len(element)
    if l != 9:
        deficit = 9 - l
        for i in range(0, deficit):
            element.insert(0, 0.0)


normalize(element1)
normalize(element2)
normalize(element3)
normalize(element4)
normalize(element5)
normalize(element6)
normalize(element7)
normalize(element8)
normalize(element9)
global h
h = 1


# writing a function that will print out the various kinds of denominators

def functionprint(list):
    l = len(list)
    for i in range(0, l):
        if ((list[i] != 0) and (
                i < 6)):  # This enables us to print the result differently when we have cedi notes from when we have
            # pesewas
            print(str(list[i]) + "  of the  " + str(denominations1[i]) + "  GHC note")
        if ((list[i] != 0) and (i > 5)):
            print(str(list[i]) + "  of the  " + str(denominations1[i]) + "  pesewa coin")
    print("\n")


# Printing the various combinations
print("\nCOMBINATION 1")
functionprint(element1)
print("\nCOMBINATION 2")
functionprint(element2)
print("\nCOMBINATION 3")
functionprint(element3)
print("\nCOMBINATION 4")
functionprint(element4)
print("\nCOMBINATION 5")
functionprint(element5)
print("\nCOMBINATION 6")
functionprint(element6)
print("\nCOMBINATION 7")
functionprint(element7)
print("\nCOMBINATION 8")
functionprint(element8)
print("\nCOMBINATION 9")
functionprint(element9)
