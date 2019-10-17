import RPi.GPIO as GPIO
import time

def human_sensor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.IN)
    try:
        return bool(GPIO.input(26))
    except(KeyboardInterrupt):
        print("interrupt")
    GPIO.cleanup()
