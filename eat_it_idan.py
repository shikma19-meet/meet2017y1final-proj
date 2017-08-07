import random
import turtle

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
food_stamps = []
box_pos=[]
bird_pos=[]
SIZE_X = 400
SIZE_Y = 400
turtle.setup(500,500)
player_size = 100
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
 
    if within_bounds: 
        if direction == RIGHT:
            turtle.goto(x_pos + 10,y_pos)
        elif direction == LEFT:
            turtle.goto(x_pos - 10,y_pos)
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
    global food    
    #turtle.ontimer(move_player,TIME_STEP)
    if turtle.pos() in good_food_pos:
        good_food_ind = good_food_pos.index(turtle.pos())
        food.clearstamp(food_stamps[good_food_ind])
        food_stamps.pop(good_food_ind)
        good_food_pos.pop(good_food_ind)
        good_food()

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

    
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
food.fillcolor('yellow')
food.hideturtle()

def good_food():
    global good_pos, food
    min_x=-int(SIZE_X/2/player_size)+1
    max_x=int(SIZE_X/2/player_size)-1
    food_x = random.randint(min_x,max_x)*player_size
    food.goto(food_x,turtle.pos()[1])
    good_food_pos.append(food.pos())
    stampnew = food.stamp()
    #stamp_old = food_stamps[-1]
    food_stamps.append(stampnew)  

def box():
    global y_pos
    box = turtle.clone()    
    x = random.randint(1,20)
    box.goto(x,y_pos)
    #box.addshape('box.gif')
    #box.shape('box.gif')
    box.shape('square')
    box.fillcolor('green')
    box1 = 20
    gravity()
    x_box = box.pos()[0]
    y_box = box.pos()[1]

def gravity():
    global my_pos,x_box,y_box,y_pos,x_pos
    if x_pos == x_box:
        turtle.goto(x_box,y_box)
    
'''
def bad_food():
    food = turtle.clone()
    food.shape('square')
    food.fillcolor('black')
    min_x=-int(SIZE_X/2/player_size)+1
    max_x=int(SIZE_X/2/player_size)-1
    min_y=-int(SIZE_Y/2/player_size)+1
    max_y=int(SIZE_Y/2/player_size)-1
    food_x = random.randint(min_x,max_x)*player_size
    food_y = random.randint(min_y,max_y)*player_size
    food.goto(food_x,food_y)
    good_food_pos.append(food.pos())
    stampnew = food.stamp()
    food_stamps.append(stampnew)
'''
good_food()
move_player()
box()
gravity()
