def cipher(c):
    k = ord(c) + 2
    return chr(k) 
def decode(i):
    k = ord(i) - 2
    return chr(k)
def main():
    plain = input("Enter the string to be encoded: ")
    cipherText = ""
    for c in plain:
        cipherText += cipher(c)
    print(cipherText)
    etext = input("Enter the text to be decoded: ")
    plainText = ""
    for k in etext:
        plainText += decode(k)
    print(plainText)

main()