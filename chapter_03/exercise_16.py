#!/usr/bin/env python3

# Exercise 16: February Days

# This program determines whether a year is a leap year
# and displays the number of days in February.

# Get the year from the user
year = int(input("Enter a year: "))

# Check the leap year
if (year % 100 == 0 and year % 400 == 0):
    # Leap year (divisible by 100 and 400)
    days = 29
elif (year % 100 != 0 and year % 4: == 0):
    # Leap year (not divisible by 100 but divisible by 4)
    days = 29
else:
    # Not a leap year
    days = 28

# Display the results
print(f"In {year}, February has {days} days.")
