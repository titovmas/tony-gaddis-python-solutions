#!/usr/bin/env python3

# Exercise 13: Grapevine Calculator

# Get the length of the row in meters
row_length = float(input("Enter the length of the row, in meters: "))

# Get the amount of space used by an end-post assembly
end_post_space = float(input("Enter the end-post space, in meters: "))

# Get the distance between vines
vine_spacing = float(input("Enter the distance between vines, in meters: "))

# Calculate the number of grapevines that will fit in the row
# Formula: V = (R - 2E) / S
num_vines = (row_length - 2 * end_post_space) / vine_spacing

# Display the result
print(f"You can plant {int(num_vines)} grapevines in this row.")
