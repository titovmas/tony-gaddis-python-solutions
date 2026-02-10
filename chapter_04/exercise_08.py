#!/usr/bin/env python3


# Exercise 08: Sum of Numbers
# This program calculates the sum of positive numbers entered by the user.
# It uses a negative number as a sentinel to stop the loop.

# Initialize the accumulator for the total sum
total_sum = 0.0

# Get the first number from the user
number = float(input("Enter a positive number (or negative for exit): "))

# Use a while loop as long as the number is non-negative
while number >= 0:
    # Add the number to the total sum
    total_sum += number

    # Get the next number
    number = float(input("Enter the positive number(or negative for exit): "))

# Display the final total sum
print(f"The total sum of the numbers you entered is: {total_sum:.2f}")
