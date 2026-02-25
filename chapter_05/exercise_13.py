#!/usr/bin/env python3

# Exercise 13:Falling Distance
# This program calculates the distance an object falls over time.

# Global constant for gravity
GRAVITY = 9.8

def main():
    # Display table headers
    print("Time (s)\tDistance (m)")
    print("----------------------------")
    
    for time in range(1, 11):
        # Get distance from function
        distance = falling_distance(time)

        # Display time and distance
        print(f"{time}\t{distance:.2f}")

    
def falling_distance(t):
    # Calculate distance using the formula d = 0.5 * g * t^2
    distance = 0.5 * GRAVITY * (t ** 2)
    return distance

# Call main function
main()
