#!/usr/bin/env python3

# Exercise 06: Calories from Fat and Carbohydrates
# This program calculates calories from fat and carbs using functions.

# Constants
CALORIE_PER_FAT = 9
CALORIE_PER_CARB = 4





def main():
    # Get grams of fat and carbohydrates
    fat_grams = float(input("Enter the grams of fat: "))
    carb_grams = float(input("Enter the grams of carbohydrates: "))

    # Use a function to calculate and display calories from fat
    show_fat_calories(fat_grams)

    # Use a function to calculate and display calories from carbs
    show_carb_calories(carb_grams)

def show_fat_calories(fat):
    # Calculate and display calories from fats
    fat_calories = fat * CALORIE_PER_FAT
    print(f"Calories from fats: {fat_calories:.1f}")

def show_carb_calories(carb):
    # Calculate and display calories from carb
    carb_calories = carb * CALORIE_PER_CARB
    print(f"Calories from carbs: {carb_calories:.1f}")

# Call main function
main()
