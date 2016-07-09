from gadgets..lights.led import LED
import time

l = LED(7) #connect led to pin number 7
l.on()
time.sleep(2)
l.off()
time.sleep(2)
l.blink(3,1)
l.cleanup()
