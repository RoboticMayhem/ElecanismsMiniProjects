import time
import project3

class sweep:

	def __init__(self):
		#	Set initial variables
		x = 0;
		delay = 0.01;

	def move(self):
		p = project3.project3()

		for x in range(0,65535,500):
			#	Reset the y to 90 degrees
			y = 32767;

			while (y >= 0):
				p.set_vals(x,y)
				#p.get_dist()
				y = y-100;
		p.set_vals(0,0)
	
	#def stop(self):





