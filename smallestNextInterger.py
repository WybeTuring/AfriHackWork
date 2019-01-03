def next_smaller(n):
    import itertools
    import binarysearch
    num = str(n)
    if len(num) == 1:
        return -1
    else:
        num = list(num)
        var = list(itertools.permutations(num))
        print(len(var))
        # Make the values in var intergers
        var2 = []
        for i in var:
            ls = ""
            for k in range(0, len(i)):
                ls += i[k]
            i = str(ls)
            var2.append(int(i))

        #insert the initial argument in the list, and then sort it
        # This will make it easier to return the closest element
        var2.sort()
        h = binarysearch.binarySearch(var2, 0, len(var2)-1, n)

        # Find the index at which n occurs and return the element before it
        # index = var2.index(str(n))
        if h != 0:
            return int(var2[h-1])
        else:
            return -1

print(next_smaller(1879))
