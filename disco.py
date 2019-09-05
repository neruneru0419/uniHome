import RPi.GPIO as GPIO
import time
import threading
import audio
import dance

thread_audio = threading.Thread(target=audio.sound)
thread_dance = threading.Thread(target=dance.dance)

thread_audio.start()
thread_dance.start()
