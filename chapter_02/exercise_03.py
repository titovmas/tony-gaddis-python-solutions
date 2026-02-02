#!/usr/bin/env python3

# Exercise 03: Calculation of the land area

# A constant for the number of square meters per acre
SQ_METER_PER_ACRE = 4046.86

# Get the total square meter from user
total_square_meter = float(input("Enter the total square meter in the field: "))

# Calculate the number of acres
acres = total_square_meter / SQ_METER_PER_ACRE

# Display the result 
print(f"The number of acres in the field is: {acres:.2f}")
