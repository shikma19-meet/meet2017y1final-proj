import turtle
import random

#lists
box_color_list = ["box1.gif", "box2.gif", "box3.gif", "box4.gif", "box5.gif"]

randombox = random.randint (0, len(box_color_list)-1)
this_box = box_color_list[randombox]


box = turtle.clone()
turtle.register_shape(this_box)
box.shape(this_box)


turtle.mainloop ()


background = random.randint (0,4)
screen = turtle.Screen()

####

background_list = ["background1.gif", "background2.gif", "background3.gif", "background4.gif"]
randbackground = random.randint (0,len(background_list)-1)
this_background = background_list [randbackground]

background = turtle.addshape(this_background)
screen = turtle.Screen()
turtle

turtle.mainloop ()

