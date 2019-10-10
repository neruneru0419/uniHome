import RPi.GPIO as GPIO
import time
import json
from websocket import create_connection
from threading import Thread
from UniboLibrary import *

#Websocket通信のクラス
class UniboWs:
    def __init__(self):
        self.ws = create_connection("ws://192.168.11.2:8080/uniHome/ws")
        with open("data/UniboRoboData.json", "r") as f:
            self.unibo_data = json.load(f)
        self.unibo_user = self.unibo_data["user"]
        self.facial_expression = "normal"#表情の設定
        self.time_count = 0
        self.result = self.unibo_data
    #頭の静電容量センサーの処理
    #頭を触ったらTrue、触ってないならFalseを返す 
    def unibo_headsensor(self):
        while True:
            #print(2)
            if (not self.unibo_data["head_sensor"]):
                self.unibo_data["head_sensor"] = UniboSeiden.seiden()
    #人感センサーの処理
    #人を検知したらTrueを返す
    def unibo_humansensor(self):
        while True:
            #print(3)
            if (not self.unibo_data["human_sensor"]):
                self.unibo_data["human_sensor"] = UniboHumanSensor.human_sensor()
    #あいさつの処理
    #おはよう、ただいま、おやすみのいずれかの挨拶を聞いたらTrueを返す
    def unibo_greeting(self):
        while True:
            #print(4)
            if(not self.unibo_data["greeting"]):
                self.unibo_data["words"] , self.unibo_data["greeting"] = UniboMic.mic()
    #uniboからのデータ送信
    def unibo_ws_send(self):
        while True:
            #print(5)
            result = json.dumps(self.unibo_data)
            self.ws.send(result)
            if self.unibo_data["head_sensor"]:
                self.unibo_data["head_sensor"] = False
            elif self.unibo_data["human_sensor"]:
                self.unibo_data["human_sensor"] = False
            elif self.unibo_data["greeting"]:
                self.unibo_data["greeting"] = False
            time.sleep(1)
        self.ws.close()
    #uniboやスマホからのデータ受信
    def unibo_ws_recv(self):
        while True:
            if self.result["head_sensor"] or self.result["human_sensor"] or self.result["greeting"]:
                pass
            else:
                self.result = json.loads(self.ws.recv())
        self.ws.close()
    def unibo_dance(self):
        while True:
            if self.result["user"] != self.unibo_user:
                #静電容量センサーが触られたら、音楽を流しながら踊る
                if self.result["head_sensor"]:
                    UniboDisco.disco()
                    self.result["head_sensor"] = False
                    time.sleep(10)
                #挨拶を聞いたら、挨拶のポーズを取る
                elif self.result["greeting"]:
                    UniboArm.greeting(result["words"])
                    self.result["greeting"] = False
    def unibo_led(self):
        while True:
            if self.result["user"] != self.unibo_user:
                if self.result["human_sensor"]:
                    UniboLED.led_fade()
                    self.result["human_sensor"] = False
            

if __name__ == "__main__":
    ws = UniboWs()

    unibo_wss = Thread(target=ws.unibo_ws_send)
    unibo_wsr = Thread(target=ws.unibo_ws_recv)
    head_sensor = Thread(target=ws.unibo_headsensor)
    human_sensor = Thread(target=ws.unibo_humansensor)
    mic = Thread(target=ws.unibo_greeting)
    dance = Thread(target=ws.unibo_dance)
    led = Thread(target=ws.unibo_led)

    unibo_wss.start()
    unibo_wsr.start()
    head_sensor.start()
    human_sensor.start()
    mic.start()
    dance.start()
    led.start()
