#!/usr/bin/env python3

# Exercise 23: Snowman
# This program draws a snowman using separate functions for each part.

import turtle

def main():
    # Set up the window
    turtle.setup(700, 900)
    turtle.speed(5)
    turtle.pensize(2)
    turtle.hideturtle()
    
    # Draw the snowman parts
    draw_base()
    draw_mid_section()
    draw_head()
    draw_arms()
    draw_hat()
    
    # Hide turtle and keep window open
    turtle.done()




def draw_base():
    turtle.penup()
    turtle.goto(0, -400)
    turtle.pendown()
    turtle.circle(150)
    turtle.penup()

def draw_mid_section():
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()

def draw_head():
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()
    turtle.goto(-20, 150)
    turtle.pendown()
    turtle.circle(8)
    turtle.penup()
    turtle.goto(20, 150)
    turtle.pendown()
    turtle.circle(8)
    turtle.penup()
    turtle.goto(-25, 130)
    turtle.pendown()
    turtle.goto(25, 130)
    turtle.penup()

def draw_arms():
    # Drawing right hand
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.goto(-170, 20)
    turtle.goto(-180, 90)
    turtle.goto(-180, 105)
    turtle.penup()
    turtle.goto(-180, 90)
    turtle.pendown()
    turtle.goto(-195, 90)
    turtle.penup()

    # Drawing left hand
    turtle.goto(100, 0)
    turtle.pendown()
    turtle.goto(180, 60)
    turtle.goto(180, 75)
    turtle.penup()
    turtle.goto(180, 60)
    turtle.pendown()
    turtle.goto(195, 60)
    turtle.penup()

def draw_hat():
    turtle.goto(-80, 190)
    turtle.fillcolor('black')
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(-80, 230)
    turtle.goto(-40, 230)
    turtle.goto(-40, 320)
    turtle.goto(40, 320)
    turtle.goto(40, 230)
    turtle.goto(80, 230)
    turtle.goto(80, 190)
    turtle.goto(-80, 190)
    turtle.end_fill()

# Call the main function
main()
