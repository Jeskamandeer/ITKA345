import RPi.GPIO as GPIO
import time

PIR=4
PRINT1=0
PRINT2=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)

loppu = time.time() + 30
while time.time() < loppu:
	if GPIO.input(PIR) == 1: 
		if PRINT1 == 0:
			print("LIIKE ALKAA")
			PRINT1 = 1
			PRINT2 = 0
		time.sleep (0.5)
		
		if GPIO.input(PIR) == 0:
			if PRINT2 == 0:
				print("LIIKE LOPPUU")
				PRINT2=1
				PRINT1=0
		
	
	
	
	time.sleep (0.5)
	
	

GPIO.cleanup()