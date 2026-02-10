#!/usr/bin/env python3

# Exercise 05: Average Rainfall
# This program uses nested loops to collect data and calculate average rainfall.

# Get the number of years
years = int(input("Enter the number of years: "))

# Initialize accumulators
total_rainfall = 0.0
total_months = 0

# Outer loop for years
for current_year in range(1, years + 1):
    print(f"For year {current_year}: ")

    # Inner loop for 12 months
    for month in range(1, 13):
        rain = float(input(f"Enter the rainfall for month {month}: "))

        # Add to accumulators
        total_rainfall += rain
        total_months += 1

# Calculate average
average_rainfall = total_rainfall / total_months

# Display the results
print("--- Summary Report ---")
print(f"Total months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f} mm")
print(f"Average monthly rainfall: {average_rainfall:.2f} mm")
