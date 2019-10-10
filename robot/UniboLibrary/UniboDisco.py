import RPi.GPIO as GPIO
import time
import threading
import subprocess
def sound():
    GPIO.setmode(GPIO.BCM)

    CMD = "aplay /home/pi/hello-Pi/トーマス.wav"
    try:
        subprocess.call(CMD, shell=True)

    except KeyboardInterrupt:
        pass
def dance():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(24, GPIO.OUT)
    right = GPIO.PWM(24, 50)
    right.start(0)

    GPIO.setup(23, GPIO.OUT)
    left = GPIO.PWM(23, 50)
    left.start(0)

    for i in range(8):
        right.ChangeDutyCycle(2.5)
        left.ChangeDutyCycle(4.875)
        time.sleep(0.3)

        right.ChangeDutyCycle(9.625)
        left.ChangeDutyCycle(12)
        time.sleep(0.3)
    right.ChangeDutyCycle(2.5)
    time.sleep(1)
def five_dance():
    for i in range(5):
        dance()

def disco():
    thread_audio = threading.Thread(target=sound)
    thread_dance = threading.Thread(target=dance)

    thread_audio.start()
    thread_dance.start()

