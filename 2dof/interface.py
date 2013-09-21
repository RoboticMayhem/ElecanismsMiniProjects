import Tkinter as tk
import serial

ser = serial.Serial('/dev/tty.usbFILLIN',19200)

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
        elif event.keysym == 'Right':
            self.right = True
        elif event.keysym == 'Left':
            self.left = True
        elif event.keysym == 'Up':
            self.up = True
        elif event.keysym == 'Down':
            self.down = True

    def keyReleased(self,event):
        if event.keysym == 'Right':
            self.right = False
        elif event.keysym == 'Left':
            self.left = False
        elif event.keysym == 'Up':
            self.up = False
        elif event.keysm == 'Down':
            self.down = False

    def task(self):
        if self.right:
            ser.write(39)
        elif self.left:
            ser.write(37)
        elif self.up:
            ser.write(38)
        elif self.down:
            ser.write(40)
        root.after(20,self.task)

application = App()
root = tk.Tk()
#print( "Press arrow key (Escape key to exit):" )

root.bind_all('<Key>', application.keyPressed)
root.bind_all('<KeyRelease>', application.keyReleased)
root.after(20,application.task)

root.mainloop()