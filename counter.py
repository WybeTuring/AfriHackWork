def counter(filename):
    k = open(filename, 'r').readlines()
    num_line = len(k)
    num_words = 0
    num_char = 0
    for line in k:
        num_words += len(line.split())
        num_char += len(line)
    return (num_line, num_words, num_char)


def main():
    name = input("Enter the name of the file: ")
    try:
        print(name, "has", counter(name)[0], "lines")
        print(name, "has", counter(name)[1], "words")
        print(name, "has", counter(name)[2], "characters")
    except:
        print('Please make sure to check one of the following:\n\t1. The file name is correct\n\t2.The extension is valid for the python file operations, and you are actually typing it in\n\t3. Your script is stored in thesame location as your file\n\tTRY AGAIN PLEASE')

main()
