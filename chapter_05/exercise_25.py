#!/usr/bin/env python3

# Exercise 25: Chess Board
# This program draws a 8x8 chessboard pattern using a square function.

import turtle

# Constants
HEIGHT = 50

def main():
    # Setup window size and drawing speed
    turtle.setup(500, 500)
    turtle.speed(0)
    turtle.hideturtle()
    
    # Initial coordinates
    start_x = -200
    start_y = 200
    
    # Outer loop for rows
    for row in range(8):
        # Inner loop for columns
        for col in range(8):

            # Calculate the top-left (x, y) position for the current square
            x = start_x + (col * HEIGHT)
            y = start_y - (row * HEIGHT)

            # Determine cell color using parity check
            if (row + col) % 2 == 0:
                draw_square(x, y, HEIGHT, 'black')
            else:
                draw_square(x, y, HEIGHT, 'white')
    # Keep the window open
    turtle.done()

def draw_square(x, y, height, color):
    # Move the turtle to the starting position
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Set the fill color and start the filling process
    turtle.fillcolor(color)
    turtle.begin_fill()

    # Draw the four sides of the square
    for i in range(4):
        turtle.forward(height)
        turtle.right(90)

    turtle.end_fill()
    turtle.penup()

# Call the main function
main()
