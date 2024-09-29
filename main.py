import turtle
from turtle import Turtle, Screen
import random

color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203),
              (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107),
              (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78),
              (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]

tim = Turtle()
tim.penup()
tim.setpos(-250, -250)
tim.pendown()
turtle.colormode(255)

for i in range(1, 101):
    tim.color(random.choice(color_list))
    tim.dot(25)
    tim.penup()
    tim.forward(50)
    tim.pendown()
    if i % 10 == 0 and i > 0:
        tim.penup()
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.right(180)
        tim.pendown()

screen = Screen()
screen.exitonclick()
