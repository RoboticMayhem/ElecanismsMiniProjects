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
        self.enter = False
        self.r = False

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
        elif event.keysym == 'Enter':
            self.enter = True
            print("Press")
        elif event.keysym == 'r':
            self.r = True
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
        elif event.keysym == 'Enter':
            self.enter = False
            print("Release")
        elif event.keysym == 'r':
            self.r = False
            print("Release")

    def task(self):
        if self.right:
            ser.write("d\r\n")
            print("Output = Right")
        elif self.left:
            ser.write("a\r\n")
            print("Output = Left")
        elif self.up:
            ser.write("w\r\n")
            print("Output = Up")
        elif self.down:
            ser.write("s\r\n")
            print("Output = Down")
        elif self.r:
            ser.write("r\r\n")
            print("Reset")
        root.after(20,self.task)

application = App()
root = tk.Tk()
#print( "Press arrow key (Escape key to exit):" )

root.bind_all('<Key>', application.keyPressed)
root.bind_all('<KeyRelease>', application.keyReleased)
root.after(20,application.task)

root.mainloop()