# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_color=[]
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color = (r, g, b)
#     rgb_color.append(color)
#
# print(rgb_color)
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle.colormode(255)
tim.speed("fastest")
tim.hideturtle()
tim.setheading(310)
tim.penup()
tim.forward(320)
tim.setheading(180)
tim.forward(400)
tim.right(180)


def forward():
    for i in range(10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)
for i in range(10):
    forward()
screen.exitonclick()
