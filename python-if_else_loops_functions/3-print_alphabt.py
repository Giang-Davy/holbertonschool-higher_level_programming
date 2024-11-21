#!/usr/bin/python3
for i in range(97, 123):
    if i == 113:
        continue
    elif i == 101:
        continue
    else:
        lettre = "{}".format(chr(i))
        print(lettre, end="")
