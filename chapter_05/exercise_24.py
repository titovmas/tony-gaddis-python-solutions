#!/usr/bin/env python3

# Exercise 24: Rectangular Pattern
# This program draws a nested rectangular pattern based on user input.

import turtle

def main():
    # Get dimensions from the user
    pattern_width = int(input("Enter the width of the pattern: "))
    pattern_height = int(input("Enter the height of the pattern: "))
    
    # Setup turtle
    turtle.setup(800, 800)
    turtle.speed(1)
    turtle.hideturtle()
    
    # Call the pattern function
    draw_pattern(pattern_width, pattern_height)
    
    # Finish
    turtle.done()

def draw_pattern(w, h):
    # 1. Draw the outer rectangle
    draw_rectangle(-w/2, -h/2, w, h)

    # 2. Draw the middle rectangle (half size)
    draw_rectangle(-w/4, -h/4, w/2, h/2)

    # 3. Draw the inner rectangle (quarter size with filling)
    turtle.begin_fill()
    draw_rectangle(-w/8, -h/8, w/4, h/4)
    turtle.end_fill()
 
    # 4. Draw the connecting lines
    # Diagonal line: bottom-left to top-right
    draw_line(-w/2, -h/2, w/2, h/2)
    # Diagonal line: top-left to bottom-right
    draw_line(-w/2, h/2, w/2, -h/2)
    # Vertical line: middle
    draw_line(0, -h/2, 0, h/2)
    # Horizontal line: middle
    draw_line(-w/2, 0, w/2, 0)

def draw_rectangle(x, y, width, height):
    # Helper function to draw a rectangle 
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.penup()

def draw_line(x1, y1, x2, y2):
    # Helper function to draw a line
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()

# Call main function
main()
