def list_squared(m, n):
    import math
    answers = []
    for i in range(m,n+1):
        divisors = []
        sum = 0
        for j in range(1,i+1):
            if m % j == 0:
                divisors.append(j)
        for i in range(0, len(divisors)):
            sum = sum + (divisors[i]*divisors[i])
        num = math.sqrt(sum)
        if num % 1 == 0:
            answers.append(i)
    return answers

ans = list_squared(1,250)
print(ans)
