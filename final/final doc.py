import random
import turtle
import time

print('are you MALE/FEMALE ? (*PLEASE USE CAPITAL LETTERS)')
gender = input('ANSWER:')

turtle.tracer(1, 0)
'''
def menu():
    x = input('would you like to start the game? \n (YES/NO) \n would you like to quit the menu bar? \n (QUIT) \n *PLEASE USE CAPITAL LETTERS \n YOUR ANSWER: ')
    if x == 'NO' or x == 'QUIT':
        quit()
    elif x == 'YES':
##        print('')
menu()
'''


# screen setup + score turtle clone + player
# score 
turtle2 = turtle.clone()
score = 0
turtle2.write(str(score), font=( "Aerial", 24, "normal"))
turtle2.ht()
turtle.penup()

# player
#turtle.shape('circle')
# screen setup

box_color_list = ["box1.gif", "box2.gif", "box3.gif", "box4.gif", "box5.gif"]
background_list = ["background1.gif", "background2.gif", "background3.gif", "background4.gif"]

#screen = turtle.Screen()

randbackground = random.randint (0,len(background_list)-1)
this_background = background_list [randbackground]
turtle.register_shape(this_background)
turtle.bgpic(this_background)

randbox_color= random.randint (0,len(box_color_list)-1)
this_box_color = box_color_list [randbox_color]
turtle.register_shape(this_box_color)
# initial vars
turtle.goto(-5,-270)
good_food=['orange.gif', 'pepper.gif']
bad_food=['icecream.gif', 'cupcake.gif']
good_food_pos= []
bad_food_pos = []
good_food_stamps = []
bad_food_stamps = []
box_stamps = []
box_pos=[]
turtles_list = []
SIZE_X = 690
SIZE_Y = 620
turtle.setup(SIZE_X, SIZE_Y)
player_size = 10
my_pos = turtle.pos()

x_pos = my_pos[0]
y_pos = my_pos[1]
UP_EDGE = 310
DOWN_EDGE = -310
RIGHT_EDGE = 345
LEFT_EDGE = -345


LEFT_ARROW = 'Left'
RIGHT_ARROW = 'Right'
TIME_STEP = 100
TIME_STEP2 = 10000

