def writeUpperCase(filename):
    inputfile = open(filename, 'r')
    output = open('upper.txt', 'w')
    k = inputfile.readlines()
    for i in k:
        print(i.upper(), file = output, end = '')
    inputfile.close()
    output.close()

    
def main():
    name = input("Enter the name of the file: ")
    try:
        writeUpperCase(name)
        print("Check your output in a file called upper.txt")
    except:
        print('Please make sure to check one of the following:\n\t1. The file name is correct\n\t2.The extension is valid for the python file operations, and you are actually typing it in\n\t3. Your script is stored in thesame location as your file\n\tTRY AGAIN PLEASE')

main()