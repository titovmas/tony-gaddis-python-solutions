#!/usr/bin/env python3

# Exercise 01: Bug Collector
# This program calculates the running total of bugs collected over 5 days.

# Initialize the accumulator variable
total_bugs = 0

# Use a for loop to repeat 5 times
for day in range(1,6):
    # Ask the user for the number of bugs for the current day
    bugs = int(input(f"Enter the number of bugs collected on day {day}: "))

    # Add the bugs to the running total (accumulator)
    total_bugs += bugs

# Display the final results
print(f"\nTotal number of bugs collected: {total_bugs}")
