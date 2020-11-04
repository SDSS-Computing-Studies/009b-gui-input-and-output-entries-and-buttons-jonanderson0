"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""
import tkinter as tk
from tkinter import *

win = tk.Tk()
win.title("Madlib!")


def start():
  name = f4.get()
  adverb = f5.get()
  noun = f6.get()
  
  f1.delete(0,END)
  f2.delete(0,END)
  f3.delete(0,END)
  f4.delete(0,END)
  f5.delete(0,END)
  f6.delete(0,END)
  f1.insert(0,name)
  f2.insert(0,adverb)
  f3.insert(0,noun)


op1 = StringVar()
op2 = StringVar()
op3 = StringVar()
op4 = StringVar()
op5 = StringVar()
op6 = StringVar()


op1.set("(Enter a name )")
op2.set("(Enter an adverb )")
op3.set("(Enter a noun )")


f4 = tk.Entry(win,textvariable=op4)
f5 = tk.Entry(win,textvariable=op5)
f6 = tk.Entry(win, textvariable=op6)

l4 = tk.Label(win,text="Dear ")
l5 = tk.Label(win,text=",")

l6 = tk.Label(win,text="You are ")

l7 = tk.Label(win,text="invited!")

l8 = tk.Label(win,text="It's time for a ")

l9 = tk.Label(win,text="!")


f1 = tk.Entry(win, width=30, textvariable=op1)

f2 = tk.Entry(win, width=30,textvariable=op2)

f3 = tk.Entry(win, width=30, textvariable=op3)


b1 = tk.Button(win,text="start",command=start)


l4.grid(row=1,column=1)

f1.grid(row=1,column=2)

l5.grid(row=1,column=3)

f4.grid(row=2,column=2)

l6.grid(row=3,column=1)

f2.grid(row=3,column=2)

f5.grid(row=4,column=2)

l7.grid(row=3,column=3)

l8.grid(row=6,column=1)

f3.grid(row=6,column=2)

l9.grid(row=6,column=3)

f6.grid(row=7,column=2)

b1.grid(row=8,column=3)


win.mainloop()
