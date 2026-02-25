#!/usr/bin/env python3

# Exercise 11: Math Quiz
# This program generates a simple addition test for a user.

import random

def main():

    # Generate two random numbers between 1 and 500
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
   
    # Display the numbers to the user
    display_problem(num1, num2)

    # Get answer from user
    user_answer = int(input("Enter the sum of these numbers: "))

    # Check if the answer is correct
    check_answer(num1, num2, user_answer)

def display_problem(n1, n2):
    print(f"  {n1}")
    print(f"+ {n2}")

def check_answer(n1, n2, answer):
    if answer == n1 + n2:
        print("Congratulations! That is correct.")
    else:
        print(f"Incorrect. The correct answer is {n1 + n2}.")


# Call main function
main()
