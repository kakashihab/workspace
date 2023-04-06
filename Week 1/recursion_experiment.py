from turtle import *
import random 

#def f(n):
#    if n > 0:
#        print(f"The number is {n}")
#        f(n - 1)

#f(5)

def rf(n):
    if n > 0:
        print(f"hello {n}")
        rf(n - 1)
    else:
        print("The end")

        
rf(99)

###Draws multiple squares
#def recursivesquare(n):
 #   if n > 0:
  #      for i in range(4):
   #         forward(100 + n * 10)
    #        right(90)
    #    penup()
    #    right(45)
#        forward(20)
#        left(45)
#        pendown()

#        recursivesquare(n - 1)
# reset()
# speed(0)

# recursivesquare(20)
# exitonclick()

def tree(n):
    if n > 10:
        pencolor(165, 42, 42)
        width(n / 20)
        forward(n)
        left(60)
        tree(n * 0.4) 
        right(120)
        tree(n * 0.6)
        left(60)
        fillcolor(67, 117, 43)
        begin_fill()
        pencolor(67, 117, 43)
        circle(radius = random.randint(1, 30))
        end_fill()
        back(n)
reset()
speed(0)
penup()
goto(0, -300)
left(90)
pendown()
colormode(255)
pentuple = (110, 57, 42)
pencolor(pentuple)


tree(200)
exitonclick()
