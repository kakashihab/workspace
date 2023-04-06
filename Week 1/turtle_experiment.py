#Pyhton has a built in 'turtle'

from turtle import *

reset() #starts at the middle of the screen
speed(0) #0 is fastest speed where 9 is slowest 

#setting up pen and colour
colormode(255)
fill = (20, 50, 35)
pen = (0, 0, 255)

pencolor(pen)
fillcolor(fill)
for j in range(4):
    for i in range(14):
        forward(250)
        right(90)
    forward(30)
    right(30)


end_fill()
done() #stops window from closing

