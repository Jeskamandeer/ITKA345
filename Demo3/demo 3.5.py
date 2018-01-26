import RPi.GPIO as GPIO
import datetime
import time
import picamera

PIR=4
PRINT1=0
PRINT2=0
camera = picamera.PiCamera()
monesko=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)

loppu = time.time() + 30
while time.time() < loppu:
	if GPIO.input(PIR) == 1: 
		if PRINT1 == 0:
			print("OTETAAN KUVA")
			camera.capture('image'+str(monesko)+'.jpg')
			monesko = monesko +1
			PRINT1 = 1
			PRINT2 = 0
			time.sleep(1.0)
			
		if GPIO.input(PIR) == 0:
			if PRINT2 == 0:
				print("LIIKE LOPPUU")
				PRINT2=1
				PRINT1=0
time.sleep(1.0)
		
		
GPIO.cleanup()