import RPi.GPIO as GPIO 
from datetime import datetime as dt
import sys, tty, termios, time, threading

class myTh (threading.Thread):
	def __init__(self, threadID, name, where, speed):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
        self.where = where
        self.speed = speed
	def run(self):
        run(self.where, self.speed)
		

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

initial = True
state = False
starttime = dt.now()
pressed = False

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def run(where, speed):
	if(where == "r"):
		RunRight(speed, threadName)
	if(where == "l"):
		RunLeft(speed, threadName)
    if(where == "f"):
        RunForward(speed, threadName)
    if(where == "b"):
        RunBackward(speed, threadName)

def LightLED(LedId, state):
    GPIO.output(LedId, state)

def TurnOff():
    GPIO.output(31,False)
    GPIO.output(33,False)
    GPIO.output(35,False)
    GPIO.output(37,False)

def RunForward(speed, threadName):
    run = True
    ct = dt.now()
    while run:
        char = getch()
        LightLED(33, 0)
        LightLED(35, 0)
        if(char != "w" or ((dt.now()-ct).total_seconds() > 0.1)):
            run = False
            threadName.exit()
            break
        time.sleep(speed)
        LightLED(33, 1)
        LightLED(35, 1)
        time.sleep(speed)

def RunRight(speed, threadName):
    run = True
    ct = dt.now()
    while run:
        char = getch()
        LightLED(33, 0)
        if(char != "a" or ((dt.now()-ct).total_seconds() > 0.1)):
            run = False
            threadName.exit()
            break
        time.sleep(speed)
        LightLED(33, 1)
        time.sleep(speed)

def RunLeft(speed, threadName):
    run = True
    ct = dt.now()
    while run:
        char = getch()
        LightLED(35, 0)
        if(char != "d" or ((dt.now()-ct).total_seconds() > 0.1)):
            run = False
            threadName.exit()
            break
        time.sleep(speed)
        LightLED(35, 1)
        time.sleep(speed)

def RunBackward(speed, threadName):
    run = True
    ct = dt.now()
    while run:
        char = getch()
    	LightLED(31, 0)
    	LightLED(37, 0)
        if(char != "s" or ((dt.now()-ct).total_seconds() > 0.1)):
            run = False
            threadName.exit()
            break
    	time.sleep(speed)
    	LightLED(31, 1)
    	LightLED(37, 1)
        time.sleep(speed)

TurnOff()

print "Spreman!"

while True:
    char = getch()
    if(char == "w"):
        #print("naprijed")
        thf = myTh(1,"f","f",0.001))
        thf.start()

    if(char == "s"):
        #print("nazad")
        thb = myTh(2,"b","b",0.001))
        thb.start()

    if(char == "a"):
        #print("desno")
        thr = myTh(3,"r","r",0.001))
        thr.start()

    if(char == "d"):
        #print("lijevo")
        thl = myTh(4,"l","l",0.001))
        thl.start()

    if(char == "x"):
        print("Kraj")
        break

     
try:
    #RunForward(0.0001)
    #RunBackward(0.0001)  
    GPIO.cleanup()
    
except KeyboardInterrupt:
    GPIO.cleanup()

