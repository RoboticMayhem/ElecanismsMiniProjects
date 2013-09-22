import Tkinter as tk
import serial

ser = serial.Serial('/dev/ttyUSB0',19200)
print("Communication established")

class App(object):
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def keyPressed(self,event):
        #print "HERE"
        if event.keysym == 'Escape':
            root.destroy()
            print("Press")
        elif event.keysym == 'Right':
            self.right = True
            print("Press")
        elif event.keysym == 'Left':
            self.left = True
            print("Press")
        elif event.keysym == 'Up':
            self.up = True
            print("Press")
        elif event.keysym == 'Down':
            self.down = True
            print("Press")

    def keyReleased(self,event):
        if event.keysym == 'Right':
            self.right = False
            print("Release")
        elif event.keysym == 'Left':
            self.left = False
            print("Release")
        elif event.keysym == 'Up':
            self.up = False
            print("Release")
        elif event.keysym == 'Down':
            self.down = False
            print("Release")

    def task(self):
        if self.right:
            ser.write("d")
            print("Output = ")
            print(ser.read()) 
            print("Right")
        elif self.left:
            ser.write("a")
            print("Output = ")
            print(ser.read())
            print("Left")
        elif self.up:
            ser.write("w")
            print("Output = ")
            print(ser.read())
            print("Up")
        elif self.down:
            ser.write("s")
            print("Output = ")
            print(ser.read())
            print("Down")
        root.after(20,self.task)

application = App()
root = tk.Tk()
#print( "Press arrow key (Escape key to exit):" )

root.bind_all('<Key>', application.keyPressed)
root.bind_all('<KeyRelease>', application.keyReleased)
root.after(20,application.task)

root.mainloop()