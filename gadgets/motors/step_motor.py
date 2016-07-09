from gadgets.th_gpio import TH_GPIO
import time 
'''
#referenece:https://arduino-info.wikispaces.com/SmallSteppers		

'''
class Model_28BYJ_48():
	CCW_8_STEP_SEQ = -1
	CCW_4_STEP_SEQ = -2
	CW_8_STEP_SEQ = 1
	CW_4_STEP_SEQ = 2

	
	def __init__(self,pin_numbers=[]):
		if pin_numbers != []:
			self.pins = pin_numbers
			TH_GPIO().enable_pins(self.pins,mode='out')
			for p in self.pins:
				TH_GPIO().send(p,False)

		self.seq = [[1,0,0,1],
				[1,0,0,0],
				[1,1,0,0],
				[0,1,0,0],
				[0,1,1,0],
				[0,0,1,0],
				[0,0,1,1],
				[0,0,0,1]]
		
		self.step_formular = {-1:(8,4076,5.625),
						-2:(4,2038,11.25),
						1:(8,4096,5.625),
						2:(4,2038,11.25)}
		
		self.step_count = len(self.seq)
		#self.step_dir = 1 # Set to 1 or 2 for clockwise  # Set to -1 or -2 for anti-clockwise	
		self.wait_time = 3/float(1000) # do not use 1 ! it will not step
		# Initialise variables
		#self.step_counter = 0
		self.dir_err = "Invalid direction value, \nit must be one of -2,-1,0,1,2. \n0 : swing back and forth (angular_step)\n 1 : step clockwise with 8 step-sequences \n 2 : step clockwise with 4 step-sequences \n-1 : step couter clockwise with 8 step-sequences \n-2 : step couter clockwise with 4 step-sequences."
		self.wt_err="waiting time must be an integer between 2 and 20.(Lower is faster)"
		 
	def step(self,rnd=1,direction=2,waiting_time=2):
		assert (direction in [-1,-2,1,2]),self.dir_err
		assert (2 <= waiting_time <= 20) ,self.wt_err
		'''
		direction = 1  : 
		 - step clockwise 
		 - use 8 step-sequence
		 - takes 4096 steps per output shaft revolution
		 
 		direction = 2  : 
		 - step clockwise 
		 - use 4 step-sequence
		 - takes 2048 steps per output shaft revolution

		direction = -1  : 
		 - steps counter clockwise 
		 - use 8 step-sequence
		 - takes 4096 steps per output shaft revolution
		 
 		direction = -2  : 
		 - steps counter clockwise 
		 - use 4 step-sequence
		 - takes 2048 steps per output shaft revolution
		'''
		info_touple = self.step_formular[direction]		
		max_rev = info_touple[1]*rnd
		wait_time = waiting_time/float(1000)
		self._step(max_rev,direction,wait_time)
	

	def angular_step(self,angle=90,direction=2,waiting_time=2,bi_direction=False):
		assert (direction in [-1,-2,1,2]),self.dir_err
		assert (2 <= waiting_time <= 20) ,self.wt_err
		info_touple = self.step_formular[direction]	
		rnd,angle = self._div(angle,360)
		max_rev = info_touple[1]*rnd + angle * info_touple[1] // 360
		wait_time = waiting_time/float(1000)
		self._step(max_rev,direction,wait_time)
		if bi_direction :
			self._step(max_rev,-direction,wait_time)
			
	
	def _step(self,max_rev,direction,wait_time):
		rev = 0
		step_counter = 0
		while rev < max_rev: 
			for pin in range(0,4):
				gpio_pin=self.pins[pin]# Get GPIO
				step_val = self.seq[step_counter][pin]
				TH_GPIO().send(gpio_pin,step_val)
 
			step_counter += direction
 
			# If we reach the end of the sequence
  			# start again
  			
			if (step_counter >= self.step_count):
				step_counter = 0
			if (step_counter < 0):
				step_counter = self.step_count + direction
 			
			# Wait before moving on
			time.sleep(wait_time)
			rev += 1
	
	def _div(self,v1,v2):
		res=(0,0)
		if v2 >= v1 :
			return (0,v1)
		vt = v1 - v2
		m = 1
		while vt > v2 :
			vt = vt - v2
			m +=1
		return (m,vt)
