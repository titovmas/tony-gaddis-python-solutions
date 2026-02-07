#!/usr/bin/env python3

# Exercise 11: Book Club Points
# This program calculates points awarded based on book purchases.


# Get the number of books from the user
books_purchased = int(input("Enter the number of books you purchased: "))

# Calculate points based on the book club's specific scale
if 0 <= books_purchased < 2:
    points = 0
elif 2 <= books_purchased < 4:
    points = 5
elif 4 <= books_purchased < 6:
    points = 15
elif 6 <= books_purchased < 8:
    points = 30
elif books_purchased >= 8:
    points = 60
else:
    # Handle negative numbers just in case
    points = 0
    print("Invalid input. Number of books cannot be negative.")

# Display the total points earned
if books_purchased >=0:
    print(f"Points earned: {points}")
