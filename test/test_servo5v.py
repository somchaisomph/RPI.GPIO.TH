from gadgets.motors.servos import Servo5V
import time
import random

servo = Servo5V(pin_number=12,freq=100)
count = 0
while count < 185:
	time.sleep(0.1)
	servo.write(count)
	count += 5
servo.cleanup()	
	
