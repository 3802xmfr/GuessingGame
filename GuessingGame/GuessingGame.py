#Brandon Gillespie
#CIS261
#GuessingGame

import random

number = random.randint(1,100)
guess = 0

while guess != number:
    guess = int(input("Guess the Number! 1 to 100: "))
    if (guess < number):
        print("Guess higher!")
    elif (guess > number):
        print("Guess lower!")
    else:
        print("You are Correct!")

play_again_input = input("Do you want to play again? (yes/no): ").lower()
if play_again_input != "yes":
    keep_playing = False
print("\nThanks for playing. ")
