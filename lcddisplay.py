def printer(a):
    if a == 1:
        return ("  |\n  |")
    elif a == 2:
        return ("__\n__|\n|__")
    elif a == 3:
        return ("__\n__|\n__|")
    elif a == 4:
        return ("|__|\n   |")
    elif a == 5:
        return (" __\n|__\n___|")
    elif a == 6:
        return (" __\n|__\n|__|")
    elif a == 7:
        return ("__\n  |\n  |")
    elif a == 8:
        return (" __\n|__|\n|__|")
    elif a == 9:
        return (" __\n|__|\n __|")
    elif a == 0:
        return (" __\n|  |\n|__|")
    else:
        print("Ensure that you are entering a digit")

num = list(input("Please type in the number: "))
num = [int(k) for k in num]
for k in num:
    print(printer(k)
    

    