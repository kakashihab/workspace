from turtle import * 
import random

reset()
speed(0)
ht()

def randomColor():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    fillcolor(r, g, b)
    pencolor(r, g, b)

def square():
    randomColor()
    pendown()
    begin_fill()
    for i in range(1,5): #created square
        forward(200)
        right(90)
    end_fill()
    penup()

colormode(255)
pentuple = (0, 0, 255)
pencolor(pentuple)

for i in range(30):
    left(1)
    for i in range(1):
        pendown()
        square()
        penup()
        right(20)
        forward(50)

done()