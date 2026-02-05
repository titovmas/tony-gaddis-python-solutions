#!/usr/bin/env python3

# Exercise 12: Stock Trading Calculator

# Constant for the transaction
NUM_SHARES = 2000
PURCHASE_PRICE_PER_SHARE = 40.00
SELLING_PRICE_PER_SHARE = 42.75
COMMISSION_RATE = 0.03

# Calculate purchase details 
amount_paid_for_stock = NUM_SHARES * PURCHASE_PRICE_PER_SHARE
buy_commission = amount_paid_for_stock * COMMISSION_RATE

# Calculate sales details
amount_received_from_sale = NUM_SHARES * SELLING_PRICE_PER_SHARE
sell_commission = amount_received_from_sale * COMMISSION_RATE

# Calculate total costs (purchase price + both commissions) 
total_costs = amount_paid_for_stock + buy_commission + sell_commission

# Calculate final profit
total_profit = amount_received_from_sale - total_costs

# Display the results
print(f"Amount paid for the stock: ${amount_paid_for_stock:,.2f}")
print(f"Commission paid on purchase: ${buy_commission:,.2f}")
print(f"Amount stock sold for: ${amount_received_from_sale:,.2f}")
print(f"Commission paid on sale: ${sell_commission:,.2f}")
print("---------------------------------------")
print(f"Profit/Loss: ${total_profit:,.2f}")
