def rgbFunction(d):
    def changeToHex(n):
        if n < 10 and n >= 0:
            ls = "0"
            ls = ls + str(n)
            return ls
        elif n<=16 and n >= 0:
            ls = ["0A", "0B", "0C", "0D", "0E", "0F", "10"]
            intern = [10, 11, 12, 13, 14, 15, 16]
            if n in intern:
                x = intern.index(n)
                return ls[x]
        else:
            if n > 255:
                return "FF"
            elif n < 0:
                return "00"
            else:
                ls = ""
                while n != 0:
                    x = n % 16
                    x = changeToHex(x)
                    ls = ls + str(x[1])
                    n = n // 16
                re = ""
                for i in range(0,len(ls)):
                    re += ls[len(ls)-(1+i)]
                return re
    ans = ""
    for x in d:
        ans = ans + str(changeToHex(x))
    return ans
print(rgbFunction((-20,275,125)))
