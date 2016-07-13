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
Download gadgets and spi folders and place somewhere on your Raspberry Pi.
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
<hr/>
<h3>Weather</h3>
<h4>Temperatur sensor DS18B20</h4>
<pre>
from gadgets.weather.DS18B20 import DS18B20 
import time

_id = '28-0000066a6165' # change it to be your own id

sensor = DS18B20(_id,2)

try:
	sensor.start()
	while True :
		print(sensor.C)
		time.sleep(2)
	
except KeyboardInterrupt:
	print("Stoping")
	
finally:	
	sensor.stop()
	sensor.join()
	
</pre>
