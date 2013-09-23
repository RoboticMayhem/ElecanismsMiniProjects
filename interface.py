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
        self.t = False

    def keyPressed(self,event):
        if event.keysym == 'Escape':
            root.destroy()
        elif event.keysym == 'Right':
            self.right = True
        elif event.keysym == 'Left':
            self.left = True
        elif event.keysym == 'Up':
            self.up = True
        elif event.keysym == 'Down':
            self.down = True
        elif event.keysym == 'Enter':
            self.enter = True
        elif event.keysym == 'r':
            self.r = True
        elif event.keysym == 't':
            self.t = True

    def keyReleased(self,event):
        if event.keysym == 'Right':
            self.right = False
        elif event.keysym == 'Left':
            self.left = False
        elif event.keysym == 'Up':
            self.up = False
        elif event.keysym == 'Down':
            self.down = False
        elif event.keysym == 'Enter':
            self.enter = False
        elif event.keysym == 'r':
            self.r = False
        elif event.keysym == 't':
            self.t = False

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
        elif self.t:
            ser.write("t\r\n")
            print("Trigger Ultrasonic Burst")

        root.after(20,self.task)

application = App()
root = tk.Tk()
#print( "Press arrow key (Escape key to exit):" )

root.bind_all('<Key>', application.keyPressed)
root.bind_all('<KeyRelease>', application.keyReleased)
root.after(20,application.task)

root.mainloop()