#!/usr/bin/env python3

# Exercise 19: Hit the Target with Hints

import turtle

# Named Constants

# Screen parameters
SCREEN_WIDTH = 600      # Screen width
SCREEN_HEIGHT = 600     # Screen height

# Target parameters
TARGET_LLEFT_X = 100    # Target bottom_left X coordinate
TARGET_LLEFT_Y = 250    # Target bottom_left Y coordinate
TARGET_WIDTH = 25       # Target width

# Physics and animation
FORCE_FACTOR = 30       # Arbitary force factor
PROJECTILE_SPEED = 1    # Projectile animation speed

# Directions (in degrees)
NORTH = 90              # North direction angle
SOUTH = 270             # South direction angle
EAST = 0                # East direction angle
WEST = 180              # West direction angle

# Set window size
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Draw a target
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Centering the turtle
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle of the shot and the power from the user
angle = float(input("Enter the angle of the projectile shot: "))
force = float(input("Enter the starting force (1 - 10): "))

# Calculate the distance
distance = force * FORCE_FACTOR

# Set direction
turtle.setheading(angle)

# Launch a projectile
turtle.pendown()
turtle.forward(distance)


# Did the projectile hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print("The target is hit!")
else:
    print("You missed")

    # Hint for the Angle
    # Based on coordinates (100, 250), the ideal angle is approximately 68-70 degrees
    if angle < 68:
        print("Try a greater angle.")
    elif angle > 72:
        print("Try a smaller angle.")
    
    # Hint for the Force
    # Distance to target is roughly 270, so ideal force is around 9 (9 * 30 = 270)
    if force < 9:
        print("Use more force.")
    elif force > 10:
        print("Use less force.")

# Leave the window open
turtle.done()
