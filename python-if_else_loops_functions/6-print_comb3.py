#!/usr/bin/python3
for i in range(10):  # Premier chiffre de la combinaison
    for j in range(i + 1, 10):  
        if i == 8 and j == 9:  # Dernière combinaiso
            print("{}".format(f"{i}{j}"))
        else:
            print("{}".format(f"{i}{j}"), end=", ")

