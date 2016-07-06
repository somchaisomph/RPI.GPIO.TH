import spidev


class rpi_spi_dev ():
	def __init__(self,device=0):
		try:
			# To open spi bus
			self.spi = spidev.SpiDev()
			# Raspi has only one spi bus (#0) and able to connect 2 devices (#0,#1).
			self.spi.open(0,device)
		except:
			self.spi = None
			
			
	def get_device(self):
		return self.spi

