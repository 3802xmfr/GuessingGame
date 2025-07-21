#Brandon Gillespie
#CIS261
#GuessingGame

import random
from token import NUMBER
number = random.randint(1,100)
guess = 0
play_again = "y"

print("Guess the Number!")

print("Guess the number 1 to 100!")

while play_again == "y":
    guess = int(input("What is your guess?"))
    if guess == "":
        print("Please enter a valid response.")
    elif guess > number:
        print("Too High")
    elif guess > number:
        print("Too Low")
    elif guess == number:
        print(f"\nAwesome!! {guess} was correct!")
        play_again = input("Would you like to play again? y/n")
        if play_again == 'n':
            print("Thanks for playing!")
            play = False
        elif play_again == 'y':
            number = random.randint(1, 100)
    else:
        print(f"\nSorry nice try. {guess} is not correct.")
        if play_again == 'n':
            print("Come back later.")
            play  = False


print("Congrats you guessed it!")


play_again = input("Do you want to play again? y/n")
