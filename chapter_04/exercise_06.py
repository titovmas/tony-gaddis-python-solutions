#!/usr/bin/env python3

# Exercise 06: Celsius to Fahrenheit Table
# This program displays a conversion table from 0 to 20 degrees Celsius.

# Print the table header
# \t is used for alignment
print("Celsius\tFahrenheit")
print("--------------------")

# Use a for loop to iterate from 0 to 20
for celsius in range(1, 21):
    # Calculate Fahrenheit
    fahrenheit = (9 / 5) * celsius + 32

    # Display the results
    print(f"{celsius:.2f}\t{fahrenheit:.2f}")
