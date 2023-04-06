from turtle import *

reset()
speed(0)

def square():
    fillcolor(0, 255, 0)
    pendown()
    begin_fill()
    for i in range(1,5):
        forward(200)
        right(90)
    end_fill()
    penup()

colormode(255)
pentuple = (0, 0, 255)
pencolor(pentuple)

for i in range(1, 5):
    pendown()
    circle(radius = 150, steps = 6)
    penup()
    right(45)
    forward(50)
    left(45)

done()