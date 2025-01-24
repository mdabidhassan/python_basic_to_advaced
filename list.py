import random

def get_user_choice():
    print("Choose one of the following:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter your choice (1, 2, or 3): ")
    choices = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    return choices.get(choice, None)

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        return "You win!"
    else:
        return "You lose!"
def play_game():
        print("Welcome to Rock-Paper-Scissors!")
        while True:
            user_choice = get_user_choice()
            if not user_choice:
                print("Invalid choice. Please choose again.")
                continue
computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again != "yes":
    print("Thanks for playing!")
    break

 if __name__ == "__main__":
        play_game()