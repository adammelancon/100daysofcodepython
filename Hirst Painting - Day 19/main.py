# import colorgram

# colors = colorgram.extract('image.jpg', 30)
# color_list = []

# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color_list.append((r, g, b)) 

# print(color_list)
#- -------------------------------------------------
# This top colorgram.py code is commented out because I only ran it once
# to be able to grab a color pallet sample from the image.jpg file.

import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
my_screen = Screen()
my_screen.delay(1)
my_screen.screensize(100000, 100000, bg="black")
tim.shape("circle")
tim.speed(0)
my_screen.colormode(255)
tim.color("white")

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

color_list = [(236, 35, 108), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 
46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 
27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182), (180, 187, 211)] 


def dot_machine(spacing, shape_size, rows, columns):
    tim.shapesize(shape_size)
    tim.penup()
    tim.setposition(x=-250, y=-250)
    tim.hideturtle()
    
    for _ in range(rows):
        for x in range(columns):
            tim.color(random.choice(color_list))
            tim.setheading(EAST)
            tim.stamp()
            # tim.write(x)
            tim.forward(spacing)
        tim.backward(columns * spacing)
        tim.setheading(NORTH)
        tim.forward(spacing)
     
dot_machine(50, 1, 10, 10)
my_screen.exitonclick()