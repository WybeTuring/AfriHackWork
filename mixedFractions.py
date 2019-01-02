def mixed_fraction(s):
    import math
    import fractions
    ls = []
    num = s.split('/')
    num[0] = int(num[0])
    num[1] = int(num[1])
    if (num[0] > 0 and num[1] > 0) or (num[0] < 0 and num[1] < 0):
        ls.append(1)
    else:
        ls.append(0)
    num[0] = abs(num[0])
    num[1] = abs(num[1])
    if num[0] % num[1] == 0  and num[0] >= num[1]:
        ls.append(num[0] // num[1])
    else:
        ls.append(num[0] // num[1])
        ls.append(num[0] % num[1])
    #simplifying the last remaining digits
    def printResults(vid):
        if len(vid) == 2:
            if vid[0]==1:
                return (str(vid[1]))
            else:
                return (str(-1*vid[1]))
        elif vid[1] == 0:
            if vid[0] == 1:
                re = str(fractions.Fraction(vid[2],num[1]))
            else:
                re = str(-fractions.Fraction(vid[2],num[1]))
            return re
        else:
            if vid[0] == 1:
                re = str(vid[1]) + " " + str(fractions.Fraction(vid[2],num[1]))
                print(re)
                return re
            else:
                re = str(-1*vid[1]) + " " + str(fractions.Fraction(vid[2],num[1]))
                print(re)
                return re
    return printResults(ls)
print(mixed_fraction("-22/-7"))
