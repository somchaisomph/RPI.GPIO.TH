from gadgets.navigators.gyro import GYRO_GY61
import signal
import time


def signal_handler(signal,frame):
	global stop_flag
	stop_flat = True
	
gyro = GYRO_GY61(0,0,1,2)

stop_flag = False
while not stop_flag :
	direction = gyro.get_data()
	x,y,z = direction
	print x,y,z
