import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    # Set the number of attempts
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        # Ask the player for their guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is correct, too high, or too low
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

# Start the game
number_guessing_game()
