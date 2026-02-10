#!/usr/bin/env python3

# Exercise 04: Distance Traveled
# This program calculates and displays a table of distance traveled for each hour.

# Get the speed of the vehicle
speed = float(input("What is the speed of vehicle in kmh: "))

# Get thethe number of hours traveled
hours = int(input("How many hours has it traveled? "))

# Print the table header
print("Hour\t\tDistance Traveled")
print("--------------------------")

# Use a for loop to calculate distance for each hour
for current_hour in range(1, hours + 1):
    # Calculate distance for the current hour
    distance = current_hour * speed

    # Display the hour and the distance
    print(f"{current_hour}\t\t{distance}")
