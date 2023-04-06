from tkinter import *

def closeme(new):
    new.destroy()

def child1():
    new = Toplevel(wnd)

    lbl1 = Label(new, text="Hello from child 1")
    lbl1.pack()

    btn3 = Button(new, text="Click me", command=lambda: closeme(new))
    btn3.pack()

    new.focus_set()
    new.grab_set()

def child2():
    pass
wnd = Tk()
wnd.title("Parent Window")

btn1 = Button(wnd, text = "Child 1", command=child1)
btn1.pack()

btn2 = Button(wnd, text = "Child 2", command=child2)
btn2.pack()


wnd.mainloop()