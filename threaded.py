import RPi.GPIO as GPIO
from datetime import datetime as dt
import sys, tty, termios, time, threading

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


def LightLED(LedId, state):
    GPIO.output(LedId, state)


def TurnOff():
    GPIO.output(31, False)
    GPIO.output(33, False)
    GPIO.output(35, False)
    GPIO.output(37, False)


class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print ("Starting ")
      print("Spreman!")
      speed = 0.001

      while True:
         char = getch()
         if (char == "w"):
            # print("naprijed")
            RunForward(speed)

         if (char == "s"):
            # print("nazad")
            RunBackward(speed)

         if (char == "d"):
            # print("desno")
            RunRight(speed)

         if (char == "a"):
            # print("lijevo")
            RunLeft(speed)

         if (char == "r"):
            speed = speed - 0.0001
            if (speed < 0.0005):
                speed = 0.0005
            print (speed)

         if (char == "f"):
            speed = speed + 0.0001
            if (speed > 0.002):
                speed = 0.002
            print (speed)

         if (char == "x"):
            print("Kraj")
            break

         TurnOff()

      print ("Exiting " + self.name)


def RunForward(speed):
    ct = dt.now()
    while True:
        if (dt.now() - ct).total_seconds() >= 0.002:
            ct = dt.now()
            LightLED(31, 1)
            LightLED(37, 1)

        if (dt.now() - ct).total_seconds() >= speed:
            LightLED(31, 0)
            LightLED(37, 0)

        char = getch()
        if char != "w":
            break


def RunRight(speed):
    run = True
    ct = dt.now()
    while run:
        LightLED(31, 0)
        char = getch()
        if(char != "d"):
            run = False
            break
        time.sleep(speed)
        LightLED(31, 1)
        time.sleep(speed)


def RunLeft(speed):
    run = True
    ct = dt.now()
    while run:
        LightLED(37, 0)
        char = getch()
        if(char != "a"):
            run = False
            break
        time.sleep(speed)
        LightLED(37, 1)
        time.sleep(speed)


def RunBackward(speed):
    run = True
    ct = dt.now()
    while run:
        LightLED(33, 0)
        LightLED(35, 0)
        char = getch()
        if(char != "s"):
            run = False
            break
        time.sleep(speed)
        LightLED(33, 1)
        LightLED(35, 1)
        time.sleep(speed)

TurnOff()

# Create new threads
thread1 = myThread(1, "Thread-1", 1)

# Start new Threads
thread1.start()
thread1.join()

GPIO.cleanup()

print ("Exiting Main Thread")