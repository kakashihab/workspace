from tkinter import *
from playsound import playsound

def hello():
    if lbl1["text"] == "Hello":
        lbl1["text"] = "Goodbye"
        lbl1["image"] = circlesquare
        playsound("cow.mp3")
    else:
        lbl1["text"] = "Hello"
        lbl1["image"] = circle
        playsound("rooster.mp3")

wnd = Tk()

wnd.title("Hello World")

circle = PhotoImage(file="circle.gif")
circlesquare = PhotoImage(file="circlesquare.gif")
switch = PhotoImage(file="switch.gif")

frame1 = Frame(wnd)
frame1.pack(side="top", padx=20, pady=20)

lbl1 = Label(frame1, text="Hello this is a label", background="green", image = circle)
lbl1.pack(side= "left")

btn1 = Button(frame1, text="Click me", command=hello, image=switch)
btn1.pack(side="left")

wnd.mainloop()



