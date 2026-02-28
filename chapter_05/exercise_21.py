#!/usr/bin/env python3

# Exercise 21: Rock, Paper & Scissors
# A game where the user competes against the computer.

import random

def main():
    # Keep playing until there is a winner (no tie)
    keep_playing = True
    
    while keep_playing:
        # Get computer's choice
        comp_choice = get_comp_choice()

        # Get user's choice
        user_choice = get_user_choice()

        # Display what both chose
        print(f"\nComputer chose: {comp_choice}")
        print(f"You chose: {user_choice}")

        # Determine the winner
        if comp_choice == user_choice:
            print("It's a tie! Tossing again...\n")
        else:
            determine_winner(comp_choice, user_choice)
            keep_playing = False


def get_comp_choice():
    # Generate a random number and map it to a string
    choice = random.randint(1, 3)
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "scissors"
    else:
        return "paper"

def get_user_choice():
    # Prompt the user for their choice and validate it
    choice = input("Enter rock, paper, or scissors: ").lower()
    while choice != "rock" and choice != "paper" and choice != "scissors":
        print("Invalid choice. Please try again.")
        choice = input("Enter rock, paper, or scissors: ").lower()
    return choice


def determine_winner(comp, user):
    if (user == "rock" and comp == "scissors") or \
       (user == "paper" and comp == "rock") or \
       (user == "scissors" and comp == "paper"):
        print("You win! Congratulations.")
    else:
        print("Computers win. Try again next time.")

# Call the main function
main()
