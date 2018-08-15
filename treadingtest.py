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
speed = 80

counter = 4

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
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      sensor(self.name)


def sensor(threadName):
   global exitFlag
   global stop
   while True:
       if stop:
           return
       elif GPIO.input(leftPin) == False:
           exitFlag = 1
           print("left")
       elif GPIO.input(rightPin) == False:
           exitFlag = 1
           print("righ")
       else:
           exitFlag = 0
       print("thread")
       time.sleep(0.1)


# Create new threads
thread1 = myThread(1, "Thread-1")

# Start new Threads
thread1.start()

try:
    while True:
        if exitFlag:
            TurnOff()
            while counter:
                reverseRight.start(speed)
                reverseLeft.start(speed)
                reverseRight.ChangeDutyCycle(speed)
                reverseLeft.ChangeDutyCycle(speed)
                time.sleep(0.2)
                counter -= 1
        else:
            forwardRight.start(speed)
            forwardLeft.start(speed)
            forwardRight.ChangeDutyCycle(speed)
            forwardLeft.ChangeDutyCycle(speed)
            counter = 4
        time.sleep(0.1)
        print("main")
        print(exitFlag)

except KeyboardInterrupt:
    GPIO.cleanup()
    stop = 1


print("Kraj!")
