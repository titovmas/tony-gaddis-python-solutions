#!/usr/bin/env python3

# Exercise 04: Total sales volume

# Constant for the sales tax rate (7%)
TAX_RATE = 0.07

# Get the price of five items from the user
item1 =float(input("Enter the price of item #1: "))
item2 =float(input("Enter the price of item #2: "))
item3 =float(input("Enter the price of item #3: "))
item4 =float(input("Enter the price of item #4: "))
item5 =float(input("Enter the price of item #5: "))

# Calculate the subtotal of the sales
subtotal = item1 + item2 + item3 + item4 + item5

# Calculate the amount of sales tax
sales_tax = subtotal * TAX_RATE

# Calculate the total amount
total = subtotal + sales_tax

# Display the results
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Sales Tax: ${sales_tax:,.2f}")
print(f"Total: ${total:,.2f}")
