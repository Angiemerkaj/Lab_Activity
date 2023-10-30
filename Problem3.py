#!/usr/bin/env

#Enxhi Merkaj 10/29/2023

import turtle

# Function to draw and fill a regular polygon
def draw_regular_polygon(sides, length, line_color, fill_color):
    # Create a Turtle object
    polygon = turtle.Turtle()

    # Set the fill color
    polygon.fillcolor(fill_color)

    # Set the pen (line) color
    polygon.pencolor(line_color)

    # Begin filling
    polygon.begin_fill()

    # Draw the polygon
    for _ in range(sides):
        polygon.forward(length)
        polygon.left(360 / sides)

    # End filling
    polygon.end_fill()

    # Close the window on click
    turtle.exitonclick()

# Get user input
sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of the sides: "))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

# Call the function to draw and fill the polygon
draw_regular_polygon(sides, length, line_color, fill_color)
