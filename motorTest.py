import RPi.GPIO as GPIO 
from datetime import datetime as dt
import time

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

initial = True
state = False
starttime = dt.now()
pressed = False

def LightLED(LedId, state):
    GPIO.output(LedId, state)

def TurnOff():
    GPIO.output(31,False)
    GPIO.output(33,False)
    GPIO.output(35,False)
    GPIO.output(37,False)

TurnOff()
     
print "Spreman!"
try:
    print "F1"
    LightLED(33, 1)
    print "F3"
    LightLED(35, 1)

    time.sleep(0.5)
    LightLED(35, 0)

    LightLED(33, 0)

    print "F2"
    LightLED(31, 1)
    
    print "F4"
    LightLED(37, 1)

    time.sleep(0.5)
    LightLED(37, 0)
    LightLED(31, 0)
    
    GPIO.cleanup()
    
except KeyboardInterrupt:
    GPIO.cleanup()

