def pizzaArea(d):
    return (((22/7)*(d**2))/4)

def pricePSI(d, p):
    return (p/pizzaArea(d))

def main():
    d = eval(input("Enter the diameter of the pizza (Inches): "))
    p = eval(input("Enter the price of the pizza (Ghana Cedis): "))
    print("The area of your pizza is", pizzaArea(d), "square inches.")
    print("The price per square inch of a",d,"pizza", "is", pricePSI(d,p), "GHC")

main()