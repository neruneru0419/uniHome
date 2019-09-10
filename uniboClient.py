import RPi.GPIO as GPIO
import time
import json
import disco
import seiden
import led_fade
import UniboFace
import UniboHumanSensor
import Unibomic
import UniboArm
from websocket import create_connection
from threading import Thread
#websocket通信のためのクラス
class UniboWs:
    def __init__(self):
        self.ws = create_connection("wss://neruneru.higashi.dev/uniHome/ws")
        with open("./UniboRoboData.json", "r") as f:
            self.unibo_data = json.load(f)
        self.unibo_user = "child"#ユーザーの設定
        self.unibo_data["user"] = self.unibo_user
        self.face_number = 1
        self.unibohs = UniboHumanSensor.UniboHumanSensor()
        print(self.unibo_data)
    def unibo_face(self):
        UniboFace.DotMatrixLED().loop_face(self.face_number)    
    def unibo_headsensor(self):
        self.unibo_data["head_sensor"] = seiden.seiden()
    def unibo_humansensor(self):
        self.unibo_data["human_sensor"] = self.unibohs.human_sensor()
    def unibo_greeting(self):
        self.unibo_data["words"] , self.unibo_data["greeting"] = Unibomic.uniboMic()
    #uniboからのデータ送信
    def unibo_ws_send(self):
        while True:
            result = json.dumps(self.unibo_data)
            self.ws.send(result)
        self.ws.close()
    #uniboやスマホからのデータ受信
    def unibo_ws_recv(self):
        while True:
            result = json.loads(self.ws.recv())
            if result["user"] != self.unibo_user:
                print("Received '%s'" % result) 
                if result["human_sensor"]:
                    led_fade.led_fade()
                elif result["head_sensor"]:
                    disco.disco()
                elif result["greeting"]:
                    UniboArm.Arm(result["words"])
                    
        ws.close()
ws = UniboWs()
unibo_wss = Thread(target=ws.unibo_ws_send)
unibo_wsr = Thread(target=ws.unibo_ws_recv)
face = Thread(target=ws.unibo_face)
head_sensor = Thread(target=ws.unibo_headsensor)
human_sensor = Thread(target=ws.unibo_humansensor)
greeting_sensor = Thread(target=ws.unibo_greeting)

unibo_wss.start()
unibo_wsr.start()
face.start()
head_sensor.start()
human_sensor.start()
greeting_sensor.start()
