import sys
from random import randint

# Making our game as difficult as we want
lower_bound, upper_bound = int(sys.argv[1]), int(sys.argv[2])
_answer = randint(lower_bound, upper_bound)

valid_guesses = []

print(
    f'Welcome to Sarah\'s guessing game! You are guessing a number between {lower_bound} and {upper_bound} (including both).')
while True:
    try:
        user_guess = int(input('Your guess: '))
        if lower_bound <= user_guess <= upper_bound:
            if user_guess not in valid_guesses:
                valid_guesses.append(user_guess)
                if user_guess == _answer:
                    break
                elif user_guess > _answer:
                    print(f'{user_guess} was too high.')
                else:
                    print(f'{user_guess} was too low.')
            else:
                print(f'You already guessed {user_guess}.')
        else:
            print(
                f'Please input an integer between {lower_bound} and {upper_bound}.')
        continue
    except ValueError:
        print("Please enter an integer.")
        continue
print(
    f'Congratulations! You won! It took you {len(valid_guesses)} guesses to get the correct number.')
