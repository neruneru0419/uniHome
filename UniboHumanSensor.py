import RPi.GPIO as GPIO
import time

class UniboHumanSensor:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.IN)
    def human_sensor(self):
        try:
            while True:    
                if GPIO.input(26):
                    return False
                else:
                    return True
        except(KeyboardInterrupt):
            print("interrupt")
        GPIO.cleanup()