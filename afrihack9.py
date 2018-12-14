def add_length(str_):
    string = str_.split(" ")
    wlen = []
    ans = []
    for i in range(0,len(string)):
        l = len(string[i])
        wlen.append(l)
    for i in range(0, len(string)):
        ans.append(string[i]+ " " + str(wlen[i]))
    return ans