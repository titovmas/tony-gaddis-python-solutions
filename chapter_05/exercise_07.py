#!/usr/bin/env python3

# Exercise 7: Stadium Seating
# This program calculates total income from ticket sales using functions.

# Constants for ticket prices
TICKET_A = 20
TICKET_B = 15
TICKET_C = 10

def main():
    # Get number of tickets sold for each class
    count_a = int(input("Enter tickets sold for Class A: "))
    count_b = int(input("Enter tickets sold for Class B: "))
    count_c = int(input("Enter tickets sold for Class C: "))
    
    # Use a function to calculate and display the total income
    show_income(count_a, count_b, count_c)

def show_income(a, b, c):
    # Calculate total amount
    total = (a * TICKET_A) + (b * TICKET_B) + (c * TICKET_C)

    # Display the result
    print(f"Total income from ticket sales: ${total:,.2f}")

# Call main function
main()
