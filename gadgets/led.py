from gadgets.th_gpio import TH_GPIO
import time 


class LED():
	def __init__(self,gpio_number=7):
		self.gpio_number = gpio_number
		#A singleton class is treated like a function
		TH_GPIO().enable_pin(gpio_number,mode='out')
    
	def on(self):
		TH_GPIO().send(self.gpio_number,1)
    
	def off(self):
		TH_GPIO().send(self.gpio_number,0)
    
	def blink(self,numTimes=3,speed=1):
		for i in range(0,numTimes):## Run loop numTimes
			TH_GPIO().send(self.gpio_number,1)
			time.sleep(speed)## Wait
			TH_GPIO().send(self.gpio_number,0)
			time.sleep(speed)## Wait
      
	def cleanup(self):
		TH_GPIO().disable_pin(self.gpio_number)

      
