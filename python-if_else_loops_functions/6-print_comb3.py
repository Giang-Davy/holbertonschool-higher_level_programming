#!/usr/bin/python3
for i in range(10):  # Premier chiffre de la combinaison
    for j in range(i + 1, 10):  # Deuxième chiffre, commence à i+1 pour éviter les doublons
        # Formatage des combinaisons en deux chiffres
        if i == 8 and j == 9:  # Dernière combinaison, donc pas de virgule finale
            print(f"{i}{j}")
        else:
            print(f"{i}{j}", end=", ")

