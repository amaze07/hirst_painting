# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('download.jpeg', 10)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
import random
t.colormode(255)

vishi = t.Turtle()
color_list = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181)]

vishi.hideturtle()
vishi.speed("normal")
vishi.penup()
vishi.setheading(225)
vishi.forward(300)
vishi.setheading(0)

for __ in range(10):
    for _ in range(10):
        vishi.dot(20, random.choice(color_list))
        vishi.forward(50)

    vishi.setheading(90)
    vishi.forward(50)
    vishi.setheading(180)
    vishi.forward(500)
    vishi.setheading(0)

screen =  t.Screen()
screen.exitonclick()