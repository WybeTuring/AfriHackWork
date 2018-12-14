def persistence(n):
    n =str(n)
    if len(n)==1:
        return 0
    else:
        counter = 0
    while len(n)> 1:
        counter += 1
        multiple = 1
        for x in n:
            multiple *= int(x)
        n = str(multiple)
    return counter
            