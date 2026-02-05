#!/usr/bin/env python3

# Exercise 14: Compound Interest Calculator

# Get the principal amount deposited into the account
principal = float(input("Enter the starting principal: "))

# Get the annual interest rate
# Example: 0.05 for 5%
rate = float(input("Enter the annual interest rate (decimal): "))

# Get the number of times per year interest is compounded
compounded = int(input("Enter the compounding frequency (per year): "))

# Get the number of years the account will earn interest
years = float(input("Enter the number of years: "))

# Calculate the amount of money in the account after the specified years
amount = principal * (1 + rate / compounded) ** (compounded * years)

# Display the final balance
print(f"Final balance after {years:.0f} years: ${amount:,.2f}")
