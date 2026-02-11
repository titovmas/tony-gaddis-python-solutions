#!/usr/bin/env python3

# Exercise 14:Drawing Patterns
# This program uses nested loops to draw a pattern of asterisks.

# Set the base size for the pattern
BASE_SIZE = 7

# Use a for loop to display each row of the pattern
for row in range(BASE_SIZE, 0, -1):
    # Use a for loop to display each asterisk in the row
    for col in range(row):
        print("*", end="")

    # Move to the next line
    print()
