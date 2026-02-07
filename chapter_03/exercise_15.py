#!/usr/bin/env python3

# Exercise 15: Time Calculator
# This program converts a given number of seconds into days, hours, and minutes.

# Get the number of seconds from the user
total_seconds = int(input("Enter a number of seconds: "))


# Initialize variables
days = 0
hours = 0
minutes = 0
seconds = 0

# Check if the input is enough to form any time units
if total_seconds >= 86400:
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(f"Days: {days}, Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")

elif total_seconds >= 3600:
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")

elif total_seconds >= 60:
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    print(f"Minutes: {minutes}, Seconds: {seconds}")

else:
    seconds = total_seconds
    print(f"Seconds: {seconds}")
