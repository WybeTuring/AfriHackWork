# Function to determine if a number is green
def determineGreen(n):
    ls = list(str(n))
    ls2 = list(str(n**2))
    ans = ls2[len(ls2) - len(ls) : len(ls2)]
    if ans == ls:
        return True
    else:
        return False
## Checking if there is a pattern in which the green numbers appear
def green(i):
    k = 1
    for j in range():
        if determineGreen(j):
            k += 1
            u = 1
        else:
            u = 0
        if k == i and u == 1:
            return j
    return False


print(green(30))