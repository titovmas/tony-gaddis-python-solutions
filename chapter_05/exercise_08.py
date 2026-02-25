#!/usr/bin/env python3

# Exercise 08: Paint Job Estimator
# This program calculates costs and requirements for a painting job.

import math

# Constants
METERS_PER_CONTAINER = 10
LITERS_PER_CONTAINER = 5
HOURS_PER_UNIT = 8
LABOR_COST_PER_HOUR = 2000

def main():
    # Get the square meters and paint price from user
    sq_meters = float(input("Enter the total square meters of wall: "))
    paint_price = float(input("Enter the price of 5-liter paint container: "))
    
    # Use a function to calculate and display the estimate
    show_estimate(sq_meters, paint_price)

def show_estimate(area, price):
    # Calculate the number of containers
    containers = math.ceil(area / METERS_PER_CONTAINER)

    # Calculate the labor hours
    labor_hours = (area / METERS_PER_CONTAINER) * HOURS_PER_UNIT

    # Calculate the costs
    paint_cost = containers * price
    labor_cost = labor_hours * LABOR_COST_PER_HOUR
    total_cost = paint_cost + labor_cost

    # Display the results
    print(f"\nContainers of paint: {containers}")
    print(f"Labor hours: {labor_hours:.1f}")
    print(f"Paint cost: {paint_cost:,.2f} RUB")
    print(f"Labor cost: {labor_cost:,.2f} RUB")
    print(f"Total cost: {total_cost:,.2f} RUB")

# Call main function
main()
