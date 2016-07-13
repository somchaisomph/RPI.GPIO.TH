import subprocess
import threading
import time

class DS18B20(threading.Thread):
	SLAVE_PATH = "/sys/bus/w1/devices/"
	SLAVE_FILE = "w1_slave"

	def __init__(self,sensor_id,interval=2):	
		threading.Thread.__init__(self)	
		self.sensor_id = sensor_id
		self.time_interval = interval
		self.cmd = self.SLAVE_PATH + sensor_id+"/"+self.SLAVE_FILE 
		self.running = False
		self.temp_c = 0
		
	def run(self):
		self.running = True
		while self.running:
			self.temp_c = self.read()
			time.sleep(self.time_interval)				

	def stop(self):
		self.running = False
				
	def read(self):	
		proc = subprocess.Popen(['cat',self.cmd],stdout=subprocess.PIPE)

		# stdout_value is array of bytes. Use decode('utf-8') to change it to a String
		stdout_value = proc.communicate()[0].decode('utf-8')

		#remove newline symbol
		stdout_value=stdout_value.replace('\n','')

		tpos = stdout_value.find('t=')
		temp_str = stdout_value[tpos+2:]
		return float(temp_str)
		
	@property	
	def C(self):
		return self.temp_c/1000
		
	@property
	def F(self):
		t  = self.C
		f = t * 9.0 / 5.0 + 32.0
		return f
	


