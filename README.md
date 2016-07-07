# RPI.GPIO.TH
To collect general GPIO components used with Raspberry Pi created by Thai community.

<h2>Examples</h2>
<h3>LED</h3>
<pre>
from gadgets.led import LED
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
from gadgets.led import PWM_LED
import time

l2 = LED(7) #connect anode to 7th pin on Raspberry Pi
l2.brighten(start=0,end=100,step=1,dur=0.05)
l2.dim(start=100,end=0,step=-1,dur=0.05)
l2.cleanup()
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
