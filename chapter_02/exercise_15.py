#!/usr/bin/env python3

# Exercise 15: Geometric patterns using Turtle Graphics

import turtle

# Initial setup for the drawing canvas
turtle.setup(800, 800)
turtle.speed(2)
turtle.hideturtle()
turtle.pensize(2)

# ---Figure 1: Parallel Rhombus / Shaded shape ---
turtle.penup()
turtle.goto(-350, 270)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.left(45)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

# Reset heading for the next figure to avoid cumulative angle errors
turtle.penup()
turtle.setheading(60)

# --- Figure 2: Triangle with an inscibed shaded square ---
turtle.goto(120, 200)
turtle.pendown()

# Main triangle outline
turtle.forward(170)
turtle.right(120)
turtle.forward(170)
turtle.right(120)
turtle.forward(170)

# Inner shaded part
turtle.right(135)
turtle.begin_fill()
turtle.forward(120.21)
turtle.right(90)
turtle.forward(120.21)
turtle.right(135)
turtle.forward(170)
turtle.end_fill()

# Reset heading for the next figure to avoid cumulative angle errors
turtle.penup()
turtle.setheading(0)

# --- Figure 3: 3D Box (Isometric view) ---
turtle.goto(-300,150)
turtle.pendown()

# Drawing the interconnected vertices of the cube
turtle.goto(-200, 150)
turtle.goto(-200, -50)
turtle.goto(-100, -50)
turtle.goto(-100, 50)
turtle.goto(-300, 50)
turtle.goto(-300, 150)
turtle.goto(-100, -50)

# Adding depth lines (edges)
turtle.penup()
turtle.goto(-300, 50)
turtle.pendown()
turtle.goto(-200, -50)
turtle.penup()
turtle.goto(-200, 150)
turtle.pendown()
turtle.goto(-100, 50)


# Figure 4: Olympic-style interlocking circles ---
# Adjusting coordinates for a balanced layout
turtle.penup()
turtle.goto(100, 50)
turtle.pendown()
turtle.circle(42)

turtle.penup()
turtle.goto(200, 50)
turtle.pendown()
turtle.circle(42)

turtle.penup()
turtle.goto(300, 50)
turtle.pendown()
turtle.circle(42)

# Bottom row of circles
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()
turtle.circle(42)

turtle.penup()
turtle.goto(250, 0)
turtle.pendown()
turtle.circle(42)

# --- Figure 5: Compass Rose with Cardinal Directions ---
turtle.penup()
# Draw the horizontal axis (West - East)
turtle.goto(-320, -250)
turtle.pendown()
turtle.goto(-80, -250)

# Draw the vertical axis (North - South)
turtle.penup()
turtle.goto(-200, -130)
turtle.pendown()
turtle.goto(-200, -370)

# Draw a small center circle to anchor the compass
turtle.penup()
turtle.goto(-200, -280)
turtle.pendown()
turtle.circle(30)

# Add text labels for directions
turtle.penup()
# Label: North
turtle.goto(-212, -130)
turtle.write("North", font=("Arial", 10, "bold"))
# Label: East
turtle.goto(-75, -255)
turtle.write("East", font=("Arial", 10, "bold"))
# Label: South
turtle.goto(-212, -385)
turtle.write("South", font=("Arial", 10, "bold"))
# Label: West
turtle.goto(-353, -255)
turtle.write("West", font=("Arial", 10, "bold"))

# --- Figure 6: Geometric Grid with Nodes and Dashed Lines ---
turtle.goto(100, -130)
turtle.pendown()

# Mark the vertices (corners) and the center with dots
turtle.dot(15)  # Top-left
turtle.goto(100, -370)
turtle.dot(15)  # Bottom-left
turtle.goto(340, -130)
turtle.dot(15)  # Top-right
turtle.goto(340, -370)
turtle.dot(15)  # Bottom-right
turtle.goto(220, -250)
turtle.dot(15)  # Center point
turtle.goto(100, -130)

# Draw segmented (dashed) top horizontal line
turtle.goto(120, -130)
turtle.penup()
turtle.goto(140, -130)
turtle.pendown()
turtle.goto(210, -130)
turtle.penup()
turtle.goto(230, -130)
turtle.pendown()
turtle.goto(300, -130)
turtle.penup()
turtle.goto(320, -130)
turtle.pendown()
turtle.goto(340, -130)

# Draw segmented (dashed) bottom horizontal line
turtle.goto(100, -370)
turtle.goto(120, -370)
turtle.penup()
turtle.goto(140, -370)
turtle.pendown()
turtle.goto(210, -370)
turtle.penup()
turtle.goto(230, -370)
turtle.pendown()
turtle.goto(300, -370)
turtle.penup()
turtle.goto(320, -370)
turtle.pendown()
turtle.goto(340, -370)


# Finish the drawing session
turtle.penup()
turtle.done()
