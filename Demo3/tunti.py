import RPi.GPIO as GPIO
import datetime
import time
import picamera

camera = picamera.PiCamera()
aika = localtime()

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)

camera.capture(str(aika)+'.jpg')


time.sleep(1.0)
			
GPIO.cleanup()