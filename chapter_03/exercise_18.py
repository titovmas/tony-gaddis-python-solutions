#!/usr/bin/env python3

# Exercise 18: Restaurant Selector
# This program filters restaurants based on several dietary restrictions.

# Step 1: Get user input for dietary restrictions
veg_input = input("Is anyone in your party a vegetarian? (yes/no): ")
vegan_input = input("Is anyone in your party a vegan? (yes/no): ")
gf_input = input("Is anyone in your party gluten-free? (yes/no): ")

# Step 2: Convert inputs to boolean values
is_veg = veg_input == "yes"
is_vegan = vegan_input == "yes"
is_gf = gf_input == "yes"

print("\nHere are your restaurant options:")

# Step 3: Check each restaurant against the restrictions
# 1. Joe’s Gourmet Burgers (Only if NO restrictions at all)
if not is_veg and not is_vegan and not is_gf:
    print("Joe's Gourmet Burgers")

# 2. Main Street Pizza Company (Vegetarian and Gluten-Free, but NOT Vegan)
if not is_vegan:
    print("Main Street Pizza Company")

# 3. Corner Cafe (Suitable for everyone)
print("Corner Cafe")

# 4. Mama’s Italian (Vegetarian only, NOT Vegan or Gluten-Free)
if not is_vegan and not is_gf:
    print("Mama's Italian")

# 5. The Chef’s Kitchen (Suitable for everyone)
print("The Chef's Kitchen")

