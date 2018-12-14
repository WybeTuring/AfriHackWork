def likes(names):    
    if len(names) == 0:
        ans = "no one likes this"
        return ans
    if len(names) == 1:
        ans = names[0] + " likes this"
        return ans
    elif len(names) == 2:
        ans = names[0] + " and " + names[1] + " like this"
        return ans
    elif len(names) == 3:
        ans = names[0] + ", " + names[1] + " and " + names[2] + " like this"
        return ans
    else:
        num = len(names) - 2;
        ans = names[0] + ", " + names[1] + " and " + str(num) + " others like this"
        return ans
        