from gadgets.th_gpio import TH_GPIO
import time 

class Servo5V():
	def __init__(self,pin_number=12,freq=100):
		self.pin_number = pin_number
		self.freq = freq
		self.pwm = TH_GPIO().pwm_create(self.pin_number,freq=self.freq)
		self.width = float(1000/self.freq)
		
	def set_freq(self,freq):
		self.freq = freq
		self.pwm.set_freq(freq)
		self.width = float(1000/self.freq)
		
	def write(self,angle):
		duty = float(angle)/self.width + 2.5
		self.pwm.change(duty)
	
	def cleanup(self):
		TH_GPIO().disable_pin(self.pin_number)	
