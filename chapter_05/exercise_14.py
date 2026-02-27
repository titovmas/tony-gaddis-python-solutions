#!/usr/bin/env python3

# Exercise 14: Kinetic Energy
# This program calculates kinetic energy based on mass and velocity.

def main():
    # Get the mass of the object in kilograms
    mass = float(input("Enter the object's mass in kilograms: "))
    
    # Get the velocity of the object in meters per second
    velocity = float(input("Enter the object's velocity in meters per second: "))
    
    # Call the kinetic_energy function and store the result
    ke = kinetic_energy(mass, velocity)
    
    # Display the calculated kinetic energy
    print(f"The kinetic energy for this object is {ke:,.2f} Joules.")

def kinetic_energy(m, v):
    # Calculate kinetic energy using the formula KE = 0.5 * m * v^2
    energy = 0.5 * m * (v ** 2)
    return energy

# Call the main function
main()
