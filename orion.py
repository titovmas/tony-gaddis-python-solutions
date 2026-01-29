#!/usr/bin/env python3


import turtle

# Set window size
turtle.setup(500, 600)
turtle.bgcolor('black')
turtle.pencolor('white')

# Install turtle
turtle.penup()
turtle.speed(1)
turtle.hideturtle()

# Create named constants for star coordinates
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Apply stars
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)       # Left shoulder
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)     # Right shoulder
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)       # Left beltstar
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)   # Middle beltstar
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)     # Right beltstar
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)               # Left knee
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)             # Right knee
turtle.dot()

# Display the names of the stars
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)       # Left shoulder
turtle.write("Betelgeuse")
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)     # Right shoulder
turtle.write("Bellatrix")
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)       # Left beltstar
turtle.write("Alnitak")
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)   # Middle beltstar
turtle.write("Alnilam")
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)     # Right beltstar
turtle.write("Mintaka")
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)               # Left knee
turtle.write("Saiph")
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)             # Right knee
turtle.write("Rigel")

# Draw a line from the left shoulder to the left star of the belt
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

# Draw a line from the right shoulder to the right star of the belt
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# Draw a line from the left star of the belt to the middle star of the belt
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

# Draw a line from middle star of the belt to the right star of the belt
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# Draw a line from the left star of the belt to the left knee
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

# Draw a line from the right star of the belt to the right knee
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.penup()


# Leave the window open
turtle.done()
