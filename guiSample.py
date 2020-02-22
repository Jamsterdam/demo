from tkinter import *
from tkinter.ttk import *

win = Tk()

win.title("first GUI")
win.geometry("500x500")

comb = Combobox(win)
comb['values'] = (1, 2, "text")
comb.grid(column=6, row=4)
comb.current(0)

txt = Entry(win, width=10)
txt.grid(column=6, row=5)
txt.focus()

lbl = Label(win, text="yes", font=("Arial", 15))
lbl.grid(column=6, row=7)


def clicked():
    res = "\nwelcome " + txt.get()
    lbl.configure(text="you have input:"+res)


btn = Button(win, text="button1", command=clicked)
btn.grid(column=6, row=6)



win.mainloop()



