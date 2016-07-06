
import signal
import time
from gadgets.joysticks import JoyStick2D

def signal_handler(signal,frame):
	global stop_flag
	stop_flat = True

'''
usedefault values :
'''
joystick = JoyStick2D() #default 

stop_flag = False
while not stop_flag :
	direction = joystick.get_direction()
	left,right,up,down,stop = direction
	print left,right,up,down,stop
