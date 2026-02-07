#!/usr/bin/env python3

# Exercise 13: Shipping Charges
# This program calculates the shipping rate based on the package weight

# Get the package weight from the user
weight = float(input("Enter the weight of the package (in grams): "))

# Determine the shipping rate based on weight range
if 0 < weight <= 200:
    rate = 150
elif 200 < weight <= 600:
    rate = 300
elif 600 < weight <= 1000:
    rate = 400
elif weight > 1000:
    rate = 475
else:
    # Handle wight that is 0 or less
    rate = 0
    print("Error: Weight must be greater than 0.")

# Display the shipping rate if the weight was valid
if rate > 0:
    print(f"For a package weighing {weight:.2f} grams,")
    print(f"the shipping rate is ${rate} per 100 grams.")
