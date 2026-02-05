#!/usr/bin/env python3

# Exercise 10: The ingredient regulator

# Constants for the base recipe (48 cookies)
BASE_COOKIES = 48
SUGAR = 1.5
BUTTER = 1.0
FLOUR = 2.75

# Get the desired number of cookies from the user
cookies_wanted = float(input("Enter the number of cookies you want: "))

# Calculate the adjustment factor
factor = cookies_wanted / BASE_COOKIES

# Calculate the required amounts for each ingredient
sugar_needed = SUGAR * factor
butter_needed = BUTTER * factor
flour_needed = FLOUR * factor

# Display the requires amounts of ingredients
print(f"To make {cookies_wanted} cookies, you will need:")
print(f" - {sugar_needed:,.2f} cups of sugar")
print(f" - {butter_needed:,.2f} cups of butter")
print(f" - {flour_needed:,.2f} cups of flour")
