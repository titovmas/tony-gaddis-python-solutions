#!/usr/bin/env python3

# Exercise 17: Star Pattern
# This program draws a star pattern using a loop.

import turtle

# Set window size
turtle.setup(600, 600)

# Setup turtle
turtle.speed(5)
turtle.hideturtle()
turtle.penup()
turtle.goto(-150, -50)
turtle.pendown()

# Use a for loop to draw the star pattern
for i in range(8):
    # Draw a line and return to center to create a ray
    turtle.forward(300)
    turtle.left(135)

# Leave the window open
turtle.done()
