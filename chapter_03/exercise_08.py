#!/usr/bin/env python3

# Exercise 08: Hot Dog Cookout Calculator
# This program calculates the number of packages needed for a cookout.

# Constant 
SAUSAGES_PER_PKG = 10
BUNS_PER_PKG = 8

# Get input from the user
num_people = int(input("Enter the number of people: "))
hot_dogs_per_person = int(input("Enter the number of hot dogs per person: "))

# Calculate total hot dogs needed
total_needed = num_people * hot_dogs_per_person

# Calculate packages of sausages
sausages_pkgs = total_needed // SAUSAGES_PER_PKG
if total_needed % SAUSAGES_PER_PKG:
    sausages_pkgs += 1

# Calculate packages of buns
buns_pkgs = total_needed // BUNS_PER_PKG
if total_needed % BUNS_PER_PKG > 0:
    buns_pkgs += 1

# Calculate leftovers
sausages_left = (sausages_pkgs * SAUSAGES_PER_PKG) - total_needed
buns_left = (buns_pkgs * BUNS_PER_PKG) - total_needed

# Display results
print(f"Minimum packages of sausages: {sausages_pkgs}")
print(f"Minimum packages of buns: {buns_pkgs}")
print(f"Sausages left over: {sausages_left}")
print(f"Buns left over: {buns_left}")
