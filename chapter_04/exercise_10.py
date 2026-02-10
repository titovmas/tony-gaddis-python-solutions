#!/usr/bin/env python3

# Exercise 10: Tuition Increase
# This program calculates the projected tuition for the next 5 years
# with an annual increase of 3%.


# Constants
STARTING_TUITION = 145000.0
INCREASE_RATE = 0.03
YEARS = 5

# Set initial tuition
current_tuition = STARTING_TUITION

# Print the table header
print(f"Year\t\tProjected Tuition")
print("------------------------------")

# Use a for loop to calculate and display the increase for each year
for year in range(1, YEARS + 1):
     
    # Calculate the increase for the current year
    current_tuition += current_tuition * INCREASE_RATE

    # Display the year and the new tuition
    print(f"{year}\t\t{current_tuition:.2f}")
