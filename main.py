import turtle as turtle_module
import random

t = turtle_module.Turtle()
screen = turtle_module.Screen()

turtle_module.colormode(255)
color_list = [(202, 166, 109), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]
t.setheading(225)
t.penup()
t.hideturtle()
t.forward(300)
t.setheading(0)


for dot in range(1, 101):
    t.dot(16, random.choice(color_list))
    t.forward(50)
    if (dot % 10) == 0:
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(500)
        t.setheading(0)


screen.exitonclick()