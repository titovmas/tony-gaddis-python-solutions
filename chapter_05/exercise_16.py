#!/usr/bin/env python3

# Exercise 16: Odd/Even Counter
# This program generates 100 random numbers and counts evens and odds.

import random

def main():
    # Initialize counters
    even_count = 0
    odd_count = 0

    # Generate 100 random numbers
    for i in range(100):
        # Get a random number between 1 and 1000
        number = random.randint(1, 1000)

        # Check if the number is even using the function
        if is_even(number):
            even_count += 1
        else:
            odd_count += 1

    # Display the final counts
    print(f"Number of even numbers: {even_count}")
    print(f"Number of odd numbers: {odd_count}")

def is_even(num):
    # Determine if a number is even
    if num % 2 == 0:
        return True
    else:
        return False

# Call the main function
main()
