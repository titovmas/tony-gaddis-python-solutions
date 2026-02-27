#!/usr/bin/env python3

# Exercise 17: Prime Numbers
# This program determines if a number is prime using a boolean function.

def main():
    # Get an integer from the user
    user_num = int(input("Enter an integer to check: "))
    
    # Check if the number is prime using the function
    if is_prime(user_num):
        print(f"{user_num} is a prime number.")
    else:
        print(f"{user_num} is NOT a prime number.")

def is_prime(num):
    # Prime numbers must be greater than 1
    if num <= 1:
        return False
    
    # Check for divisors from 2 up to num - 1
    # If any number divides evenly, it's not prime
    for i in range(2, num):
        if num % i == 0:
            return False # Found a divisor, so it's not prime
            
    # If no divisors were found, the number is prime
    return True

# Call the main function
main()
