#!/usr/bin/env python3

# Exercise 13: Population
# This program predicts the approximate size of a population of organisms.

# Get the starting parameters
start_organisms = float(input("Starting number of organisms: "))
daily_increase = float(input("Average daily increase (as a percentage): "))
days = int(input("Number of days to multiply: "))

# Convert percentage to decimal
increase_rate = daily_increase / 100

# Initialize the current population
current_population = start_organisms

# Print table header
print("Day\tApproximate Population")
print("-------------------------------")

# Use a for loop to calculate daily population growth
for day in range(1, days + 1):
    if day == 1:
        # Display starting population on day 1
        print(f"{day}\t{current_population}")
    else:
        # Update and display population for subsequent days
        current_population += (current_population * increase_rate)
        print(f"{day}\t{current_population:,.2f}")
