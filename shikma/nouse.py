import random
import turtle
import time

turtle.tracer(1, 0)
'''
def menu():
    x = input('would you like to start the game? \n (YES/NO) \n would you like to quit the menu bar? \n (QUIT) \n *PLEASE USE CAPITAL LETTERS \n YOUR ANSWER: ')
    if x == 'NO' or x == 'QUIT':
        quit()
    elif x == 'YES':
        print('')
menu()

'''
turtle2 = turtle.clone()
score = 0
turtle2.write(str(score))
turtle2.ht()
turtle.penup()
#bird = turtle.clone()
#turtle.addshape('bird.gif')
#bird.shape('bird.gif')
turtle.shape('circle')
#turtle.hideturtle()
turtle.Screen()
turtle.fillcolor('white')
screen = turtle.Screen()
screen.bgcolor('light blue')

turtle.goto(0,-200)
good_food_pos= []
bad_food_pos = []
good_food_stamps = []
bad_food_stamps = []
box_stamps = []
box_pos=[]
bird_pos=[]
turtles_list = []
SIZE_X = 400
SIZE_Y = 400
turtle.setup(500,500)
player_size = 10
my_pos = turtle.pos()

x_pos = my_pos[0]
y_pos = my_pos[1]
UP_EDGE = 200
DOWN_EDGE = -200
RIGHT_EDGE = 200
LEFT_EDGE = -200


UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
DOWN_ARROW = 'Down'
RIGHT_ARROW = 'Right'
TIME_STEP = 100
TIME_STEP2 = 10000
SPACEBAR = 'space'

    

def move_player():
    my_pos = turtle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    x_ok = LEFT_EDGE <= x_pos <= RIGHT_EDGE
    y_ok = UP_EDGE >= y_pos >= DOWN_EDGE
    within_bounds = x_ok and y_ok

    if x_pos >= RIGHT_EDGE:
            turtle.goto(RIGHT_EDGE - 10, y_pos)
    if x_pos <= LEFT_EDGE:
            turtle.goto(LEFT_EDGE + 10, y_pos)
    if y_pos >= UP_EDGE:
        turtle.goto(x_pos, UP_EDGE + 10)
    
    
        
 
    if within_bounds: 
        if direction == RIGHT:
            turtle.goto(x_pos + 10,y_pos)
        elif direction == LEFT:
            turtle.goto(x_pos - 10,y_pos)
        elif direction == UP:
            turtle.goto(x_pos, y_pos +10)
        global my_clone        
        if turtle.pos == my_clone.pos():
            if direction == UP:
                turtle.goto(x_pos, y_pos +10)

        '''
    else:
        # x checks
        # right edge check
        if x_pos >= RIGHT_EDGE:
            if direction == LEFT:
                turtle.goto(x_pos - 10,y_pos)
        if x_pos <= LEFT_EDGE:
            if direction == RIGHT:
                turtle.goto(x_pos + 10,y_pos)
        if y_pos >= UP_EDGE:
            if direction == RIGHT:
                turtle.goto(x_pos + 10,y_pos)
            elif direction == LEFT:
                turtle.goto(x_pos - 10, y_pos)
            elif direction == DOWN:
                turtle.goto(x_pos, y_pos -10)
            
        if y_pos <= DOWN_EDGE:
            if direction == RIGHT:
                turtle.goto(x_pos + 10,y_pos)
            elif direction == LEFT:
                turtle.goto(x_pos - 10, y_pos)
            elif direction == UP:
                turtle.goto(x_pos, y_pos + 10)
    '''        
    global food,score
    #turtle.ontimer(move_player,TIME_STEP)
    if turtle.pos() in good_food_pos:
        good_food_ind = good_food_pos.index(turtle.pos())
        food.clearstamp(good_food_stamps[good_food_ind])
        good_food_stamps.pop(good_food_ind)
        good_food_pos.pop(good_food_ind)
        print('EATEN GOOD FOOD!')
        score = score + 1
        turtle2.clear()
        turtle2.write(str(score))
        good_food()
    if turtle.pos() in bad_food_pos:
        bad_food_ind = bad_food_pos.index(turtle.pos())
        bad_food.clearstamp(bad_food_stamps[bad_food_ind])
        bad_food_stamps.pop(bad_food_ind)
        bad_food_pos.pop(bad_food_ind)
        print('EATEN BAD FOOD!')
        score = score - 1
        turtle2.clear()
        turtle2.write(str(score))
        if score == -5:
            print('GAME OVER!')
            quit()
        bad_food1()
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = DOWN

    
def up():
    global direction
    direction = UP
    move_player()
    print('you pressed the up key')
    
def down():
    global direction
    direction = DOWN
    move_player()
    print('you pressed the down key')
    
def left():
    global direction
    direction = LEFT
    move_player()
    print('you pressed the left key')
    
def right():
    global direction
    direction = RIGHT
    move_player()
    print('you pressed the right key')

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()
    
good_pos = (0,0)
food = turtle.clone()
food.shape('square')
food.fillcolor('green')
food.hideturtle()

def good_food():
    min_x=-int(SIZE_X/2/player_size)+1
    max_x=int(SIZE_X/2/player_size)-1
    food_x = random.randint(min_x,max_x)*player_size
    food.goto(food_x,turtle.pos()[1])
    good_food_pos.append(food.pos())
    stampnew = food.stamp()
    #stamp_old = food_stamps[-1]
    good_food_stamps.append(stampnew)



def create_box():
    global y_pos,box,SIZE_X,player_size 
    top_y = 300
    min_x=-int(SIZE_X/2/player_size)+1
    max_x=int(SIZE_X/2/player_size)-1
    x = random.randint(min_x,max_x)*player_size
    turtles_list.append(turtle.clone())
    turtles_list[-1].hideturtle() 
    turtles_list[-1].shape("square")
    turtles_list[-1].fillcolor('red')
    turtles_list[-1].goto(x,top_y)
    turtles_list[-1].showturtle()
    #box.goto(x,y_pos)
    #box.goto(x,260)
    #box.addshape('box.gif')
    #box.shape('box.gif')
    
    #all_way = 510
   
        
def fall():
     global turtles_list,top_y,x_pos,turtle
     for my_clone in turtles_list:
         x1 = my_clone.pos()[0]
         y1 =  my_clone.pos()[1]
         if y1 > turtle.pos()[1]:
             y1 = y1 -25
             #x1 = x_pos
             my_clone.goto(x1,y1)    

     #create_box()
     turtle.ontimer(create_box,TIME_STEP2)
     turtle.ontimer(fall,TIME_STEP)


##def jump():
    
    
    
bad_pos = (0,0)
bad_food = turtle.clone()
bad_food.shape('square')
bad_food.fillcolor('black')
bad_food.hideturtle()
def bad_food1():
    global SIZE_X,player_size,y_pos,bad_food
    min_x=-int(SIZE_X/2/player_size)+1
    max_x=int(SIZE_X/2/player_size)-1
    bad_food_x = random.randint(min_x,max_x)*player_size
    bad_food.goto(bad_food_x,y_pos)
    bad_food_pos.append(bad_food.pos())
    bad_stamp_new = bad_food.stamp()
    #stamp_old = food_stamps[-1]
    bad_food_stamps.append(bad_stamp_new)
my_clone = turtle.clone()
my_clone.ht()
bad_food1()
good_food()
move_player()
create_box()
fall()

