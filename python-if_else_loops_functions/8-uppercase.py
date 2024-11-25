#!/usr/bin/python3
def uppercase(str):
    resultat = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            resultat += chr(ord(char) - 32)
        else:
            resultat += char
    print("{}".format(resultat))

