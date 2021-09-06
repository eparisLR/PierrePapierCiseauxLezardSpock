import random
liste_choices = ["Pierre", "Papier", "Ciseaux", "Lézard", "Spock"]

def choice_user():
    user= input(" 1: Pierre \n 2: Papier \n 3: Ciseaux \n 4: Lézard \n 5: Spock \n >>>>> Choix : ")
    while user not in ["1", "2", "3", "4", "5"]:
        print("Veuillez entrer un nombre entre 1 et 5 !")
        user= input(" 1: Pierre \n 2: Papier \n 3: Ciseaux \n 4: Lézard \n 5: Spock \n >>>>> Choix : ")
    choice= liste_choices[int(user)-1]
    return choice

def choice_computer(index):
    possibilities = liste_choices
    possibilities.remove(possibilities[index])
    computer = possibilities[random.randint(0, len(possibilities)-1)]
    return computer

user_choice = choice_user()
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