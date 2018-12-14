def super_size(n):
    n = str(n)
    list = []
    for i in range(0, len(n)):
        list.append(int(n[i]))
    list.sort(reverse=True)
    value = ""
    for i in range(0,len(n)):
        value = value+str(list[i])
    return int(value)