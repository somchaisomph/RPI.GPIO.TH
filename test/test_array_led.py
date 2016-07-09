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
