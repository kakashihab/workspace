from tkinter import *
import sqlite3


def newRecordWindow():
    new = Toplevel(wnd)

    name = Label(new, text="Name: ")
    name.grid(row=0, column=0)
    nameBox = Entry(new, width=50, background="white")
    nameBox.grid(row=0, column=1)
    addBtn = Button(new, text="Add")
    addBtn.grid(row=0, column=2)
    
    phone = Label(new, text="Phone: ")
    phone.grid(row=1, column=0)
    phoneBox = Entry(new, width=50, background="white")
    phoneBox.grid(row=1, column=1)
    addBtn2 = Button(new, text="Add")
    addBtn2.grid(row=1, column=2)

    email = Label(new, text="Email: ")
    email.grid(row=2, column=0)
    emailBox = Entry(new, width=50, background="white")
    emailBox.grid(row=2, column=1)
    addBtn3 = Button(new, text="Add")
    addBtn3.grid(row=2, column=2)

    exitBtn = Button(new, text="Exit", command=destroyWindow)
    exitBtn.grid(row=3,column=2)
    
def searchWindow():
    new = Toplevel(wnd)
    frameRec = Frame(wnd)

    searchTerm = Label(new, text="Search name: ")
    searchTerm.grid(row=0, column=0)
    searchBox = Entry(new, width=50, background="white")
    searchBox.grid(row=0, column=1)


    

def destroyWindow():
    wnd.destroy()

wnd = Tk()
wnd.title("Records")

frameNewRecord = Frame()
frameNewRecord.pack()

InsertBtn = Button(wnd, text="Insert new record", command=newRecordWindow)
InsertBtn.pack()

SearchBtn = Button(wnd, text="Find a record", command=searchWindow)
SearchBtn.pack()

CloseBtn = Button(wnd, text="Close window", command=destroyWindow)
CloseBtn.pack()

wnd.mainloop()