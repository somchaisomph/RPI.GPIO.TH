import spidev
import time
import sys

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



		
