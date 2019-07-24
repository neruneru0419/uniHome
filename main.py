import RPi.GPIO as GPIO
import time
import threading
import UniboFace
import UniboArm
import UniboServer
unibo_arm = threading.Thread(target=UniboArm.Arm().move_arm)
unibo_face = threading.Thread(target=UniboFace.DotMatrixLED().loop_face)
unibo_server = threading.Thread(target=UniboServer.MyHandler().main)
unibo_arm.start()
unibo_face.start()
unibo_server.start()

