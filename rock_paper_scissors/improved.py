import random

user_wins = 0
computer_wins = 0

options = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock-Paper-Scissors!")
print("Type 0 for Rock, 1 for Paper, 2 for Scissors, or 'q' to quit.\n")

while True:
    user_input = input("Your choice (0=Rock, 1=Paper, 2=Scissors, q=Quit): ").strip().lower()

    if user_input == 'q':
        print("\nThanks for playing!")
        print(f"Final Score - You: {user_wins}, Computer: {computer_wins}")
        break

    if not user_input.isdigit() or int(user_input) not in [0, 1, 2]:
        print("Invalid input. Please enter 0, 1, 2 or 'q' to quit.\n")
        continue

    user_choice = int(user_input)
    computer_choice = random.randint(0, 2)

    print(f"You chose: {options[user_choice]}")
    print(f"Computer chose: {options[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!\n")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win this round!\n")
        user_wins += 1
    else:
        print("Computer wins this round!\n")
        computer_wins += 1
