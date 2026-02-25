#!/usr/bin/env python3

# Exercise 10: Feet to Inches
# This program converts feet to inches using a value-returning function.

# Constant for conversion
INCHES_PER_FOOT = 12

def main():
    # Get the number of feet from the user
    user_feet = float(input("Enter the number of feet: "))

    # Use a function to convert feet to inches
    total_inches = feet_to_inches(user_feet)

    # Display the result
    print(f"{user_feet} feet is equal to {total_inches} inches.")

def feet_to_inches(feet):
    # Calculate and return the result
    return feet * INCHES_PER_FOOT

# Call the main function
main()
