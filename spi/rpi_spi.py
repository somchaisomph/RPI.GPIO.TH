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
			
	def get_spi_0(self):
		return self.spi_0
		
	def get_spi_1(self):
		return self.spi_1
		
