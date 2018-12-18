def add_length(str_):
    string = str_.split(" ")
    wlen = []
    ans = []
    print(string[1][1:4])
    for i in range(0,len(string)):
        l = len(string[i])
        wlen.append(l)
    for i in range(0, len(string)):
        ans.append(string[i]+ " " + str(wlen[i]))
    return ans
add_length("gajhkalk hkdjlakd bdhakdaj balka")