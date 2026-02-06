#!/usr/bin/env python3

# Exercise 01: Day of the week

# Get a number from the user
number = int(input("Enter the number in range of 1-7: "))

# Determine the day of the week
if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif  number == 7:
    print("Sunday")
else:
    # Handle values outside the rande 1-7
    print("Error: The number must be between 1 and 7.")
