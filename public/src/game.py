import module.gestion as gestion

print("Bienvenue dans le jeu du Pierre Feuille Ciseaux !")

choice = ""
while choice not in ["o", "n"]: # Possibilité d'utiliser l'opérateur Walrus ':=' pour conciser le code
    choice = input("Tu veux commencer ? O/N : ").lower()
    if choice == "o":
        gestion.pierre_feuille_ciseaux()
    elif choice == "n":
        print("À bientôt !")
    else:
        print("Choix invalide. Veuillez entrer 'O' pour oui ou 'N' pour non.")


