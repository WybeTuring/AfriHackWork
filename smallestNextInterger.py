def next_smaller(n):
    import itertools
    num = str(n)
    num = list(num)
    var = itertools.permutations(num)
    # Make the values in var intergers
    var = list(var)
    var2 = []
    for i in var:
        ls = ""
        for k in range(0, len(i)):
            ls += str(i[k])
        i = str(ls)
        var2.append(int(i))
    #insert the initial argument in the list, and then sort it
    # This will make it easier to return the closest element
    var2.append(n)
    var2.sort()
    # Find the index at which n occurs and return the element before it
    index = var2.index(n)
    if index != 0:
        return var2[index-1]
    else:
        return -1

print(next_smaller(5))
