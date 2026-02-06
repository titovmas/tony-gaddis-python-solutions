#!/usr/bin/env python3

# Exercise 04: Roman Numerals
# This program converts a number (1-10) to a Roman numeral.

# Get the number from user
number = int(input("Enter the number in range between 1-10: "))

# Determine the Roman numeral equivalent
if number == 1:
    print("Roman numeral: I")
elif number == 2:
    print("Roman numeral: II")
elif number == 3:
    print("Roman numeral: III")
elif number == 4:
    print("Roman numeral: VI")
elif number == 5:
    print("Roman numeral: V")
elif number == 6:
    print("Roman numeral: VI")
elif number == 7:
    print("Roman numeral: VII")
elif number == 8:
    print("Roman numeral: VIII")
elif number == 9:
    print("Roman numeral: IX")
elif number == 10:
    print("Roman numeral: X")
else:
    # Handle error for numbers outside 1-10
    print("Error: Input must be between 1-10 ")
