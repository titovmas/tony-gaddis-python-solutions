#!/us/bin/env python3

# Exercise 06: Sales tax

# Constants for tax rates
STATE_TAX_RATE = 0.05
COUNTRY_TAX_RATE = 0.025

# Get the amount of the purchase from the user
purchase_amount = float(input("Enter the amount of the purchase: "))

# Calculate the state sales tax
state_tax = purchase_amount * STATE_TAX_RATE

# Calculate the country sales tax
country_tax = purchase_amount * COUNTRY_TAX_RATE

# Calculate the total sales tax
total_tax = state_tax + country_tax

# Calculate the total of the sale
total_sale = purchase_amount + total_tax

# Display the results
print(f"Purchase Amount: ${purchase_amount:,.2f}")
print(f"State Sales Tax: ${state_tax:,.2f}")
print(f"Country Sales Tax: ${country_tax:,.2f}")
print(f"Total Sale: ${total_sale:,.2f}")
