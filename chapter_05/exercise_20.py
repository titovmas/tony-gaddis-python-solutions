#!/usr/bin/env python3

# Exercise 20: Random Number Guessing Game
# This program plays a guessing game with the user until they quit.

import random

def main():
    # Keep the game running in loop
    play_again = 'y'

    while play_again == 'y':
        # Generate new random number for each round
        secret_number = random.randint(1,100)
        user_guess = 0

        print("\nI have generated a number between 1 and 100.")

        # Loop until the user guesses the correct number
        while user_guess != secret_number:
            user_guess = int(input("Enter your guess: "))

            check_guess(user_guess, secret_number)

        # Ask if the user wants to play another round
        play_again = input("Correct! Do you want to play again? (y/n): ")


def check_guess(guess, secret):
    if guess > secret:
        print("Too high, try again.")
    elif guess < secret:
        print("Too low, try again.")
    else:
        print("Congratulations! You guessed it!")

# Call the main function
main()
