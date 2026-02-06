#!/usr/bin/env python3

# Exercise 09: Roulette Wheel Colors
# This program determines the color of a roulette pocket based on its number.

# Get the pocket number from the user
pocket = int(input("Enter a pocket number (0-36): "))

# Determine the color of the pocket
if pocket == 0:
    print("The pocket is green.")
elif 1 <= pocket <= 10:
    if pocket % 2 == 0:
        print("The pocket is black.")
    else:
        print("The pocket is red.")
elif 11 <= pocket <= 18:
    if pocket % 2 == 0:
        print("The pocket is red.")
    else:
        print("The pocket is black.")
elif 19 <= pocket <= 28:
    if pocket % 2 == 0:
        print("The pocket is black.")
    else:
        print("The pocket is red.")
elif 29 <= pocket <= 36:
    if pocket % 2 == 0:
        print("The pocket is red.")
    else:
        print("The pocket is black.")
else:
    # Error message for numbers outside the 0-36 range
    print("Error: Please enter a number between 0 and 36.")
