def count_change(money, coins):
    import itertools
    ls = itertools.permutations(coins)
    ls = list(ls)
    print(ls)
count_change(3,[1,3,5,2,3])
