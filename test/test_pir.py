from ...

if __name__ == "__main__":
	try :
		pir = PIR()
		pir.start()	
		while 1 :
			print(pir.result())
	except KeyboardInterrupt :	
		pir.stop()
		pir.cleanup()
