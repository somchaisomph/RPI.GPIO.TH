from gadgets.th_gpio import TH_GPIO
import time 

class LED():
	def __init__(self,pin_number=7):
		self.pin_number = gpio_number
		#A singleton class is treated like a function
		TH_GPIO().enable_pin(self.pin_number,mode='out')
		self.status = 0 #0:off,1:on
    
	def on(self):
		self.status = 1
		TH_GPIO().send(self.pin_number,self.status)
		
    
	def off(self):
		self.status = 0
		TH_GPIO().send(self.pin_number,self.status)
    
	def blink(self,numTimes=3,speed=1):
		for i in range(0,numTimes):## Run loop numTimes
			self.on()
			time.sleep(speed)## Wait
			self.off()
			time.sleep(speed)## Wait


	def cleanup(self):
		TH_GPIO().disable_pin(self.gpin_number)
		self.status = 0
		

class PWM_LED():
	def __init__(self,pin_number=7,freq=100):
		self.pin_number = pin_number
		self.freq = freq
		self.pwm = TH_GPIO().pwm_create(self.pin_number,freq=self.freq)
    
	def set_freq(self,freq):
		self.freq = freq
		self.pwm.set_freq(freq)
	
	def dim(self,start=100,end=0,step=-1,dur=0.1):
		if self.pwm is not None:			
			for dc in range(start,end, step):
				self.pwm.change(dc)
				time.sleep(dur)

	def brighten(self,start=0,end=100,step=1,dur=0.1):
		if self.pwm is not None:			
			for dc in range(start,end, step):
				self.pwm.change(dc)
				time.sleep(dur)				

	def cleanup(self):
		TH_GPIO().disable_pin(self.pin_number)		
		
class ARRAY_LED():
	def __init__(self,gpio_numbers=[]):
		self.leds = {}
		for p in gpio_numbers:
			TH_GPIO().enable_pin(p,mode='out')
			self.leds[p] = 0
    
	def on(self,leds=[]):
		for p in leds:
			TH_GPIO().send(p,1)
			self.leds[p] = 1
		
    
	def off(self,leds=[]):
		for p in leds:
			TH_GPIO().send(p,0)
			self.leds[p] = 0
    
	def blink(self,leds=[],numTimes=3,dur=1):
		for i in range(0,numTimes):## Run loop numTimes
			self.on(leds) 
			time.sleep(dur)## Wait
			self.off(leds)
			time.sleep(dur)## Wait


	def cleanup(self):
		for p in self.leds:
			TH_GPIO().disable_pin(p)
		self.leds.clear()		
		
