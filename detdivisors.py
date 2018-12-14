def detdivisors(n):
    import math
    divisors = []
    sum = 0
    for i in range(1,n+1):
        if n%i == 0:
            divisors.append(i)
    for i in range(0, len(divisors)):
        sum = sum + (divisors[i]**2)
    if (math.sqrt(sum)%1 == 0):
        return sum
    else:
        return False
def list_squared(m, n):
    answers = []
    for i in range(m, n+1):
        ans = []
        if detdivisors(i) != False:
            ans.append(i)
            ans.append(detdivisors(i))
            answers.append(ans)
    return answers
num = int(input("Enter the beginning: "))
end = int(input("Enter the end: "))
ans = list_squared(num,end)
print(ans)