def distance(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    d = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    return d
    
def move_player():
    global food,score
    my_pos = turtle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    # check boundaries
    x_ok = LEFT_EDGE <= x_pos <= RIGHT_EDGE
    y_ok = UP_EDGE >= y_pos >= DOWN_EDGE
    within_bounds = x_ok and y_ok
    #print(within_bounds)
    if turtle.pos()[0] == RIGHT_EDGE:
        turtle.goto (LEFT_EDGE + 20,turtle.pos()[1])        
    if turtle.pos()[0] == LEFT_EDGE :
        turtle.goto (RIGHT_EDGE - 20,turtle.pos()[1])

    # pseudo bounce back on edges
    if x_pos >= RIGHT_EDGE:
            turtle.goto(RIGHT_EDGE -20, y_pos)
    if x_pos <= LEFT_EDGE:
            turtle.goto(LEFT_EDGE + 20, y_pos)
    

    if turtle.pos()[0] == RIGHT_EDGE:
        turtle.goto(RIGHT_EDGE -10,y_pos)
    if turtle.pos()[0] == LEFT_EDGE:
        turtle.goto(LEFT_EDGE + 10,y_pos)

    # only move if within bounds of game
    if within_bounds: 
        if direction == RIGHT:
            turtle.goto(x_pos + 20,y_pos)
        elif direction == LEFT:
            turtle.goto(x_pos - 20,y_pos)

    for box in turtles_list:
        d = distance(turtle.pos(),box.pos())
        if d < 10:
            quit()     
##next line might be trouble
    global food,score            
    if turtle.pos() in good_food_pos:
        good_food_ind = good_food_pos.index(turtle.pos())
        food.clearstamp(good_food_stamps[good_food_ind])
        good_food_stamps.pop(good_food_ind)
        good_food_pos.pop(good_food_ind)
        print('EATEN GOOD FOOD!')
        score = score + 1
        turtle2.clear()
        turtle2.write(str(score),font=("Arial", 24, "normal"))
        good_food()
        
    if turtle.pos() in bad_food_pos:
        bad_food_ind = bad_food_pos.index(turtle.pos())
        bad_food.clearstamp(bad_food_stamps[bad_food_ind])
        bad_food_stamps.pop(bad_food_ind)
        bad_food_pos.pop(bad_food_ind)
        print('EATEN BAD FOOD!')
        score = score - 1
        turtle2.clear()
        turtle2.write(str(score), font=("Arial", 24, "normal"))
        if score == -5:
            print('GAME OVER!')
            quit()
        bad_food1()
LEFT = 1
RIGHT = 3

direction = 1

#if the code above doesnt work use this
#UP = 0
#LEFT = 1
#DOWN = 2
#RIGHT = 3

#direction = DOWN

turtle.register_shape('man_right.gif')
turtle.register_shape('man_left.gif')
turtle.register_shape('woman_right.gif')
turtle.register_shape('woman_left.gif')


if gender  == "MALE" :
    turtle.shape('man_right.gif')        
else:
    turtle.shape('woman_right.gif')
    
def left():
    global direction
    direction = LEFT
    
    if gender  == "MALE" :
        turtle.shape('man_left.gif')        
    else:
        turtle.shape('woman_left.gif')
        
    move_player()
    print('you pressed the left key')
    
def right():
    global direction
    direction = RIGHT

    if gender  == "MALE" :
        turtle.shape('man_right.gif')        
    else:
        turtle.shape('woman_right.gif')
        
    move_player()
    print('you pressed the right key')

    

turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()
########################################################################


    
good_pos = (0,0) ##
food = turtle.clone()
foodi = random.randint (0, len(good_food)+1)
turtle.register_shape(foodi)
foodi = random.randint (0, len(good_food)+1)
turtle.register_shape(foodi)
this_food = good_list[foodi]
food_stamp = food.stamp()


def good_food():
    #
##    min_x=-int(SIZE_X/2/player_size)+1
##    max_x=int(SIZE_X/2/player_size)-1
##    food_x = random.randint(min_x,max_x)*player_size
    #
    possible_x_vals = [x for x in range(-345, 345+1, 20)]
    rand_i = random.randint(0, len(possible_x_vals) - 1)
    food_x = possible_x_vals[rand_i]
    food.goto(food_x,turtle.pos()[1])
    good_food_pos.append(food.pos())
    stampnew = food.stamp()
    #stamp_old = food_stamps[-1]
    good_food_stamps.append(stampnew)



def create_box():
    global y_pos,box,SIZE_X,player_size 
    top_y = 300
    possible_x_vals = [x for x in range(-345, 345+1, 20)]
    rand_i = random.randint(0, len(possible_x_vals) - 1)
    x = possible_x_vals[rand_i]
    turtles_list.append(turtle.clone())
    turtles_list[-1].hideturtle() 
    turtles_list[-1].shape("square")
    turtles_list[-1].fillcolor('red')
    for i in range(10):
        turtles_list[-1].goto(x,top_y-20)
        turtles_list[-1].showturtle()
        top_y = top_y-20

    '''
    #maybe a problem
    min_x=-int(SIZE_X/2/player_size)+1
    max_x=int(SIZE_X/2/player_size)-1
    x = random.randint(min_x,max_x)*player_size
    
    turtles_list[-1].goto(x,top_y)
    turtles_list[-1].showturtle()
##    chose_number()
    #box.goto(x,y_pos)
    #box.goto(x,260)
    #box.addshape('box.gif')
    #box.shape('box.gif')
    '''
    #all_way = 510
bottom_y = -280
count = 0        
def fall():
     global turtles_list,top_y,x_pos,turtle,count,y_pos,bottom_y
     for my_clone in turtles_list:
         x1 = my_clone.pos()[0]
         y1 =  my_clone.pos()[1]
         if y1 > y_pos:
             y1 = y1 -25
             #x1 = x_pos
             my_clone.goto(x1,y1)
         if bottom_y > my_clone.pos()[1]:
             my_clone.goto(x1,y_pos)
     count += 1
#     print(count)
     if count%100==0:
         num_box = count//100
         for i in range(num_box):
             create_box()

         turtle.ontimer(clear, 5000)


             
         #for num_box in :

     #create_box()
     #turtle.ontimer(create_box,TIME_STEP2)
turtle.ontimer(fall,TIME_STEP)
bad_food = turtle.clone()
bad_food.shape('square')
bad_food.fillcolor('black')
def clear():
    global SIZE_X,player_size,bad_food
    bad_pos = (0,0)
    bad_food.hideturtle()
def bad_food1():
    global SIZE_X,player_size,y_pos,bad_food
      
    y_pos = turtle.pos()[1]
    #
##    min_x=-int(SIZE_X/2/player_size)+1
##    max_x=int(SIZE_X/2/player_size)-1
##    bad_food_x = random.randint(min_x,max_x)*player_size
    #
    possible_x_vals = [x for x in range(-345, 345+1, 20)]
    rand_i = random.randint(0, len(possible_x_vals) - 1)
    bad_food_x = possible_x_vals[rand_i]
    print(bad_food_x)
    bad_food.goto(bad_food_x,y_pos)
    bad_food_pos.append(bad_food.pos())
    bad_stamp_new = bad_food.stamp()
    #stamp_old = food_stamps[-1]
    bad_food_stamps.append(bad_stamp_new)
    for i in turtles_list:
        i.hideturtle()
        i.goto(1000,1000)
my_clone = turtle.clone()
my_clone.ht()
bad_food1()
good_food()
move_player()
create_box()
fall()

turtle.mainloop()

'''
if turtle.pos() == box_pos():
    print("YOU LOST !")
    quit()
'''
