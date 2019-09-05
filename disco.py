import RPi.GPIO as GPIO
import time
import threading
import audio
import dance
def disco():
    thread_audio = threading.Thread(target=audio.sound)
    thread_dance = threading.Thread(target=dance.dance)

    thread_audio.start()
    thread_dance.start()

def seiden():
    i = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.IN)

    while i < 1.8:
        if GPIO.input(14) != 0:
            i += 0.1
        else:
            return False

        time.sleep(0.1)
