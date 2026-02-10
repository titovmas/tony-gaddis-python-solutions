#!/usr/bin/env python3

# Exercise 09: Ocean Levels
# This program displays a table showing the cumulative rise in ocean levels
# over the next 25 years based on a steady increase of 1.6 mm per year.

# Constant for the annual rise in millimeters
ANNUAL_RISE = 1.6

# Print the table header
print("Year\tTotal Rise (mm)")
print("-----------------------")

# Use a for loop to iterate through years 1 to 25
for year in range(1, 26):
    # Calculate the total rise for the current year
    total_rise = year * ANNUAL_RISE

    # Display the results
    print(f"{year}\t{total_rise:10.1f}")
