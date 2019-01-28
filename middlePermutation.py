def middle_permutation(string):
    import itertools
    ls = itertools.permutations(string)
    ls2 = []
    for x in ls:
        x = "".join(x)
        ls2.append(x)
    ls2.sort()
    k = (len(ls2) -1)// 2
    print(ls2[k])

middle_permutation("abcdxg")
