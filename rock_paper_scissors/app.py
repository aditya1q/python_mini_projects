import random

# user_wins = 0
# computer_wins = 0

# rock = 0
# paper = 1
# scissors = 2


# user_input = int(input('Enter 0 for rock, 1 for paper and 2 for scissor: '))
# computer_input = random.randint(0, 2)
# print('computer choose:',computer_input)

# if user_input == computer_input:
#     print('Match is draw')
# elif user_input == 0 and computer_input == 1:
#     print('computer wins')
# elif user_input == 1 and computer_input == 2:
#     print('computer wins')
# elif user_input == 1 and computer_input == 0:
#     print('user wins')
# elif user_input == 2 and computer_input == 1:
#     print('user wins')
# elif user_input == 0 and computer_input == 2:
#     print('user wins')
# elif user_input == 2 and computer_input == 0:
#     print('computer wins')
# else:
#     print('getting error')



rock = 0
paper = 1
scissors = 2

while True:
    print("Welcome to Rock-Paper-Scissors!")
    print("Type 0 for Rock, 1 for Paper, 2 for Scissors\n")
    user_input = int(
        input('Enter 0 for rock, 1 for paper and 2 for scissor: '))
    computer_input = random.randint(0, 2)
    print('computer choose:', computer_input)

    if (user_input > 2 or user_input == ''):
        print('please enter the number between 0, 1 or 2')
        continue
    elif (user_input == computer_input):
        print('Match Draw')
    elif user_input - computer_input == 1 or user_input - computer_input == 2:
        print('user wins')
    elif user_input - computer_input == -1 or user_input - computer_input == -2:
        print('computer wins')
    continue
