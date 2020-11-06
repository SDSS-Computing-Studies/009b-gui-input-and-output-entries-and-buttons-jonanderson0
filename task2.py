"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk
from tkinter import * 
import math 




win = tk.Tk()




b = StringVar()
b.set("Answer")


def f():
    b = e1.get()
    b = float(b)
    c = e2.get()
    c = float(c)
    d1 = float((b**2)- (4*c))
    d1 = math.sqrt(d1)
    d1 = (-1*b)+d1
    d1 = d1/2
    d2 = float((b**2)- (4*c))
    d2 = math.sqrt(d2)
    d2 = (-1*b)-d2
    d2 = d2/2
    equation = []
    equation.append(d1)
    equation.append(d2)
    after.delete(0,END)
    after.insert(0,equation)


l1 = Label(win,text="fill in the coefficents for b and c")
l2 = Label(win,text='click the "=" button and your factored equation will appear')
l3 = Label(win,text="*note: a is equal to 1*")
l4 = Label(win,text="")
l5 = Label(win,text="x^2")
l6 = Label(win,text="+")
e1 = Entry(win,width=5)
l7 = Label(win,text="x")
l8 = Label(win,text="+")
e2 = Entry(win,width=5)
b1 = Button(win,text="=",command=f)
after = Entry(win,width=20,textvariable=b)

l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
l3.grid(row=4,column=1)
l5.grid(row=5,column=1,sticky = E)
l6.grid(row=5,column=2)
e1.grid(row=5,column=3)
l7.grid(row=5,column=4)
e2.grid(row=5,column=6)
l8.grid(row=5,column=5)
b1.grid(row=5,column=7)
after.grid(row=5,column=8)

win.mainloop()
