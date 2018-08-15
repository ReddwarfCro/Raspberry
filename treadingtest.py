import threading
import RPi.GPIO as GPIO
import termios, time

rightPin = 40
leftPin = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

# set GPIO Pins
GPIO_TRIGGER = 12
GPIO_ECHO = 18

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.setup(rightPin, GPIO.IN)
GPIO.setup(leftPin, GPIO.IN)

exitFlag = 0
stop = 0
speed = 30

forwardLeft = GPIO.PWM(31, 50)
reverseLeft = GPIO.PWM(33, 50)

forwardRight = GPIO.PWM(37, 50)
reverseRight = GPIO.PWM(35, 50)

def TurnOff():
    forwardLeft.stop()
    reverseLeft.stop()
    forwardRight.stop()
    reverseRight.stop()

TurnOff()

print("Spreman!")


class myThread (threading.Thread):
   def __init__(self, threadID, name, delay):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.delay = delay
   def run(self):
      sensor(self.name)


def sensor(threadName):
   global exitFlag
   global stop
   while True:
       if GPIO.input(rightPin) == False:
           exitFlag = 1
       elif GPIO.input(leftPin) == False:
           exitFlag = 1
       elif stop:
           return
       else:
           exitFlag = 0


# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()

try:
    while True:
        if exitFlag:
            TurnOff()
        else:
            forwardRight.start(speed)
            forwardLeft.start(speed)
            forwardLeft.ChangeDutyCycle(speed)
            forwardRight.ChangeDutyCycle(speed)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    stop = 1


print("Kraj!")
