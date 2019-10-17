import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
def seiden():
    i = 0

    while i < 1.5:
        if GPIO.input(14):
            i += 0.1
        else:
            break
        time.sleep(0.1)
    return bool(i >= 1.5)
