def first_non_repeating_letter(string):
    s = string
    if len(s) == 0:
        return ''
    else:
        k = s.upper()
        ls = []
        for i in k:
            ls.append(k.count(i))
        if 1 in ls:
            j = ls.index(1)
            print(ls)
            return s[j]
        else:
            return ''
