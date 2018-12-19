def choose_best_sum(t, k, ls):
    final = []
    from itertools import combinations
    solve = combinations(ls,k)
    for i in solve:
        final.append(sum(i))
    final.append(t)
    final.sort()
    final.reverse()
    i = final.index(t)
    if i == len(final)-1:
        return None
    else:
        return final[i+1]
    
            