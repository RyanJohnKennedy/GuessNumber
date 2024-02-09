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


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    counter = 0
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else :
            guess = low

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?: ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

        counter += 1

    print(f"Yay! The computer your number ({guess}) in {counter} tries.")

maxNumber = int(input("Enter max number for the computer to guess: "))
computer_guess(maxNumber)
