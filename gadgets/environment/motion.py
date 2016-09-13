import threading
import time
from gadgets.th_gpio import TH_GPIO

class PIR(threading.Thread):
	def __init__(self,pin_number=11,interval=10):
		threading.Thread.__init__(self)
		self.pin_number = pin_number
		TH_GPIO().enable_pin(self.pin_number,mode='in')
		self.current_state = 0
		self.previous_state = 0
		self.ready = 0
		self.exit_flag = 0
		self.motion_detected = 0
		self.interval = interval
		while TH_GPIO().read(self.pin_number) == 1 :
			self.current_state = 0
		self.ready = 1

		
	def run(self):
		if self.ready != 1 :
			return
		while self.exit_flag == 0 :
			self.current_state = TH_GPIO().read(self.pin_number)
			if self.current_state == 1 and self.previous_state == 0 :
				self.motion_detected = 1
				self.previous_state = 1
			elif self.current_state == 0 and self.previous_state == 1 :
				self.motion_detected = 0
				self.previous_state = 0
			time.sleep(self.interval/1000)
			
	def result(self):
		return self.motion_detected
	
	def stop(self):
		self.exit_flag = 1
		
	def cleanup(self):
		TH_GPIO().disable_pin(self.pin_number)
