from tkinter import *
import re

def validatepostcode():
    s = fld1.get()
    if s:
        fld1.delete(0, END)

        if cs.get() == 0:
            s = s.upper()

        regex = "[A-Z]{1,2}[0-9]{1,2}[A-Z]{0,1} [0-9][A-Z]{2}"
        if re.fullmatch(regex, s):
            pnl1.insert(1.0, s + "\t\tis valid\n")
        else:
            pnl1.insert(1.0, s + "\t\tis not valid\n")


def clearpanel():
    pnl1.delete(1.0, END)


def closeprogram():
    wnd.destroy()
    exit()

# create a Tkinter object
wnd = Tk()
wnd.title("Postcode validator")
cs = IntVar()

# create the widgets for the form
frame1 = Frame(wnd)
frame1.pack(side="top", padx=15, pady=15)
lbl1 = Label(frame1, text="Enter a postcode")
fld1 = Entry(frame1, width=50, background="white")
chk1 = Checkbutton(frame1, text="Case sensitive?", variable=cs, onvalue=1, offvalue=0)
btn1 = Button(frame1, text="Click to validate", command=validatepostcode)
pnl1 = Text(frame1, width=50, background="white")

widgets = [lbl1, fld1, chk1, btn1, pnl1]
for widget in widgets:
    widget.pack(pady=10)

frame2 = Frame(wnd)
frame2.pack(side="top", padx=15, pady=15)
btn2 = Button(frame2, text="Clear", command=clearpanel)
btn3 = Button(frame2, text="Exit", command=closeprogram)

for widget in btn2, btn3:
    widget.pack(side="left", padx=15)

# start the main loop
wnd.mainloop()