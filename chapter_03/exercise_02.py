#!/usr/bin/env python3

# Exercise 02: Areas of Rectangles comparison
# This program calculates and compares the areas of two rectangles.


# Get the dimensions for the first rectangle
length1 = float(input("Enter the length of first rectangle: "))
width1 = float(input("Enter the width of first rectangle: "))

# Get the dimensions for the second rectangle
length2 = float(input("Enter the length of second rectangle: "))
width2 = float(input("Enter the width of second rectangle: "))

# Calculate the areas
area1 = length1 * width1
area2 = length2 * width2

# Compare the areas and display the result
if area1 > area2:
    print("First rectangle has the greater area.")
elif area2 > area1:
    print("Second rectangle has the greater area.")
else:
    print("Both rectangles have the same area.")
