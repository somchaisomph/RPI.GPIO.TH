# RPI.GPIO.TH
To collect general GPIO components used with Raspberry Pi created by Thai community.
This project is subject to change anytime, please come to see frequently.
<h2>Installation</h2>
<h3>Python SpiDev</h3>
<pre>
$ git clone https://github.com/doceme/py-spidev.git
$ cd py-spidev
$ sudo python setup.py install
</pre>
<h3>One-Wire</h3>
<ol>
<li>
Add these lines at the bottom of /etc/modules 
<pre>
w1-gpio
w1-therm
</pre>
</li>
<li>
Add this line at the bottom of /boot/config.txt
<pre>
dtoverlay=w1-gpio-pullup,gpiopin=XX
</pre>
Where XX is GPIO to be connected to sensor.
</li>
</ol>
<h3>I2C </h3>
<ol>
<li>
Enable Raspbian I2C interface as mensioned in <a href='https://www.raspberrypi.org/documentation/configuration/raspi-config.md'>https://www.raspberrypi.org/documentation/configuration/raspi-config.md</a> 
</li>

<li> Install python interface :
<pre>
$ sudo apt-get install i2ctools
$ sudo apt-get install python-smbus python3-smbus
</pre>

</li>
</ol>
<hr />
<h2>Examples</h2>
<h3>LED</h3>
<pre>
from gadgets.lights.led import LED
import time

l = LED(7) #connect anode to 7th pin on Raspberry Pi
l.on() # turn led on
time.sleep(2)
l.off() # turn led off
time.sleep(2)
l.blink(3,1) # blink led 3 times with 1 second interval.
l.cleanup()
</pre>
<h3>PWM LED</h3>
<pre>
from gadgets.lights.led import PWM_LED
import time

l2 = LED(7) #connect anode to 7th pin on Raspberry Pi
l2.brighten(start=0,end=100,step=1,dur=0.05)
l2.dim(start=100,end=0,step=-1,dur=0.05)
l2.cleanup()
</pre>
<h3>ARRAY LED (Blinker)</h3>
<pre>
from gadgets.lights.led import ARRAY_LED
import time

def lighting(l):
	for j in range(2):
		for i in ps:
			l.blink([i],1,0.1)
		for k in ps_rev:
			l.blink([k],1,0.1)	
	for j in range(3):		
		l.blink(ps,3,0.1)
		time.sleep(0.5)

ps = [29,31,33,35,37]
ps_rev = ps[::-1] # reverse list
l = ARRAY_LED(ps)
for i in range(10):
	lighting(l)
l.cleanup()
</pre>
<hr />
<h3>2D SPI JoyStick</h3>
<pre>
import signal
import time
from gadgets.joysticks import JoyStick2D

def signal_handler(signal,frame):
	global stop_flag
	stop_flat = True

joystick = JoyStick2D() #default 

stop_flag = False
while not stop_flag :
	direction = joystick.get_direction()
	left,right,up,down,stop = direction
	print left,right,up,down,stop
</pre>
<hr />
<h3>Step Motor</h3>
<h4>Normal Step</h4>
<pre>
from gadgets.motors.step_motor import Model_28BYJ_48
from gadgets.joysticks import JoyStick2D

st_mot = Model_28BYJ_48([11,15,16,18])
#change directions and step-sequences
print("Clockwise with 4 step-sequences.")
st_mot.step(1,direction=2,waiting_time=2) 
time.sleep(2)

print("Clockwise with 8 step-sequences.")
st_mot.step(1,direction=1,waiting_time=2) 
time.sleep(2)

print("Counter Clockwise with 4 step-sequences.")
st_mot.step(1,direction=-1,waiting_time=2) 
time.sleep(2)

print("Counter Clockwise with 8 step-sequences.")
st_mot.step(1,direction=-2,waiting_time=2) 
time.sleep(2)

#change speed by changing waiting time

for sp in range(2,5):
	print("Waiting = ",str(sp))
	st_mot.step(1,direction=2,waiting_time=sp) 
	time.sleep(2)

</pre>

<h4>Sweeper</h4>
<p>1 step motor</p>
<pre>
from gadgets.motors.step_motor import Model_28BYJ_48
st_mot = Model_28BYJ_48([11,15,16,18])
for i in range(5):
	st_mot.angular_step(180,direction=2,waiting_time=2,bi_direction=True) 	
</pre>
<p>2 step motors</p>
<pre>
from gadgets.motors.step_motor import Model_28BYJ_48
import threading

st_mot = Model_28BYJ_48([11,15,16,18])
st_mot2 = Model_28BYJ_48([31,33,35,37])

def do1():
	for i in range(5):
		st_mot.angular_step(180,direction=2,waiting_time=2,bi_direction=True) 	

def do2():
	st_mot2.step(4,direction=2,waiting_time=2) 

t1 = threading.Thread(target=do1)
t2 = threading.Thread(target=do2)
t1.start()
t2.start()	
</pre>
<h4>Servo 5V</h4>
<pre>
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
</pre>
<hr/>
<h3>Weather</h3>
<h4>Temperatur sensor DS18B20</h4>
<pre>
from gadgets.weather.DS18B20 import DS18B20 
import time

_id = '28-0000066a6165' # replace it with your own id

sensor = DS18B20(_id,2) # create DS18B20 instance with 2 seconds time interval.

try:
	sensor.start() #activate sensor
	while True :
		print(sensor.C) # show temperature in Celsius. Use sensor.F for Fahrenheit.
		time.sleep(2) # take a break
	
except KeyboardInterrupt:
	print("Stoping")
	
finally:	
	sensor.stop() # Tell sensor to stop reading.
	sensor.join() # Wait util sensor complete its job.
	
</pre>
<hr/>
<h3>Navigators</h3>
<h4>GYRO GY61</h4>
<pre>
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
	
</pre>
<hr/>
<h3>Environment</h3>
<h4>PIR</h4>
<pre>
from gadgets.environment.motion import PIR

if __name__ == "__main__":
	try :
		pir = PIR(pin_number=11,interval=10) 
		# PIR connected to Pin 11 of Raspi with 10 millisecond interval of detection
		pir.start()
		print('Ctrl-c to exit.')
		while 1 :
			print(pir.result()) # 1 : motion detected, 0: no motion detected
	except KeyboardInterrupt :	
		pir.stop()
		pir.cleanup()
</pre>
