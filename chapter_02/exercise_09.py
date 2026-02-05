#!/usr/bin/env python3

# Exercise 09: Convert degrees Celsius to degrees Fahrenheit

# Get the temperature in Celsius from the user
celsius = float(input("Enter the temperature in Celsius: "))

# Calculate the temperature in Fahreinheit using the formula
# F = (9/5 * C) + 32
fahreinheit = (9 / 5) * celsius + 32

# Display the result
print(f"Celsius: {celsius}° | Fahreinheit {fahreinheit:.1f}°")
