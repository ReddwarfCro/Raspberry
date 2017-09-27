import logging
import RPi.GPIO as GPIO
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/home/pi/logs/startup.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

try:
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.setup(35, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)
    GPIO.cleanup()
except:
    logger.error("E nesto nije u redu")



logger.info('Masina se rebutala i resetirala GPIO')

