from Tkinter import *
import serial

ser = serial.Serial('/dev/ttyUSB0',19200)
print("Communication established")
def show_values():
    print (x.get(), y.get())
    ser.write(FILL_THIS_IN)
    root.after(100,show_values)

root = Tk()
y = Scale(root, from_=65535, to=0)
y.pack(anchor=CENTER)
x = Scale(root, from_=0, to=65535, orient=HORIZONTAL)
x.pack(anchor=CENTER)
#Button(master, text='Show', command=show_values).pack()

root.after(100,show_values)
root.mainloop()
