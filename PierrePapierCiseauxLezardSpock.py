import random

#Boucle pour continuer de jouer
while True:

    #Instanciation de la liste des choix possibles
    liste_choices = ["Pierre", "Papier", "Ciseaux", "Lézard", "Spock"]

    #Cette fonction renvoie le string du choix de l'utilisateur et, l'utilisateur ne peut pas 
    #choisir autre chose qu'un string correspondant à 1,2,3,4,5,6. 
    #6 est le choix pour arrêter le jeu.
    def choice_user():
        user= input(" 1: Pierre \n 2: Papier \n 3: Ciseaux \n 4: Lézard \n 5: Spock \n 6: Arrêter \n >>>>> Choix : ")
        while user not in ["1", "2", "3", "4", "5", "6"]:
            print("Veuillez entrer un nombre entre 1 et 5 !")
            user= input(" 1: Pierre \n 2: Papier \n 3: Ciseaux \n 4: Lézard \n 5: Spock \n 6: Arrêter \n >>>>> Choix : ")
        if user == "6":
            return False

        else:
            choice= liste_choices[int(user)-1]
            return choice

    #Cette fonction prend en paramètre l'index du choix de l'utilisateur dans la liste de choix.
    #L'ordinateur choisit entre les autres possibilités et retourne le choix de l'ordinateur en string.
    def choice_computer(index):
        possibilities = ["Pierre", "Papier", "Ciseaux", "Lézard", "Spock"]
        possibilities.remove(possibilities[index])
        computer = possibilities[random.randint(0, len(possibilities)-1)]
        return computer

    
    user_choice = choice_user()

    if user_choice != False:
        #Je récupère les index et, les choix de l'utilisateur et, d'un ordinateur.
        #Je lis mon dictionnaire avec les index des choix utilisateur et, ordinateur.
        #En fonction de si c'est True ou False je print le message correspondant.
        index_user = liste_choices.index(user_choice)
        computer_choice = choice_computer(index_user)
        index_computer = liste_choices.index(computer_choice)

        result = {0: {1: True, 2: False, 3: True, 4: False },
        1: {0: True, 2: False, 3: False, 4: True}, 
        2: {0: False, 1: True, 3: True, 4: False}, 
        3: {0: False, 1: True, 2: False, 4: True}, 
        4: {0: True, 1: False, 2: True, 3: False} }

        if result[index_user][index_computer] == False:
            print(f"L'ordinateur a joué : {computer_choice}. Vous avez perdu.")
        else:
            print(f"L'ordinateur a joué : {computer_choice}. Vous avez gagné !")
    
    else:
        break
        
