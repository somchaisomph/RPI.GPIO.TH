import atexit
import RPi.GPIO as GPIO ## Import GPIO library

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance
    
class TH_GPIO():
  def __init__(self):
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    self._gpios = []
    atexit.register(self.all_done)
  
  def enable_pin(self,pin_number,mode='in'):
    if pin_number not in self._gpios :
      #should check valid pin number
      mode = lower(mode)
      if mode == 'out' :
        GPIO.setup(pin_number, GPIO.OUT) 
      elif mode == 'in':
        GPIO.setup(self.gpio_number, GPIO.IN) 
      self._gpios.append(pin_number)

  def enable_pins(self,pin_list=[],mode='in'):
    mode = lower(mode)
    for p in pin_list:
      if p not in self._gpios :
        if mode == 'out' :
        GPIO.setup(pin_number, GPIO.OUT) 
      elif mode == 'in':
        GPIO.setup(self.gpio_number, GPIO.IN) 
      self._gpios.append(p)

  def send(self,pin_number,state=True):
    if pin_number in self._gpios :
      GPIO.output(pin_number,state)
  
  def read(self,pin_number):
    res = None
    if pin_number in self._gpios :
      res = GPIO.input(pin_number)
    return res

  def disable_pin(self,pin_number):
      if pin_number in self._gpios :
          GPIO.cleanup(pin_number)
          self._gpios.remove(pin_number)

  def disable_pins(self,pin_list):
      for p in pin_list:
        if pin_number in self._gpios :
          GPIO.cleanup(pin_number)
          self._gpios.remove(p)
          
  def all_done(self):
    GPIO.cleanup()
  
TH_GPIO = singleton(TH_GPIO)  
