#!/usr/bin/env python3

# Exercise 03: Budget Analysis
# This program tracks expenses against a monthly budget.

# Get the monthly budget from the user
budget = float(input("Enter the amount budgeted for the month: "))

# Initialize the accumulator for total expenses
total_expenses = 0.0

# Initialize the loop control variable
keep_going = 'y'

# Start the while loop
while keep_going == 'y':
    expense = float(input("Enter an expense: "))

    # Add the expense to the total
    total_expenses += expense

    # Ask the user if they want to continue
    # Note: If they type 'Y' (capital), the loop will stop
    keep_going = input("Do you have another expense? (y/n): ")


# Calculate the difference (remaining budget or overage)
difference = budget - total_expenses

# Display the financial summary
print("\n--- Budget Summary ---")
print("Budgeted Amount: ", budget)
print("Total Expenses:  ", total_expenses)


# Determine if the user is over or under budget
if difference > 0:
    print("You are under budget by: ", difference)
elif difference < 0:
    # Use -difference to show a positive number for the overage
    print("You are over budget by: ", -difference)
else:
    print("You spent exactly what you budgeted.")
