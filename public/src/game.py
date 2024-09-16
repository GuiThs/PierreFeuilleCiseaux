

import module.gestion as gestion

print("Bienvenue dans le jeu du Pierre Feuille Ciseaux !")

while True:
        choice = input("Voulez-vous commencer ? O/N : ").lower() # L'utilisateur chosiit si il veut lancer le jeu
        if choice == "o":
            gestion.pierre_feuille_ciseaux()
            break
        elif choice == "n":
            print("À bientôt !")
            break  # On quitte la boucle si l'utilisateur choisit 'n'
        else:
            print("Choix invalide. Veuillez entrer 'O' pour oui ou 'N' pour non.") #