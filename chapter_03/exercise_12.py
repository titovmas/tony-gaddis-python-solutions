#!/usr/bin/env python3

# Exercise 12: Software Sales
# This program calculates the discount and total cost of a software purchase.

# Constant for the retail price
RETAIL_PRICE = 99.0

# Get the number of packages from the user
quantity = int(input("Enter the number of packages purchased: "))

# Determine the discount percentage based on quantity ranges
if 0 <= quantity < 10:
    discount_percent = 0
elif 10 <= quantity <= 19:
    discount_percent = 10
elif 20 <= quantity <= 49:
    discount_percent = 20
elif 50 <= quantity <= 99:
    discount_percent = 30
elif quantity >= 100:
    discount_percent = 40
else:
    # Flag for negative input errors
    discount_percent = -1

# Check for valid input and perform final calculations
if discount_percent >= 0:
    # Calculate total price without any discount
    full_price = quantity * RETAIL_PRICE

    # Calculate the discount amount (e.g., 20% of 100 is 20)
    discount_amount = full_price * (discount_percent / 100)

    # Subtract discount from full price
    total_price = full_price - discount_amount

    # Show results to the user
    print(f"Discount percentage: {discount_percent}%")
    print(f"Discount amount: ${discount_amount:,.2f}")
    print(f"Total purchase amount: ${total_price:,.2f}")
else:
    # Error message if the user enters a negative number
    print("Error: Quantity cannot be negative.")
