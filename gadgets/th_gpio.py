import atexit
import RPi.GPIO as GPIO ## Import GPIO library

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

'''
I think TH_GPIO class is needed to be a singleton
to be sure that there is only one instance of it running
at a time.
'''

@singleton      
class TH_GPIO():
	
	def __init__(self):
		GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
		self._gpios = {}
		#to make sure every gpio pin will be cleanup at the end of program.
		atexit.register(self.all_done)
  
	def enable_pin(self,pin_number,mode='in'):
		if pin_number not in self._gpios :
			mode = mode.lower()
			if mode == 'out' :
				GPIO.setup(pin_number, GPIO.OUT)
			elif mode == 'in' :
				GPIO.setup(gpio_number, GPIO.IN) 
			self._gpios[pin_number]=None


	def enable_pins(self,pin_list=[],mode='in'):
		mode = mode.lower()
		for p in pin_list:
			if p not in self._gpios :
				if mode == 'out' :
					GPIO.setup(p, GPIO.OUT) 
				elif mode == 'in':
					GPIO.setup(p, GPIO.IN) 
			self._gpios[p]=None	


	def send(self,pin_number,state=True):
		if pin_number in self._gpios :
			GPIO.output(pin_number,state)
  
	def read(self,pin_number):
		res = None
		if pin_number in self._gpios :
			res = GPIO.input(pin_number)
		return res


	def pwm_create(self,pin_number,freq=100):
		p = None
		if pin_number not in self._gpios:
			GPIO.setup(pin_number, GPIO.OUT)
			p = SOFT_PWM(GPIO.PWM(pin_number,freq),freq)
			self._gpios[pin_number]=p
		return p

		
	def disable_pin(self,pin_number):
		if pin_number in self._gpios :
			if self._gpios[pin_number] is not None:				
				# it is pwn pin, should be stop before cleanup
				self._gpios[pin_number].stop() 
			GPIO.cleanup(pin_number)				
			del self._gpios[pin_number]


	def disable_pins(self,pin_list):
		for p in pin_list:
			if self._gpios[pin_number] is not None:				
				self._gpios[pin_number].stop() 
			GPIO.cleanup(pin_number)				
			del self._gpios[pin_number]
          
	def all_done(self):
		if len(self._gpios) > 0 :
			for p in self._gpios:
				if self._gpios[p] is not None:				
					self._gpios[p].stop() 
				GPIO.cleanup(p)							
			self._gpios.clear()	

	

class SOFT_PWM():
	def __init__(self,pwm,freq):
		self.pwm = pwm
		self.freq = freq
		self.pwm.start(1)

	def stop(self):
		self.pwm.stop()
		
	def change(self,dc):
		self.pwm.ChangeDutyCycle(dc)
		
	def set_freq(self,freq):
		self.pwm.ChangeFrequency(freq)
		self.freq = freq

