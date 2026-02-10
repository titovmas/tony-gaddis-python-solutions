#!/usr/bin/env python3

# Exercise 12: Factorial of a Number
# This program calculates the factorial of a non-negative integer.

# Get the number from the user
number = int(input("Enter a non-negative integer: "))

# Initialize the accumulator for the product to 1
factorial = 1

# Use a for loop to calculate factorial
for value in range(1, number + 1):
    factorial *= value

# Display the result
print(f"The factorial of {number} is {factorial}")
