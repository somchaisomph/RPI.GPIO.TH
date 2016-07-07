from gadgets.led import PWM_LED
import time


led = PWM_LED(7,freq=100)

led.brighten(start=0,end=100,step=1,dur=0.05)
time.sleep(1)
led.dim(start=100,end=0,step=-1,dur=0.05)
time.sleep(1)
led.cleanup()
