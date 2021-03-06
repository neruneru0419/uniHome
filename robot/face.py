import RPi.GPIO as GPIO
import time
import json
from websocket import create_connection
from threading import Thread
from UniboLibrary import *

#Websocket通信のクラス
class UniboWs:
    def __init__(self):
        #self.ws = create_connection("ws://192.168.11.40:8080/uniHome/ws")
        self.ws = create_connection("wss://neruneru.higashi.dev/uniHome/ws")
        with open("data/UniboRoboData.json", "r") as f:
            self.unibo_data = json.load(f)
        self.unibo_user = self.unibo_data["user"]
        self.facial_expression = "normal"#表情の設定
        self.time_count = 0
    #表情のループ処理
    #表情がノーマルから変わったら、3秒で戻る
    def unibo_face(self):
        while True:
            #print(1)
            UniboFace.loop_face(self.facial_expression, self.time_count)
            if self.facial_expression == "normal":
                start_time = time.time()
            else:
                now_time = time.time()
                if 7 <= now_time - start_time:
                    self.facial_expression = "normal"
            self.time_count += 1
    #uniboやスマホからのデータ受信
    def unibo_ws_recv(self):
        while True:
            #print(6)
            recv_data = json.loads(self.ws.recv())
            print(recv_data)
            print(self.unibo_user)
            if recv_data["head_sensor"] or recv_data["human_sensor"] or recv_data["greeting"]:
                if recv_data["user"] != self.unibo_user:
                    self.facial_expression = recv_data["user"]
                    recv_data["user"] = self.unibo_user
            
        self.ws.close()

if __name__ == "__main__":
    ws = UniboWs()

    unibo_wsr = Thread(target=ws.unibo_ws_recv)
    face = Thread(target=ws.unibo_face)

    unibo_wsr.start()
    face.start()
