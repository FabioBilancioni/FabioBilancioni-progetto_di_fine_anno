import random

def get_user_choice():
    user_choice = input("Scegli sasso, carta o forbici: ")
    while user_choice.lower() not in ['sasso', 'carta', 'forbici']:
        user_choice = input("Scelta non valida. Scegli sasso, carta o forbici: ")

    return user_choice.lower()

def get_computer_choice():
    choices = ['sasso', 'carta', 'forbici']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Pareggio!")
    elif user_choice == 'sasso' and computer_choice == 'forbici':
        print("Hai vinto!")
    elif user_choice == 'carta' and computer_choice == 'sasso':
        print("Hai vinto!")
    elif user_choice == 'forbici' and computer_choice == 'carta':
        print("Hai vinto!")    
    else:
        print("Hai perso!")

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"La tua scelta: {user_choice}")
    print(f"La scelta del computer: {computer_choice}")

    determine_winner(user_choice, computer_choice)
    rigiocare = input("vuoi rigiocare? (si/no): ").lower()
    if rigiocare == 'si':
        play_game()
    else:
        print("grazie per aver giocato")

if __name__ == "__main__":
    play_game()