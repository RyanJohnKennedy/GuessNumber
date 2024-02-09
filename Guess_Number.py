import random


def guess(x):
    random_number = random.randint(1, x)
    counter = 0
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high")
        counter += 1

    print(f"Yay, congrats! You guessed the number ({random_number}) in {counter} tries.")


guess(10)
