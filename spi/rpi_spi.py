import spidev


class RPI_SPI ():
	def __init__(self):
		try:
			self.spi_0 = spidev.SpiDev()
			self.spi_1 = spidev.SpiDev()
			self.spi_0.open(0,0)
			self.spi_1.open(0,1)
		except:
			self.spi_0 = None
			self.spi_1 = None
			
	def get_device(self,device=0):
		if device==0:
			return self.spi_0
		elif device==1:
			return self.spi_1
		else :
			return None

