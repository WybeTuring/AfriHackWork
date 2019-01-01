def zeros(n):
    x = n/5
    if x:
        return int(x + zeros(x))
    else:
        return 0
print(zeros(600))
