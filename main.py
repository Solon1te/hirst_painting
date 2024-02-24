# import colorgram
#
# colors = colorgram.extract("image.jpg", 88)
# colors_a = []
#
# for color in colors:
#     rgb_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     colors_a.append(rgb_tuple)
#
# print(colors_a)

import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)
tim.speed("fastest")
tim.hideturtle()


color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71),
              (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (244, 39, 149), (65, 202, 229), (14, 205, 222),
              (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9),
              (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 212),
              (86, 77, 208), (86, 225, 235), (250, 8, 14), (242, 166, 157), (177, 180, 224), (36, 243, 159),
              (6, 81, 115), (11, 55, 248)]
tim.pu()
tim.setx(-250)
tim.sety(-225)


# pick a color and creates a circle on the canvas
def create_circle():
    tim.color(random.choice(color_list))
    tim.begin_fill()
    tim.dot(20)
    tim.end_fill()


# moves the turtle forward in the x direction 50 paces
def move_to_x():
    current_x_location = tim.xcor()
    tim.setx(current_x_location + 50)


# creates 10 circles in the specified x plane
def create_x_circles():
    for _ in range(10):
        create_circle()
        move_to_x()


# moves the turtle to a new y plane and resets the x position back to "start"
def move_to_y():
    current_y_location = tim.ycor()
    tim.sety(current_y_location + 50)
    tim.setx(-250)


for _ in range(10):
    create_x_circles()
    move_to_y()


screen.exitonclick()
