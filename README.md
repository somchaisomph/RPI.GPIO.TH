# RPI.GPIO.TH
To collect general GPIO components used with Raspberry Pi created by Thai community.

<h2>Examples</h2>
<h3>LED</h3>
<pre>
from gadgets.led import LED
import time

l = LED(7)
l.on()
time.sleep(2)
l.off()
time.sleep(2)
l.blink(3,1)
l.cleanup()
</pre>
