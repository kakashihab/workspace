from tkinter import *
from playsound import playsound

def cows():
    playsound("Week 4\cow.mp3")

def roosters():
    playsound("Week 4\rooster.mp3")

def sheeps():
    playsound("Week 4\sheep.mp3")

def chickens():
    playsound("Week 4\chicken.mp3")

wnd = Tk()

wnd.title("Farm soundboard")

chicken = PhotoImage(file="Week 4\chickenpic.gif")
cow = PhotoImage(file="Week 4\cowpic.gif")
sheep = PhotoImage(file="Week 4\sheeppic.gif")
rooster = PhotoImage(file="Week 4\roosterpic.gif")

frame1 = Frame(wnd)
frame1.pack()

btn1 = Button(frame1, command=chickens, image=chicken) #compoun=BOTTOM will add text next to pic
btn1.grid(row=0, column=0, sticky='n')

btn2 = Button(frame1, command=cows ,image=cow)
btn2.grid(row=1, column=0, sticky='n')

btn3 = Button(frame1, command=sheeps, image=sheep)
btn3.grid(row=0, column=1, sticky='n')

btn4 = Button(frame1, command=roosters, image=rooster)
btn4.grid(row=1, column=1, sticky='n')

wnd.mainloop()
