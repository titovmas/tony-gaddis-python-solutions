#!/usr/bin/env python3

# Exercise 26: City Skyline
# This program draws a night city silhouette with stars and windows.

import turtle
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SKY_COLOR = "black"
BUILDING_COLOR = "gray"
WINDOW_COLOR = "yellow"
STAR_COLOR = "white"
WINDOW_SIZE = 20

def main():
    # Setup window and turtle speed
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.bgcolor(SKY_COLOR)
    turtle.speed(2)
    turtle.hideturtle()
    
    # Layer 1: Stars (backgrounfd)
    draw_stars(50)

    # Layer 2: City Silhouette
    draw_buildings(BUILDING_COLOR)
    
    # Keep the window open
    turtle.done()

def draw_buildings(color):
    # Initialize drawing position
    turtle.penup()
    turtle.goto(-400, -400)
    turtle.pendown()
    turtle.pencolor('grey')
    turtle.fillcolor(color)
    
    # Start creating the solid silhouette
    turtle.begin_fill()

    # Connect point to form the city silhouette
    turtle.goto(-400, -150)
    turtle.goto(-300, -150)
    turtle.goto(-300, 0)
    turtle.goto(-200, 0)
    turtle.goto(-200, 300)
    turtle.goto(0, 300)
    turtle.goto(0, -50)
    turtle.goto(100, -50)
    turtle.goto(100, 200)
    turtle.goto(250, 200)
    turtle.goto(250, 0)
    turtle.goto(300, 0)
    turtle.goto(300, -150)
    turtle.goto(400, -150)
    turtle.goto(400, -400)
    turtle.goto(-400, -400)
    
    turtle.end_fill()

    # Layer 3: Windows
    draw_windows(WINDOW_COLOR, WINDOW_SIZE)

def draw_windows(color, size):
    turtle.penup()
    
    # Building 1 window
    turtle.goto(-280, -20)
    draw_square(color, size)
    
    # Building 2 windows
    turtle.goto(-180, 260)
    draw_square(color, size)
    turtle.goto(-180, 230)
    draw_square(color, size)
    
    # Center area window
    turtle.goto(-40, 150)
    draw_square(color, size)
    turtle.goto(-60, -120)
    draw_square(color, size)

    # Building 3 window
    turtle.goto(120, 160)
    draw_square(color, size)

def draw_square(color, size):
    # Draw a singe filled square for a window
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def draw_stars(count):
    # Scatter random stars across the sky
    for _ in range(count):
        x = random.randint(-400, 400)
        y = random.randint(100, 400) # Keep stars above the skyline
        
        turtle.penup()
        turtle.goto(x, y)
        
        # Draw star as a point 
        turtle.dot(random.randint(2, 4), STAR_COLOR)

# Call the main function
main()
