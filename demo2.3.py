import RPi.GPIO as GPIO
import time


KAV1=23
KAV2=24

AUT1=4
AUT2=5
AUT3=6

painettu=0
NAPPI=17
GPIO.setmode(GPIO.BCM)

GPIO.setup(NAPPI, GPIO.IN)

GPIO.setup (AUT1, GPIO.OUT)
GPIO.setup (AUT2, GPIO.OUT)
GPIO.setup (AUT3, GPIO.OUT)

GPIO.setup (KAV1, GPIO.OUT)
GPIO.setup (KAV2, GPIO.OUT)

		

def vaihdavalot():
	GPIO.output(KAV1, 1)
	GPIO.output(KAV2, 0)
	GPIO.output(AUT1, 1)
	time.sleep (3.0)
	GPIO.output(AUT1, 0)
	GPIO.output(AUT2, 1)
	time.sleep (1.0)
	GPIO.output(AUT2, 0)
	GPIO.output(AUT3, 1)
	GPIO.output(KAV1, 0)
	GPIO.output(KAV2, 1)
	time.sleep(3.0)
	GPIO.output(AUT2, 1)
	GPIO.output(AUT3, 0)
	GPIO.output(KAV1, 1)
	GPIO.output(KAV2, 0)
	time.sleep (1.0)
	GPIO.output(AUT1, 1)
	GPIO.output(AUT2, 0)
	
	
	
loppu = time.time() + 30

while time.time() < loppu:
	if GPIO.input(NAPPI) == 1:
		
		if painettu == 0:
			vaihdavalot()
			
			painettu = 1
GPIO.cleanup()