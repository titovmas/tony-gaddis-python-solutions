#!/usr/bin/env python3

# Exercise 03: Insurance
# This program calculates the minimum recommended insurance for a building.

# Constant for the insurance percentage
INSURANCE_PERCENTAGE = 0.8


def main():
    # Get the replacement cost of the building
    replacement_cost = float(input("Enter the replacement cost of the building: "))
    
    # Use a function to calculate and display the insurance amount
    show_insurance(replacement_cost)

def show_insurance(cost):
    # Calculate insurance amount
    insurance_amount = cost * INSURANCE_PERCENTAGE
    
    # Display the result
    print(f"Minimum insurance amount: ${insurance_amount:,.2f}")

# Call main function
main()
