#!/usr/bin/python3
for i in range(100):
    if i < 10:
        resultat1 = "0{}".format(i)
        print(resultat1, end=", ")
    else:
        resultat2 = "{}".format(i)
        print(resultat2, end=", " if i < 99 else " ")
