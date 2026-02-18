#!/usr/bin/env python3

# Exercise 01: Kilometer Converter
# This program converts kilometers to miles using a function.

# Constant
CONVERSION_FACTOR = 0.6214

def main():
     # Get the distance in kilometers from the user
    kilometers = float(input("Enter the distance in kilometers: "))

    # Display the distance converted to miles
    show_miles(kilometers)

# Use a function to calculate and display the conversion result
def show_miles(km):
    miles = km * CONVERSION_FACTOR
    print(f"{km} kilometers is equal to {miles:.2f} miles.")

# Call the main function
main()
