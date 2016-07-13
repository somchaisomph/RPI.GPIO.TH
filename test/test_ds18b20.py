from gadgets.weather.DS18B20 import DS18B20 
import time

_id = '28-0000066a6165' # change it to be your own id

sensor = DS18B20(_id,2)

try:
	sensor.start()
	while True :
		print(sensor.C)
		time.sleep(2)
	
except KeyboardInterrupt:
	print("Stoping")
	
finally:	
	sensor.stop()
	sensor.join()
	
