#!/usr/bin/env python3

# Exercise 08: Tips, tax, and total amount

# Constant for tip and tax rates
TIP_RATE = 0.18
TAX_RATE = 0.07

# Get the charge for the forod from user
food_charge = float(input("Enter the charge for the food: "))

# Calculate the amount of tip
tip_amount = food_charge * TIP_RATE

# Calculate the amount of the tax
tax_amount = food_charge * TAX_RATE

# Calculate the total amount
total = food_charge + tip_amount + tax_amount

# Display the calculated amounts
print(f"Food Charge:    ${food_charge:,.2f}")
print(f"Tip (18%):      ${tip_amount:,.2f}")
print(f"Sales tax (7%): ${tax_amount:,.2f}")
print("---------------------------------")
print(f"Total:          ${total:,.2f}")
