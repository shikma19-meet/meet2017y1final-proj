import turtle
import random

#lists
box_color_list = ["box1.gif", "box2.gif", "box3.gif", "box4.gif", "box5.gif"]
background_list = ["background1.gif", "background2.gif", "background3.gif", "background4.gif"]

randombox = random.randint (0, len(box_color_list)-1)
this_box = box_color_list[randombox]


box = turtle.clone()
turtle.register_shape(this_box)
box.shape(this_box)


background = random.randint (0,4)
screen = turtle.Screen()



randbackground = random.randint (0,len(background_list)-1)
this_background = background_list [randbackground]
turtle.register_shape(this_background)
turtle.bgpic (this_background)


gabi = turtle.clone()
gabi.penup()
gabi.goto(0,-290)
gabi.pendown()
gabi.goto(0,285)
gabi.penup()
gabi.goto(350,0)
gabi.pendown()
gabi.goto(-340,0)
