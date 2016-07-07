import atexit
import RPi.GPIO as GPIO ## Import GPIO library

class TH_GPIO():
  def __init__(self,gpio_nuber,mode='IN'):
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    self.mode = lower(mode)
    self.gpio_number =  gpio_number
    if mode == 'out' :
      GPIO.setup(self.gpio_number, GPIO.OUT) 
    elif mode == 'in':
      GPIO.setup(self.gpio_number, GPIO.IN) 
    atexit.register(self.all_done)
    
  def out(self,state=True):
    GPIO.output(self.gpio_number,state)
  
  def all_done(self):
    GPIO.cleanup(self.gpio_number)
  
