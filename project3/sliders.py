#	Change log
#	Need to add a button for reset
#	Need to add a button for sweep
#	Need to add a button for ultrasonic transmit

from Tkinter import *
import project3
import sweep

p = project3.project3()
s = sweep.sweep()

def spin_servo():
    p.set_vals(x.get(), y.get())
    root.after(100,spin_servo)

root = Tk()
y = Scale(root, from_=65535, to=0)
y.pack(anchor=CENTER)
x = Scale(root, from_=0, to=65535, orient=HORIZONTAL)
x.pack(anchor=CENTER)
Button(root, text='Sweep', command=s.move).pack()
#Button(root, text = 'Stop Sweep',command=s.stop).pack()

root.after(100,spin_servo)
root.mainloop()
