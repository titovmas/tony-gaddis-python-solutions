#!/usr/bin/env python3

# Exercise 18: Prime Number List
# This program displays all prime numbers from 1 to 100.

def main():
    # Print the header for the list
    print("Prime numbers between 1 and 100:")
    print("--------------------------------")
    
    # Loop through numbers 1 to 100
    for number in range(1, 101):
        # Check each number using the is_prime function
        if is_prime(number):
            # Print prime numbers on the same line for better layout
            print(number, end=' ')
            
    # Print a newline at the end
    print()

def is_prime(num):
    # Prime numbers must be greater than 1
    if num <= 1:
        return False
    
    # Check for divisors starting from 2
    for i in range(2, num):
        if num % i == 0:
            return False # Not a prime if a divisor is found
            
    # If no divisors found, the number is prime
    return True

# Call the main function
main()

