import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)

pwm=GPIO.PWM(03, 50)

pwm.start(0)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(03, True)
	pwm.ChangeDutyCycle(duty)
	sleep(0.5)
	GPIO.output(03, False)
	pwm.ChangeDutyCycle(0)

SetAngle(90)
SetAngle(100)
SetAngle(110)
SetAngle(120)
SetAngle(130)
SetAngle(140)
SetAngle(150)
SetAngle(160)
SetAngle(170)
SetAngle(180)
SetAngle(170)
SetAngle(160)
SetAngle(150)
SetAngle(140)
SetAngle(130)
SetAngle(120)
SetAngle(110)
SetAngle(100)
SetAngle(90)
SetAngle(80)
SetAngle(70)
SetAngle(60)
SetAngle(50)
SetAngle(40)
SetAngle(30)
SetAngle(20)
SetAngle(10)
SetAngle(0)

pwm.stop()
GPIO.cleanup()