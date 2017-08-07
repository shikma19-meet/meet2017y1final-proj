import turtle
#def MALE():
    
print('are you MALE/FEMALE ? ')
print('*PLEASE USE CAPITAL LETTERS')
gender = input('ANSWER:')
if gender  == "MALE" :
    turtle.addshape('man_right.gif')
    turtle.shape('man_right.gif')

elif gender == "FEMALE" :
    turtle.addshape('woman_right.gif')
    turtle.shape('woman_right.gif')
    
