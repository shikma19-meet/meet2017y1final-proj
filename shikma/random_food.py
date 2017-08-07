import turtle
import random
food_list = ['icecream.gif','orange.gif', 'cupcake.gif','pepper.gif']


foodii = turtle.clone()
foodi = random.randint (0, 3)
turtle.register_shape(foodi)
this_food = food_list[foodi]
foodii_stamp = foodii.stamp()

turtle.mainloop()
