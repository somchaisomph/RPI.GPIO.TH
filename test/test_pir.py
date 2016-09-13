from gadgets.environment.motion import PIR

if __name__ == "__main__":
	try :
		pir = PIR()
		pir.start()
		print('Ctrl-c to exit.')
		while 1 :
			print(pir.result()) # 1 : motion detected, 0: no motion detected
	except KeyboardInterrupt :	
		pir.stop()
		pir.cleanup()
