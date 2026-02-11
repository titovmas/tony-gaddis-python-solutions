#!/usr/bin/env python3

# Exercise 18: Hypnotic Pattern
# This program draws a square spiral pattern.

import turtle

# Set the window 
turtle.setup(600,600)

# Set turtle
turtle.speed(5)
turtle.hideturtle()

# Set initial distance and increment
distance = 5
INCREMENT = 5

# Use a for loop to draw each segment of the spiral
for i in range(50):
    turtle.forward(distance)
    turtle.left(90)
    # Increase the distance for the next segment
    distance += INCREMENT

# Leave the window open
turtle.done()
