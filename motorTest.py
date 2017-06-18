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

def RunForward(speed):
    run = True
    ct = dt.now()
    while run:
        LightLED(33, 1)
        LightLED(35, 1)
        time.sleep(speed)
        LightLED(33, 0)
        LightLED(35, 0)
        if ((ct-dt.now()).total_seconds() > 0.5):
            run = False

def RunBackward(speed):
    run = True
    ct = dt.now()
    while run:
        LightLED(31, 1)
        LightLED(37, 1)
        time.sleep(speed)
        LightLED(31, 0)
        LightLED(37, 0)
        if ((ct-dt.now()).total_seconds() > 0.5):
            run = False


TurnOff()
     
print "Spreman!"
try:
    RunForward(0.1)    
    GPIO.cleanup()
    
except KeyboardInterrupt:
    GPIO.cleanup()

