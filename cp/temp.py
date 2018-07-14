import subprocess
import time
from gpiozero import PWMLED

def readTemp():
  # variable should look something like "temp=46.5'C\n"
  p = subprocess.Popen(["/usr/bin/vcgencmd", "measure_temp"], 
			stdout=subprocess.PIPE, 
			stderr=subprocess.STDOUT).communicate()[0]
  # extract the raw value
  val = p.split('=')[1].split('\'')[0]

  # convert string to float
  return float(val)

def convertF(degreesc):
  return (degreesc * 1.8) + 32
 
def intensity(value, min, max):
  if value < min:
    return 0.0
  elif value > max:
    return 1.0
  else:
    return (1.0) * (value - min) / (max - min) 

led = PWMLED(17)
led.on()

while True: 
  led.value = intensity(convertF(readTemp()), 115, 125)
  print led.value
  time.sleep(0.5)



