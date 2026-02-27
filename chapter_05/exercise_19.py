#!/usr/bin/env python3

# Exercise 19: Future Value
# This program calculates the future value of a savings account.

def main():
    # Get current value from user
    present_value = float(input("Enter the account's present value: "))
    
    # Get monthly interest rate (e.g., 0.005 for 0.5%)
    interest_rate = float(input("Enter the monthly interest rate: "))
    
    # Get the number of months money will sit in the account
    months = int(input("Enter the number of months: "))
    
    # Calculate future value using the function
    future_value = calculate_future_value(present_value, interest_rate, months)
    
    # Display the result
    print(f"The predicted future value of the account is: ${future_value:,.2f}")

def calculate_future_value(p, i, t):
    # Calculate future value: F = P * (1 + i)^t
    result = p * ((1 + i) ** t)
    return result

# Call the main function
main()

