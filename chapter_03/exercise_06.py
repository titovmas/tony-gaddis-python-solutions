#!/usr/bin/env python3

# Exercise 06:Magic Dates
# This program determines if a date is "magic" based on day, month, and year. 

# Get the day, month and two-digit year from the user
day = int(input("Enter the day: "))
month = int(input("Enter the month (numeric): "))
year = int(input("Enter the two-digit year: "))

# Calculate the product of day and month
# And check if it equals the year
if day * month == year:
    print("This date is magic!")
else:
    print("This date is not magic")
