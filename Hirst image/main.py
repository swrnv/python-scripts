# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('Hirst Painting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import turtle
import random

turtle.colormode(255)
coco = turtle.Turtle()
coco.speed("fastest")
coco.penup()
coco.hideturtle()
color_list = [(201, 164, 112), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

coco.setheading(225)
coco.forward(300)
coco.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    coco.dot(20, random.choice(color_list))
    coco.forward(50)

    if dot_count % 10 == 0:
        coco.setheading(90)
        coco.forward(50)
        coco.setheading(180)
        coco.forward(500)
        coco.setheading(0)



screen = turtle.Screen()
screen.exitonclick()

