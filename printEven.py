def printeven(ls):
    return [x for x in ls if (x%2 == 0)] # Using a list comprehension to get the even numbers

def main():
    user_input = input("Enter the numbers (Seperate with commas): ").split(",") # Getting the elements in a list
    user_input = [eval(x) for x in user_input] # changing the elements from strings to numbers
    print("The even numbers are:  ", end = "")
    for i in printeven(user_input):
        print(i, end = " ")
main()
    