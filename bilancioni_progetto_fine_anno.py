import random

def play_game():
    choices = ['sasso', 'carta', 'forbici']
    computer = random.choice(choices)
    utente = input("Scegli tra sasso, carta e forbici: ")

    print(f"Il computer ha scelto: {computer}")
    print(f"Tu hai scelto: {utente}")

    if utente == computer:
        print("Pareggio!")
    elif utente == 'sasso' and computer == 'forbici' or \
         utente == 'carta' and computer == 'sasso' or \
         utente == 'forbici' and computer == 'carta':
        print("Hai vinto!")
    else:
        print("Hai perso!")

play_game()
