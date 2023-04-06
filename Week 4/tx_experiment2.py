from tkinter import *

def addtopanel():
    s = fld1.get()
    fld1.delete(0, END)
    pnl1.insert(END, s + "\n")

def clearpanel():
    pnl1.delete(1.0, END)

def exitprogram():
    wnd.destroy()

wnd = Tk()
wnd.title("Interactive program")

frame1 = Frame(wnd)
frame1.pack(side="top", padx=20, pady=20)

lbl1 = Label(frame1, text="Type something")
lbl1.pack()

fld1 = Entry(frame1, width=50, background="white")
fld1.pack()

btn1 = Button(frame1, text="Now click here", command= addtopanel)
btn1.pack()

pnl1 = Text(frame1, width=50, background="white")
pnl1.pack()

btn2 = Button(frame1, text="Clear list", command= clearpanel)
btn2.pack()

btn3 = Button(frame1, text="Exit", command= exitprogram)
btn3.pack()
wnd.mainloop()