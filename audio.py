import RPi.GPIO as GPIO
import time
import subprocess

def sound():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.IN)

    CMD = "aplay /home/pi/hello-Pi/トーマス.wav"
    try:
        while True:
            if GPIO.input(14):
                subprocess.call(CMD, shell=True)
            time.sleep(0.01)

    except KeyboardInterrupt:
        pass

GPIO.cleanup()
