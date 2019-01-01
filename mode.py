ls = [1, 2, 4, 3, 5, 6, 7, 2, 4, 10,12]
count = 1
md = []
for el in ls:
    if ls.count(el)>count:
        count = ls.count(el)
        y = el
        pos = ls.index(el)
md.append(ls[pos])
for el in ls:
    if (ls.count(el) == count) and (el != ls[pos]):
        md.append(el)
if count == 1:
    print("Sorry, all elements occur thesame number of times")
else:
    if len(md)== 1:
        print("The element that occurs most is " + str(el) + ".\nIt occurs " + str(count) + " times")
    else:
        md = set(md) # This makes the list md a set, inorder to avoid repetition of elements
        print("The mode elements are:")
        for i in md:
            print(i)
        print("They occur " + str(count) + " times")
