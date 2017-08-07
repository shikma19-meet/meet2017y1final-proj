import turtle
import random
turtle.tracer(1,0)
turtle.shape("square")
turtle.penup()
turtle.goto(0,200)

boxes_list=[]
number_of_boxes=random.randint(1,3)
for i in range (number_of_boxes):
    x = turtle.clone()
    x.shape("square")
    boxes_list.append(x)
for c in boxes_list:
    c.goto(random.randint(-200,200),200)
turtle.mainloop()
