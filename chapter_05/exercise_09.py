#!/usr/bin/env pyton3

# Exercise 09: Monthly Sales Tax
# This program calculates monthly sales tax from total sales.

# Constants for tax rates
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

def main():
    # Get total monthly sales amount from user
    total_sales = float(input("Enter the total monthly sales: "))
    
    # Use a function to calculate and display taxes
    show_tax_details(total_sales)

def show_tax_details(sales):
    # Calculate individual taxes
    state_tax = sales * STATE_TAX_RATE
    county_tax = sales * COUNTY_TAX_RATE
    total_tax = state_tax + county_tax
    
    # Display the results in English
    print(f"County Sales Tax: ${county_tax:,.2f}")
    print(f"State Sales Tax: ${state_tax:,.2f}")
    print(f"Total Sales Tax: ${total_tax:,.2f}")

# Call main function
main()
