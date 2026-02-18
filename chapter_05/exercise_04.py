#!/usr/bin/env python3

# Exercise 04: Automobile Costs
# This program calculates total monthly and annual automobile expenses.

def main():
    # Get monthly expenses from the user
    loan = float(input("Enter the monthly loan payment: "))
    insurance = float(input("Enter the monthly insurance: "))
    gas = float(input("Enter the monthly gas expense: "))
    oil = float(input("Enter the monthly oil expense: "))
    tires = float(input("Enter the monthly tires expense: "))
    maintenance = float(input("Enter the monthly maintenance: "))


    # Use a function to calculate and display total costs
    show_expenses(loan, insurance, gas, oil, tires, maintenance)

def show_expenses(loan, ins, gas, oil, tires, main):
    # Calculate monthly and annual totals
    total_monthly = loan + ins + gas + oil + tires + main
    total_annual = total_monthly * 12

    # Display the results
    print(f"\nTotal monthly expense: ${total_monthly:,.2f}")
    print(f"Total annual expense: ${total_annual:,.2f}")

# Call the main function
main()
