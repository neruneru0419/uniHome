import RPi.GPIO as GPIO
import time
import subprocess

def sound():
    GPIO.setmode(GPIO.BCM)

    CMD = "aplay /home/pi/hello-Pi/トーマス.wav"
    try:
        subprocess.call(CMD, shell=True)

    except KeyboardInterrupt:
        pass
#sound()
