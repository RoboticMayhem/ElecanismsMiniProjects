from Tkinter import *
import project3

p = project3.project3()

def show_values():
    p.set_vals(x.get(), y.get())
    root.after(100,show_values)

root = Tk()
y = Scale(root, from_=65535, to=0)
y.pack(anchor=CENTER)
x = Scale(root, from_=0, to=65535, orient=HORIZONTAL)
x.pack(anchor=CENTER)
#Button(master, text='Show', command=show_values).pack()

root.after(100,show_values)
root.mainloop()
