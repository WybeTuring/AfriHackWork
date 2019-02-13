# Function to determine if a number is green
# Determining if a given number is green
def determineGreen(n):
    ls = list(str(n))
    ls2 = list(str(n**2))
    ans = ls2[len(ls2) - len(ls) : len(ls2)]
    if ans == ls:
        return True
    else:
        return False
## Determining the i-th green number
def green(i):
    import time
    start = time.time()
    k = 0
    num = 1
    while k != i:
        if determineGreen(num): k = k+1
        num2 = num
        if list(str(num))[-1] == '1':
            num += 4
        elif list(str(num))[-1] == '5':
            num += 1
        elif list(str(num))[-1] == '6':
            num += 5
    end = time.time()
    print((end - start), "seconds were used")  
    return num2

print(green(16))
        