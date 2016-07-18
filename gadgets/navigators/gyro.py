from spi.rpi_spi import rpi_spi_dev
from spi.adc.MCP3208 import MCP3208

class GYRO_GY61():
	# use chip ADXL335
	def __init__(self,device=0,x_channel=0,y_channel=1,z_channel=2):
		self.spi = rpi_spi_dev(device).spi
		self.mcp = None
		if self.spi is not None:
			self.mcp = MCP3208(self.spi)	
		self.vrx_channel = x_channel
		self.vry_channel = y_channel
		self.vrz_channel = z_channel	

	def get_data(self):
		if self.mcp is None:
			return (0,0)
		xpos = self.mcp.read_adc(self.vrx_channel)
        	ypos = self.mcp.read_adc(self.vry_channel)
        	zpos = self.mcp.read_adc(self.vrz_channel)
		return (xpos,ypos,zpos)
