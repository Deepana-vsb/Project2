# Number Guessing Game

import random

def ai_set_number_game():
    print("Welcome to the Number Guessing Game!")
    print("The AI has selected a number between 1 and 100. Try to guess it!")
    ai_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            user_input = int(input("Enter your guess (1-100): "))
            attempts += 1
            if user_input < ai_number:
                print("Entered value is smaller.")
            elif user_input > ai_number:
                print("Entered value is higher.")
            else:
                print(f"\n🎉 Congratulations! You guessed the number {ai_number} in {attempts} attempts! 🎉")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    ai_set_number_game()
