from gadgets.th_gpio import TH_GPIO
import time 


class LED():
	def __init__(self,gpio_number=7):
		self.gpio_number = gpio_number
		#A singleton class is treated like a function
		TH_GPIO().enable_pin(gpio_number,mode='out')
		self.status = 0 #0:off,1:on
    
	def on(self):
		self.status = 1
		TH_GPIO().send(self.gpio_number,self.status)
		
    
	def off(self):
		self.status = 0
		TH_GPIO().send(self.gpio_number,self.status)
    
	def blink(self,numTimes=3,speed=1):
		self.status =  1
		for i in range(0,numTimes):## Run loop numTimes
			TH_GPIO().send(self.gpio_number,1)
			time.sleep(speed)## Wait
			TH_GPIO().send(self.gpio_number,0)
			time.sleep(speed)## Wait
		self.status = 0

	def cleanup(self):
		TH_GPIO().disable_pin(self.gpio_number)
		self.status = 0
		
class PWM_LED():
	def __init__(self,gpio_number=7,freq=100):
		self.gpio_number = gpio_number
		self.freq = freq
		self.pwm = TH_GPIO().pwm_create(self.gpio_number,freq=self.freq)
    
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
		TH_GPIO().disable_pin(self.gpio_number)		
