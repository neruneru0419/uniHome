import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
def seiden():
    i = 0

    while i < 1.0:
        if GPIO.input(14) != 0:
            i += 0.1
        else:
            return False
        time.sleep(0.1)
    return True
