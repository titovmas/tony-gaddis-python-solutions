#!/usr/bin/env python3

# Exercise 02: Sales tax with functions

# Constants for tax rates
STATE_TAX_RATE = 0.05
COUNTRY_TAX_RATE = 0.025

def main():
    # Get the total sales from the user
    total_sales = float(input("Enter the total monthly sales: "))
    
    # Use a function to calculate and display taxes
    show_tax_details(total_sales)

def show_tax_details(sales):
    # Calculate individual taxes
    state_tax = sales * STATE_TAX_RATE
    county_tax = sales * COUNTY_TAX_RATE
    total_tax = state_tax + county_tax
    
    # Display the results
    print(f"State Sales Tax: ${state_tax:,.2f}")
    print(f"County Sales Tax: ${county_tax:,.2f}")
    print(f"Total Sales Tax: ${total_tax:,.2f}")



# Call the main function to start the program
main()
