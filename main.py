import RPi.GPIO as GPIO
import time
import json
from websocket import create_connection
from threading import Thread
from UniboLibrary import *

#Websocket通信のクラス
class UniboWs:
    def __init__(self):
        self.ws = create_connection("wss://neruneru.higashi.dev/uniHome/ws")
        with open("data/UniboRoboData.json", "r") as f:
            self.unibo_data = json.load(f)
        self.unibo_user = "child"#ユーザーの設定
        self.unibo_data["user"] = self.unibo_user
        self.facial_expression = "normal"#表情の設定
    #表情のループ処理
    #表情がノーマルから変わったら、3秒で戻る
    def unibo_face(self):
        while True:
            UniboFace.loop_face(self.facial_expression)
            if self.facial_expression == "normal":
                start_time = time.time()
            else:
                now_time = time.time()
            if 2 <= now_time - start_time:
                self.facial_expression = "normal"
    #頭の静電容量センサーの処理
    #頭を触ったらTrue、触ってないならFalseを返す 
    def unibo_headsensor(self):
        while True:
            self.unibo_data["head_sensor"] = UniboSeiden.seiden()
    #人感センサーの処理
    #人を検知したらTrueを返す
    def unibo_humansensor(self):
        while True:
            self.unibo_data["human_sensor"] = UniboHumanSensor.human_sensor()
    #あいさつの処理
    #おはよう、ただいま、おやすみのいずれかの挨拶を聞いたらTrueを返す
    def unibo_greeting(self):
        while True:
            self.unibo_data["words"] , self.unibo_data["greeting"] = UniboMic.mic()
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
                self.facial_expression = result["user"]
                #静電容量センサーが触られたら、音楽を流しながら踊る
                if result["head_sensor"]:
                    UniboDisco.disco()
                #人感センサーが反応したら、LEDを光らせる
                elif result["human_sensor"]:
                    UniboLED.led_fade()
                #挨拶を聞いたら、挨拶のポーズを取る
                elif result["greeting"]:
                    UniboArm.greeting(result["words"])                    
        self.ws.close()

if __name__ == "__main__":
    ws = UniboWs()

    unibo_wss = Thread(target=ws.unibo_ws_send)
    unibo_wsr = Thread(target=ws.unibo_ws_recv)
    face = Thread(target=ws.unibo_face)
    head_sensor = Thread(target=ws.unibo_headsensor)
    human_sensor = Thread(target=ws.unibo_humansensor)
    mic = Thread(target=ws.unibo_greeting)

    unibo_wss.start()
    unibo_wsr.start()
    face.start()
    head_sensor.start()
    human_sensor.start()
    mic.start()
