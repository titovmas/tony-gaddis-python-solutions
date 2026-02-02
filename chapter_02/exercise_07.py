#!/usr/bin/env python3

# Exercise 07: Gasoline consumption per kilometers traveled

# Get the number of kilometers driven from the user
kilometers_driven = float(input("Enter the number of kilometers driven: "))

# Get the number of litres of fuel used
litres_used = float(input("Enter the litres of fuel used: "))

# Calculate the kilometer-per-litres(km/L)
km_l = kilometers_driven / litres_used

# Display the result
print(f"Your car's fuel consumption is {km_l:.2f} kilometer per litre")
