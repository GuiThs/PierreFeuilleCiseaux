

import numpy as np


def pierre_feuille_ciseaux():
    options = ['pierre', 'feuille', 'ciseaux']
    
    while True:
        user_choice = input("Choisissez Pierre, Feuille ou Ciseaux : ").lower()
        if user_choice not in options:
            print("Choix invalide. Essayez encore.")
            continue
        
        # Choix aléatoire de l'ordinateur avec numpy
        computer_choice = np.random.choice(options)
        print(f"L'ordinateur a choisi {computer_choice}.")
        
        if user_choice == computer_choice:
            print("Égalité !")
            
        elif (user_choice == "pierre" and computer_choice == "ciseaux") or \
             (user_choice == "feuille" and computer_choice == "pierre") or \
             (user_choice == "ciseaux" and computer_choice == "feuille"):
            print("Vous gagnez !")
            """L'antislash est une continuation de ligne mais,
            il y avait possibilié de faire un tuple pour imbriquer ces 3 users choices
            """
            
        else:
            print("Vous perdez !")
        
        
        replay = input("Voulez-vous rejouer ? O/N : ").lower() # "o" si le joueur veut rejouer
        if replay != "o":
            print("Merci d'avoir joué !")
            break


