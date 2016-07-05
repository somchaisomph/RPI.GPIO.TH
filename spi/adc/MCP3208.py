import spidev
import time
import sys

try:
	# To open spi bus
	spi = spidev.SpiDev()

	# Raspi has only one spi bus (#0) and able to connect 2 devices (#0,#1) .
	spi.open(0,0) # connect to device with bus=0,device=0
except :
	spi = None

class MCP3208 :
	def __init__(self,spi=None):
		self.spi = spi

	def create_cmd(self,channel=None):
		if self.spi is None or channel is None :
			return []

		start_bit = 0x01
		end_bit = 0x08
		# last element must be 0 --> Why ?
		return [start_bit,(end_bit | channel)<<4,0]
	
	def process_data(self,data):
		'''
		Take in result as array of three bytes.
		Returns two lowest bits of the 2nd byte and
		all of the third byte
		'''
		if data is None :
			return None
		secd_byte = (data[1] & 0x03) # & is bitwise 'and'
		return (secd_byte<<8) | data[2] # | bitwise 'or'

	def read_adc(self,channel):
		if channel > 7 or channel < 0 :
			return None
		if self.spi is None :
			return None
		data = self.spi.xfer2(self.create_cmd(channel))
		return self.process_data(data)


if __name__ == "__main__":
	mcp = MCP3208(spi)		
	swt_channel = 0
	vrx_channel = 1
	vry_channel = 2	
	delay = 0.5
	while True:
		vrx_pos = mcp.read_adc(vrx_channel)
  		vry_pos = mcp.read_adc(vry_channel)
 
  		# Read switch state
  		swt_val = mcp.read_adc(swt_channel)
 
		# Print out results
		print "--------------------------------------------"
		print("X : {}  Y : {}  Switch : {}".format(vrx_pos,vry_pos,swt_val))
 
		# Wait before repeating loop
		time.sleep(delay)
		
