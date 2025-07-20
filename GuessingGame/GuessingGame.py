import random

def guess_the_number():
    play_again = True

    while play_again:
        print("Guess the number!")

        limit = 10
        while True:
            try:
                limit_str = input("Enter the limit")
                limit = int(limit_str)
                if limit > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                        print("Invalid input. Please enter a whole number.")
        secret_number = random.randint(1, limit)
        print(f"I'm thinking of a number from 1 to {limit}")

        tries = 0
        guess = 0

        while guess != secrect_number:
            try:
                guess_str = input("Your guess: ")
                guess = int(guess_str)
                tries += 1

                if guess < secret_number:
                    print("Too low.")
                elif guess > secret_number:
                    print("Too high")
                else:
                    print(f"You guess it in {tries} tries.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")
        while True:
            again_choice = input("Would you like to play again? (y/n): ").lower()
            if again_choice in ["y", "n"]:
                if again_choice == "n":
                    play_again = False
                break
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")
    print("\nBye!")
    input("Press Enter to exit . . .")

if __name__ == "main":
    guess_the_number()