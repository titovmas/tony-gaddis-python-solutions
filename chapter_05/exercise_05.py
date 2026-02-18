#!/usr/bin/env python3

# Exercise 05: Property Tax
# This program calculates assessment value and property tax.

# Constants
ASSESSMENT_PERCENT = 0.60
TAX_PER_HUNDRED = 0.72

def main():
    # Get actual value of the property
    actual_value = float(input("Enter the actual value of the property: "))


    # Use a function to calculate and display assessment value and tax
    show_tax_info(actual_value)


def show_tax_info(actual_value):
    # Calculate assessment value
    assessment_value = actual_value * ASSESSMENT_PERCENT

    # Calculate tax property tax ($0.72 for each $100)
    property_tax = (assessment_value / 100) * TAX_PER_HUNDRED

    # Show results
    print(f"Assessment Value: ${assessment_value:,.2f}")
    print(f"Property tax: ${property_tax:,.2f}")

# Call main function
main()
