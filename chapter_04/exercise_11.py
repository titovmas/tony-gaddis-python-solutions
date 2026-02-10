#!/usr/bin/env python3

# Exercise 11: Weight Loss
# This program calculates projected weight loss over 6 months.

# Constants
LOSS_PER_MONTH = 1.5
MONTHS = 6

# Get starting weight
weight = float(input("Enter your starting weight (in kg): "))


print("Month\tProjected Weight")
print("-------------------------")

# Use a for loop to calculate and display the weight changes
for month in range(1, MONTHS + 1):
    weight -= LOSS_PER_MONTH

    # Display the results
    print(f"{month}\t{weight:.1f}")
