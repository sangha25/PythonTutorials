
from tkinter import *
from tkinter import ttk

root = Tk()
def bu_press(event):
    print("type:{}".format(event.type))

entry=ttk.Entry(root,width=30)
entry.pack()
button=ttk.Button(root,text="Submit")
button.pack()
button.bind("<ButtonPress>")

def BuClick():
    print(entry.get())
    entry.delete(0,END)


button.config(command=BuClick)


root.mainloop( )