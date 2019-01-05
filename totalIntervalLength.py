def sum_of_intervals(intervals):
    ls = []
    for x in intervals:
        for i in range(x[0],x[1]):
            ls.append(i)
    print(ls)
    ls = set(ls)
    return len(ls)
print(sum_of_intervals([[1,4], [7,10], [3,5]]))
