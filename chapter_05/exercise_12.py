#!/usr/bin/env python3

# Exercise 12: Maximum of Two Values
# This program finds the larger of two integers using a function.

def main():
    # Get two integers from the user
    first_number = int(input("Enter the first integer: "))
    second_number = int(input("Enter the second integer: "))

    if first_number == second_number:
        print("The numbers are equal")
    else:
        # Use the max function to find the greater value
        greater_value = maximum(first_number, second_number)

        # Display the result
        print(f"The maximum value is: {greater_value}")

def maximum(num1, num2):
    # Compare the two numbers and return the larger one
    if num1 > num2:
        return num1
    else:
        return num2

# Call main function
main()
