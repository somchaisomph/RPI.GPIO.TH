import RPi.GPIO as GPIO ## Import GPIO library
import time 

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

class LED():
  def __init__(self,gpio_number=7):
    self.gpio_number = gpio_number
    GPIO.setup(self.gpio_number, GPIO.OUT) 
    
  def on(self):
    GPIO.output(self.gpio_number,True)
    
  def off(self):
    GPIO.output(self.gpio_number,False)
    
  def blink(self,numTimes=3,speed=1):
    for i in range(0,numTimes):## Run loop numTimes
      GPIO.output(self.gpio_number,True)## Switch on pin 7
      time.sleep(speed)## Wait
      GPIO.output(self.gpio_number,False)## Switch off pin 7
      time.sleep(speed)## Wait
      
  def clean_up(self):
    GPIO.cleanup(self.gpio_number)

      
