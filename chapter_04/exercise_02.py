#!/usr/bin/env python3

# Exercise 02: Calories Burned
# This program displays the calories burned at specific time intervals.

# Constant for calories burned per minute
CALORIES_PER_MINUTE = 4.2

# Display the table header
print("Minutes\t\tCalories Burned")
print("-------------------------------")

# Use a for loop with a range that steps by 5
for minutes in range(10, 31, 5):
    # Calculate calories burned
    calories = minutes * CALORIES_PER_MINUTE

    # Display the result
    print(f"{minutes}\t\t{calories:.1f}")
