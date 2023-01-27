import random

def guess_number():
    number_list = list(range(1, 10))
    chosen_number = random.choice(number_list)
    guess = 0
    while guess != chosen_number:
        guess = input("Guess the number: ")
        try:
            guess = int(guess)
            if guess < 0:
                print("The number you need to guess is natural number")
            elif guess > chosen_number:
                print("Too big!")
            elif guess < chosen_number:
                print("Too small!")
            elif guess == chosen_number:
                print("You win!")

        except ValueError:
            print("Sorry I only understand natural numbers from 1 to 100")


guess_number()
