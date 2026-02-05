#!/usr/bin/env python3

# Exercise 11: Male/Female Ratio

# Get the number of males and females from the user
males = int(input("Enter the number of males in the class: "))
females = int(input("Enter the number of females in the class: "))

# Calculate the total number of students
total_students = males + females

# Calculate the percentage of each gender
# Formula: (part / total) * 100
male_percentage = (males / total_students) * 100
female_percentage = (females / total_students) * 100

# Display the results
print(f"Total students: {total_students}")
print(f"Percentage of males: {male_percentage:.2f}%")
print(f"Percentage of females: {female_percentage:.2f}%")
