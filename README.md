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
