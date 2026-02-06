#!/usr/bin/env python3

# Exercise 07: Color Mixer
# This program determines the secondary color from two primary colors.

# Get two primary colors from the user
color1 = input("Enter the first primary color (red, blue, or yellow): ")
color2 = input("Enter the second primary color (red, blue, or yellow): ")

# Determine the resulting color
if (color1 == "red" and color2 == "blue") or \
   (color1 == "blue" and color2 == "red"):
    print("When you mix red and blue, you get purple.")

elif (color1 == "red" and color2 == "yellow") or \
     (color1 == "yellow" and color2 == "red"):
    print("When you mix red and yellow, you get orange.")

elif (color1 == "blue" and color2 == "yellow") or \
     (color1 == "yellow" and color2 == "blue"):
    print("When you mix blue and yellow, you get green.")

else:
    # Handle incorrect input
    print("Error: You must enter two different primary colors.")
