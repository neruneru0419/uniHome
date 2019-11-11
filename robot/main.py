import RPi.GPIO as GPIO
import time
import json
import sys
from websocket import create_connection
from threading import Thread
from UniboLibrary import *
#Websocket通信のクラス
class UniboWs:
    def __init__(self):
        self.ws = create_connection("ws://192.168.11.40:8080/uniHome/ws")
        UniboJulius.julius()
        with open("data/UniboRoboData.json", "r") as f:
            self.send_data = json.load(f)
        if sys.argv[1] == "1":
            self.send_data["user"] = "child"
        elif sys.argv[1] == "2":
            self.send_data["user"] = "parents"
        elif sys.argv[1] == "3":
            self.send_data["user"] = "grand_parents"
        self.unibo_user = self.send_data["user"]
        self.facial_expression = "normal"#表情の設定
        self.time_count = 0
        self.recv_data = self.send_data.copy()
        time.sleep(1)
    #頭の静電容量センサーの処理
    #頭を触ったらTrue、触ってないならFalseを返す 
    def unibo_headsensor(self):
        while True:
            #print(2)
            if (not self.send_data["head_sensor"]):
                self.send_data["head_sensor"] = UniboSeiden.seiden()
    #人感センサーの処理
    #人を検知したらTrueを返す
    def unibo_humansensor(self):
        while True:
            #print(3)
            if (not self.send_data["human_sensor"]):
                self.send_data["human_sensor"] = UniboHumanSensor.human_sensor()
    #あいさつの処理
    #おはよう、ただいま、おやすみ、おかえりのいずれかの挨拶を聞いたらTrueを返す
    def unibo_greeting(self):
        while True:
            #print(4)
            try:
                if (not self.send_data["greeting"]):
                    self.send_data["words"] , self.send_data["greeting"] = UniboMic.mic()
                    print(self.send_data["words"], self.send_data["greeting"])
            except ConnectionResetError:
                print("にぎりつぶした")
                UniboJulius.julius()
                time.sleep(1)
                self.send_data["words"], self.send_data["greeting"] = UniboMic.mic()
    #uniboからのデータ送信
    def unibo_ws_send(self):
        while True:
            if self.send_data["head_sensor"] or self.send_data["human_sensor"] or self.send_data["greeting"]:
                str_send_data = json.dumps(self.send_data)
                print(self.send_data)
                self.ws.send(str_send_data)
                if self.send_data["head_sensor"]:
                    self.send_data["head_sensor"] = False
                elif self.send_data["human_sensor"]:
                    self.send_data["human_sensor"] = False
                elif self.send_data["greeting"]:
                    self.send_data["greeting"] = False
                    self.send_data["words"] = ""
                time.sleep(0.1)
        self.ws.close()
    def unibo_ws_recv(self):
        while True:
            self.recv_data = json.loads(self.ws.recv())
        self.ws.close()
    def unibo_dance(self):
        while True:
            if self.recv_data["user"] != self.unibo_user:
                if self.recv_data["head_sensor"]:
                    UniboDisco.disco()
                    self.recv_data["head_sensor"] = False
                    self.recv_data["user"] = self.unibo_user
                #挨拶を聞いたら、挨拶のポーズを取る
                elif self.recv_data["greeting"]:
                    UniboArm.greeting(self.recv_data["words"])
                    self.recv_data["greeting"] = False
                    self.recv_data["words"] = ""
                    self.recv_data["user"] = self.unibo_user
    def unibo_led(self):
        while True:
            if self.recv_data["user"] != self.unibo_user:
                if self.recv_data["human_sensor"]:
                    UniboLED.led_fade()
                    self.recv_data["human_sensor"] = False
                    self.recv_data["user"] = self.unibo_user
            

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