#!/usr/bin/env python3

# Exercise 05: Mass and Weight
# This program calculates weight in Newtons and checks its magnitude.

# Constant
GRAVITY = 9.8

# Get the mass form the user
mass = float(input("Enter the object's mass in kilograms: "))

# Calculate the weight
weight = mass * GRAVITY

# Display the weight
print(f"The weight of the object is {weight:.2f} Newton")

# Check weight limits
if weight > 500:
    print("The object is too heavy! It weighs more than 500 Newtons.")
elif weight < 100:
    print("The object is too light! It weighs less than 10 Newtons.")
