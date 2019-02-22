def standing(credits):
    if credits < 7: return "Freshman"
    elif credits < 16: return "Junior"
    elif credits < 26: return "Sophomore"
    return "Senior"
def main():
    cr = eval(input("Enter number of credits: "))
    print(standing(cr))


# Babysitting expenses

def costBSitting(start, stop): # start[0] is the starting hour, start[1] is the starting minute. Same thing for stop
    # I assume that stop times will always be ahead of start times
    if stop[0] <= 21:
        if stop[0] == 21:
            return 2.50*(stop[0]-start[0]) + (stop[1] * (1.75/60)) + (start[1] * (2.50/60)) # The last two additions handle the costs for the minutes
        else:
           return 2.50*(stop[0]-start[0]) + (stop[1] * (2.50/60)) + (start[1] * (2.50/60)) 
    else:
        if start[0] >= 21:
            return 1.75*(stop[0]-start[0]) + (stop[1] * (1.75/60)) + (start[1] * (1.75/60))
        else:
            return (2.50*(21 - start[0]) + (1.75 * (stop[0] - 21))) + (start[1] * (2.50/60)) + (stop[1] * (1.75/60))
def main2():
    startTime = input("Enter the start time (e.g 22:47): ").split(':')
    startTime = [eval(x) for x in startTime]
    stopTime = input("Enter the stop time (e.g 23:30): ").split(':')
    stopTime = [eval(x) for x in stopTime]
    print("The cost is", round(costBSitting(startTime, stopTime), 2), '$.')

main2()
