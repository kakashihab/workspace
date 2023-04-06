from tkinter import *
import sqlite3

conn = sqlite3.connect('RecordDB.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE if not exists CONTACTS (
    name text, 
    phone integer, 
    email text
    )""")

def newRecordWindow():
    new = Toplevel(wnd)

    name = Label(new, text="Name: ")
    name.grid(row=0, column=0)
    nameBox = Entry(new, width=50, background="white")
    nameBox.grid(row=0, column=1)
    
    phone = Label(new, text="Phone: ")
    phone.grid(row=1, column=0)
    phoneBox = Entry(new, width=50, background="white")
    phoneBox.grid(row=1, column=1)

    email = Label(new, text="Email: ")
    email.grid(row=2, column=0)
    emailBox = Entry(new, width=50, background="white")
    emailBox.grid(row=2, column=1)
    
    addBtn3 = Button(new, text="Add", command=addContact)
    addBtn3.grid(row=2, column=2)

    exitBtn = Button(new, text="Exit", command=destroyWindow)
    exitBtn.grid(row=3,column=2)

def addContact():
    nameBox.delete(0, END)
    phoneBox.delete(0, END)
    emailBox.delete(0, END)


    conn = sqlite3.connect('RecordDB.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO CONTACTS VALUES (:nameBox, :phoneBox, :emailBox)",{'name': nameBox.get(),'phone': phoneBox.get(),'email': emailBox.get()})
    conn.commit()
    conn.close()

    
def searchWindow():
    new = Toplevel(wnd)

    searchTerm = Label(new, text="Search name:")
    searchTerm.grid(row=0, column=0)
    searchBox = Entry(new, width=50, background="white")
    searchBox.grid(row=0, column=1)
    addBtn4 = Button(new, text="search")
    addBtn4.grid(row=0, column=2)

    frameRecords = Frame(new)
    frameRecords.grid(row=1, column=1, padx=20, pady=30)

    #resultsWindow.delete(1.0, END)
    #search = searchName.get()
    #cursor.execute(f"SELECT * FROM contacts WHERE name like ('%{search}%') or phone like ('%{search}) or email like ('%{search}%')")
    #results = cursor.fetchall()
    #for result in results:
    #    resultsWindow.insert(END, f"name: {result[0]}\nphone: {result[1]}\nemail: {result[2]}\n\n")

def destroyWindow():
    wnd.destroy()

wnd = Tk()
wnd.title("Records")

frameNewRecord = Frame()
frameNewRecord.pack()

new = PhotoImage(file="new.gif")
InsertBtn = Button(wnd, text="Insert new record", command=newRecordWindow, image=new, compound="left")
InsertBtn.pack()

search = PhotoImage(file="search.gif")
SearchBtn = Button(wnd, text="Find a record", command=searchWindow, image=search, compound="left")
SearchBtn.pack()

CloseBtn = Button(wnd, text="Close window", command=destroyWindow)
CloseBtn.pack()

conn.commit()
conn.close()
wnd.mainloop()