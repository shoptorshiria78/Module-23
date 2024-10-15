import random

def guess_number():
    # The computer picks a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Loop until the player guesses the correct number
    while True:
        try:
            # Player enters their guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct, too high, or too low
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_number()
