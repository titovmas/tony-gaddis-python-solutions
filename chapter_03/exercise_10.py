#!/usr/bin/env python3

# Exercise_10: Money Counting Game
# This program asks the user to enter coins to total exactly one dollar.


# Constants for coin values in cents
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
DOLLAR_VALUE = 100


# Get input from the user
print("Try to make exactly $1.00!")
pennies = int(input("Enter number of pennies: "))
nickels = int(input("Enter number of nickels: "))
dimes = int(input("Enter number of dimes: "))
quarters = int(input("Enter number of quarters: "))

# Calculate the total value in cents
total_cents = ( pennies * PENNY_VALUE + \
                nickels * NICKEL_VALUE + \
                dimes * DIME_VALUE + \
                quarters * QUARTER_VALUE )

# Compare the total value with 100 cents
if total_cents == DOLLAR_VALUE:
    print("Congratulations! You won the game!")
    print("The total is exactly one dollar.")
elif total_cents > DOLLAR_VALUE:
    # Calculate how much they went over
    over_amount = (total_cents - DOLLAR_VALUE) / 100
    print(f"Sorry, that's too much. You went over by ${over_amount:.2f}")
else:
    # Calculate the remaining amount
    under_amount = (DOLLAR_VALUE - total_cents) / 100
    print(f"Sorry, that's too little. You are short by ${under_amount:.2f}")
