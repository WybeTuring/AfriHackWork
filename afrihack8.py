def iq_test(numbers):
    numbers = numbers.split(" ")
    even = []
    odd = []
    list = []
    for i in range(0,len(numbers)):
        list.append(int(numbers[i]))
    for i in range(0,len(list)):
        if list[i] % 2 == 0:
            even.append(i+1)
        else:
            odd.append(i+1)
    if len(odd) == 1:
        return odd[0]
    else:
        return even[0]
  