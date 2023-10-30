#!/usr/bin/env

#Enxhi Merkaj 10/29/2023


import turtle
import random

# Create a Turtle object
spiral = turtle.Turtle()

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")  # Set the background color to black

# Function to draw a colorful spiral
def draw_colorful_spiral():
    for _ in range(72):  # Create 72 segments for a full spiral
        spiral.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        spiral.forward(100)  # Move forward
        spiral.right(45)  # Turn right

# Set initial position and angle
spiral.penup()
spiral.goto(0, 0)
spiral.pendown()
spiral.speed(10)  # Increase the drawing speed

# Draw the colorful spiral
draw_colorful_spiral()

# Hide the turtle
spiral.hideturtle()

# Close the window on click
wn.exitonclick()
