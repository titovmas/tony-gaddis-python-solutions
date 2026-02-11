#!/usr/bin/env python3

# Exercise 15: Drawing Patterns with Spaces
# This program uses nested loops to draw a specific pattern of # characters.

# Set the number of rows
ROWS = 6

# Use a for loop to display each row of the pattern
for row in range(ROWS):
    # Print the first hash mark
    print('#', end='')
    
    # Use a for loop to display the spaces between hashes
    for space in range(row):
        print(' ', end='')
        
    # Print the second hash mark and move to the next line
    print('#')
