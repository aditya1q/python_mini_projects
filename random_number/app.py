import random


# example

# # it choose the number between -1 to 10
# random_randrange_number = random.randrange(-1, 11)
# print(random_randrange_number)
# # it also choose the number between -1 to 10
# random_randint_number = random.randint(-1, 10)
# print(random_randint_number)


# random_number = int(input('Enter the number: '))
# random_randrange_number = random.randrange(-1, 11)
# if random_number == random_randrange_number:
#     print('Your guess is right')
# else:
#     print('Your guess is wrong')
# random_randint_number = random.randint(-1, 10)
# print(random_randint_number)


import random

try:
    top_of_range = int(input("Enter the maximum number for the range: "))
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
except ValueError:
    print("Invalid input. Please enter a valid number next time.")
    quit()

# Generate a random number between 0 and top_of_range (inclusive)
target_number = random.randint(0, top_of_range)

guess_count = 0

while True:
    user_input = input("Make a guess: ")

    if user_input.isdigit():
        guess = int(user_input)
        guess_count += 1
    else:
        print("Invalid input. Please enter a number.")
        continue

    if guess == target_number:
        print(
            f"Congratulations! You guessed the correct number in {guess_count} tries.")
        break
    elif guess > target_number:
        print("Too high. Try a smaller number.")
    else:
        print("Too low. Try a larger number.")
