# Author: Lemfon Karl Ndze'dzenyuy, Kojo E Armah, Hephziba E. U
## email: karllemfon@gmail.com
##Purpose
#### This is a substitution cypher that works in a circular manner. This cypher does not encode special characters and encodes capital
#### letters only with capital letters and lower case letters with lower case letters only
def cipher(c,key): # Arguments are the character to be encoded and the step by which the change is being done
    if (ord(c) == 32): # Makes sure that there is no attempt to encode spaces
        return c
    else:
        if ord(c) in range(65,91):
            k = ord(c) + key
            if k > 90:
                k = 65 + k%91 # Gets the new character that represents the character in a cyclic manner
            return chr(k)
        elif ord(c) in range(97,123):
            k = ord(c) + key
            if k > 122:
                k = 97 + k % 123 # Gets the new character 
            return chr(k)
        else:
            return c
def decode(i,key):
    if ord(i) == 32:
        return i
    elif ord(i) in range(65,key + 65): # If the character is in the cyclic range
        return chr(ord(i)+ (26 - key))
    elif ord(i) in range(97,key + 97):
        return chr(ord(i) + (26 - key)) # Also checking if the character is in the cyclic range
    elif ord(i) in range(65,91) or ord(i) in range(97,123):
        return chr(ord(i) - key)
    else:
        return i
def main():
    shift = int(input("Please enter the digit by which you want the cipher to shift: "))
    plain = input("Enter the string to be encoded: ")
    cipherText = ""
    for c in plain:
        cipherText = cipherText + cipher(c,shift)
    print(cipherText)
    etext = input("Enter the text to be decoded: ")
    plainText = ""
    for k in etext:
        plainText += decode(k,shift)
    print(plainText)
main()
