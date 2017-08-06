import random
import turtle

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
turtle.setup(400,400)
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


UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

    
def up():
    global direction
    direction = UP
    print('you pressed the up key')
    
def down():
        global direction
        direction = DOWN
        print('you pressed the down key')
    
def left():
        global direction
        direction = LEFT
        print('you pressed the left key')
    
def right():
    global direction
    direction = RIGHT
    print('you pressed the right key')

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()
    
good_pos = (0,0)

def good_food():
    global good_pos
    food = turtle.clone()
    good_pos = food.pos()
    food.shape('square')
    food.fillcolor('yellow')
    min_x=-int(SIZE_X/2/player_size)+1
    max_x=int(SIZE_X/2/player_size)-1
    min_y=-int(SIZE_Y/2/player_size)+1
    max_y=int(SIZE_Y/2/player_size)-1
    food_x = random.randint(min_x,max_x)*player_size
    food_y = random.randint(min_y,max_y)*player_size
    food.goto(food_x,food_y)
    good_food_pos.append(food.pos())


def eat_food():
    stampnew = food.stamp()
    stamp_old = food_stamps[-1]
    food_stamps.append(stampnew)
    food_stamps.append(stampnew)
    food.clearstamp(stamp_old)  
    if my_pos == good_pos:
        food_stamps.clearstamp[-1]
        
def move_player():
    my_pos = turtle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if x_pos == RIGHT_EDGE:
        turtle.goto(RIGHT_EDGE - 10,y_pos)
    if x_pos == LEFT_EDGE:
        turtle.goto(LEFT_EDGE + 10,y_pos)
    if y_pos == UP_EDGE:
        turtle.goto(UP_EDGE - 10,x_pos)
    if y_pos == DOWN_EDGE:
        turtle.goto(DOWN_EDGE + 10,x_pos)
        
    if direction == RIGHT:
        turtle.goto(x_pos + 10,y_pos)
    elif direction == LEFT:
        turtle.goto(x_pos - 10,y_pos)
    elif direction == UP:
        turtle.goto(x_pos, y_pos + 10)
    elif direction == DOWN:
        turtle.goto(x_pos, y_pos -10)
    turtle.ontimer(move_player,TIME_STEP)

def box():
    box = turtle.clone()    
    x = random.randint(1,20)
    box.goto(0,x)
    #box.addshape('box.gif')
    #box.shape('box.gif')
    box.shape('square')
    box.fillcolor('green')
    box1 = 20
    

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
eat_food
