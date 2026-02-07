#!/usr/bin/env python3

# Exercise 14: Body Mass Index
# This program calculates BMI and informs the user if their weight is
# optimal, underweight, or overweight.

# Get weight and height from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in metres: "))

# Calculate BMI using the formula: (weight * / (height^2))
bmi = weight / (height ** 2)

# Display the calculated BMI
print(f"Your BMI is {bmi:.1f}")

# Categorize the BMI result using your range style
if 18.5 <= bmi <= 25:
    print("Your weight is optimal.")
elif bmi < 18.5:
    print("You are underweight.")
elif bmi > 25:
    print("You are overweight.")
