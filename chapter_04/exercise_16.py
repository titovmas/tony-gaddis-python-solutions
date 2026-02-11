#!/usr/bin/env python3

# Exercise 16: Repeating Squares
# This program draws a pattern of 100 squares using nested loops.

import turtle

# Set  # Set window size
turtle.setup(800, 800)
 
# Setup turtle
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(250, -250)
turtle.pendown()

# Set the starting size and the increment
size = 5
INCREMENT = 5

# Use a for loop to draw 100 squares
for square in range(100):
    # Use a for loop to draw each side of the square
    for side in range(4):
        turtle.left(90)
        turtle.forward(size)
    
    # Increase the size for the next square
    size += INCREMENT

# Leave the window open
turtle.done()
