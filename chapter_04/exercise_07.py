#!/usr/bin/env python3

# Exercise 07: Pennies for Pay
# This program calculates how much a person would earn if their
# salary doubles each day, starting with one penny.

# Get the number of days from the user
days = int(input("Enter the number of days: "))
 
# Initialize the daily pay in pennies
daily_pay = 1

# Initialize the accumulator for total pay
total_pennies = 0

# Print table header
print("Day\tSalary (in Pennies)")
print("---------------------------")

# Use a loop to calculate pay for each day
for day in range(1, days + 1):
    # Display the current day and the pay for that day
    print(f"{day}\t{daily_pay}")

    # Add daily pay to the total accumulator
    total_pennies += daily_pay

    # Double the pay for the next day
    daily_pay *= 2

# Calculate total in major currency (Rubles)
total_currency = total_pennies / 100

# Display the final total
print("---------------------------")
print(f"Total salary after {days} days: {total_currency:,.2f}")
