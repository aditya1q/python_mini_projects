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


Top_of_range = int(input('Enter the last value: '))

if Top_of_range:  # type: ignore
    Top_of_range = int(Top_of_range)

    if Top_of_range <= 0:
        print('Please type a number larget than 0 next time.')
        quit()
else:
    print('please type a number next time')
    quit()
random_randrange_number = random.randint(0, Top_of_range)

guesses = 0
while True:
    guesses += 1

    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_randrange_number:
        print('your guess is right')
        break

    if user_guess > random_randrange_number:
        print('this number is greter then the expected number')
    else:
        print('this number is smaller then the expected number')

print(guesses)
