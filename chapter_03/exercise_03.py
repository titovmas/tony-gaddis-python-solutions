#!/usr/bin/env python3

# Exercise 03: Age Classifier
# This program categorizes a person based on their age input.

# Get the age from user
age = int(input("Enter the person's age: "))

# Categorize the person based on age
if age < 1:
    print("This person is an toddler.")
elif age < 13:
    print("This person is a child.")
elif age < 20:
    print("This person is a teenager.")
else:
    # Any age 20 or greater falls here
    print("This person is an adult.")
