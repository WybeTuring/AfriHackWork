# Author: lemfon Karl Ndze'dzenyuy
    #karl.lemfon@gmail.com
##A calcullator that works with the principle of bodmas

"""
Create a simple calculator that given a string of operators (+ - * and /) and numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.
"""
def evaluate(strin):
    cal = strin.split(" ")
    i = 0
    ans = []
    for i in range(len(cal)):
        if i < len(cal) and cal[i] == '/':
            index1 = int(cal[i-1]) / int(cal[i+1])
            ans.append(index1)
            del cal[i-1:i+2]
            cal.insert(i-1,index1)
            print(cal)
        elif i < len(cal) and cal[i] == '*':
             index1 = int(cal[i-1]) * int(cal[i+1])
             ans.append(index1)
             del cal[i-1:i+2]
             cal.insert(i-1,index1)
             print(cal)
    for i in range(len(cal)):
        if i < len(cal) and cal[i] == '-':
            index1 = int(cal[i-1]) - int(cal[i+1])
            ans.append(index1)
            del cal[i-1:i+2]
            cal.insert(i-1,index1)
            print(cal)
        elif i < len(cal) and cal[i] == '+':
             index1 = int(cal[i-1]) + int(cal[i+1])
             ans.append(index1)
             del cal[i-1:i+2]
             cal.insert(i-1,index1)
             print(cal)
    if cal[1] == '+':
        ret = int(cal[0]) + int(cal[2])
    elif cal[1] == '-':
        ret = int(cal[0]) - int(cal[2])
    
    return ret
       
print(evaluate("2 / 2 + 3 * 4 - 6 + 2 - 3 * 5"))

