from datetime import datetime as dt
import sys, tty, termios, threading


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
      print ("Exiting " + self.name)


def RunForward(speed):
    run = True
    ct = dt.now()
    while run:
        if (dt.now() - ct).total_seconds() >= 0.002:
            ct = dt.now()
            print("pali")

        if (dt.now() - ct).total_seconds() >= speed:
            print("gasi")

        char = getch()
        if(char != "w"):
            run = False
            break



# Create new threads
thread1 = myThread(1, "Thread-1", 1)

# Start new Threads
thread1.start()
thread1.join()

print ("Exiting Main Thread")