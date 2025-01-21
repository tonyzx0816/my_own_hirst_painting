# import colorgram

# rgb_list = []
# colors = colorgram.extract('hirst_painting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_list.append((r, g, b))
# print(rgb_list)

color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

import turtle as t
import random

t.colormode(255)
tt = t.Turtle()
tt.speed("fastest")
tt.hideturtle()
tt.penup()
tt.setheading(225)
tt.forward(300)
tt.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tt.dot(20, random.choice(color_list))
    tt.forward(50)

    if dot_count % 10 == 0:
        tt.setheading(90)
        tt.forward(50)
        tt.setheading(180)
        tt.forward(500)
        tt.setheading(0)

screen = t.Screen()
screen.exitonclick()