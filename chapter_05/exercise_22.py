#!/usr/bin/env python3

# Exercise 22: Triangle Function
# This program uses the turtle module to draw 
# a filled triangle at specific coordinates.

import turtle


def main():
    # Setup the turtle screen
    turtle.setup(600, 600)
    turtle.speed(3)
    
    # Draw the first triangle (Red) at coordinates (0, 0)
    triangle(0, 0, "red")
    
    # Keep the window open until it is clicked
    print("Click on the graphics window to exit.")
    turtle.exitonclick()

def triangle(xcor, ycor, color):
    # Move the turtle to the specified coordinates without drawing
    turtle.penup()
    turtle.goto(xcor, ycor)
    turtle.pendown()

    # Set the fill color and start filling
    turtle.fillcolor(color)
    turtle.begin_fill()
   
    # Draw an equilateral triangle
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    
    # Complete the filling process
    turtle.end_fill()


# Call the main function
main()
