#!/usr/bin/env python3

# Exercise 19: STOP Sign
# This program draws an octagon with the word STOP in the center.

import turtle

# Set the window
turtle.setup(600,600)

# Set the turtle
turtle.hideturtle()
turtle.speed(2)

# Constants for the octagon
SIDE_LENGTH = 200
ANGLE = 45



# Move turtle to a starting position so the sign is centered
turtle.penup()
turtle.goto(-100, 250)
turtle.pendown()


turtle.begin_fill()
turtle.fillcolor("red")

# Use a for loop to draw each side of the octagon
for side in range(8):

    turtle.forward(SIDE_LENGTH)
    turtle.right(ANGLE)

turtle.end_fill()

# Display the word STOP
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.color("white")
turtle.write("STOP", align="center", font=("Arial", 30, "bold"))

# Leave the window open
turtle.done()
