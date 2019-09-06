import time
import json
import random
from websocket import create_connection
from threading import Thread
#websocket通信のためのクラス
class UniboWs:
    def __init__(self):
        print("hoge")
        self.ws = create_connection("wss://neruneru.higashi.dev/uniHome/ws")
        with open("./UniboRoboData.json", "r") as f:
            self.unibo_data = json.load(f)
        self.unibo_user = "parent"#ユーザーの設定
        self.unibo_data["user"] = self.unibo_user
        print(self.unibo_data)
    #uniboからのデータ送信
    def unibo_ws_send(self):
        while True:
            #ここにjsonのフラグを変化させる処理を書きたい
            self.result = json.dumps(self.unibo_data)
            self.ws.send(self.result)
        self.ws.close()
    #uniboやスマホからのデータ受信
    def unibo_ws_recv(self):
        while True:
            self.result = json.loads(self.ws.recv())
            """
            if result["user"] != self.unibo_user:
                print("Received '%s'" % result) 
                if result["human_sensor"]:
                    pass#ここにLED点滅と表情変化の処理を書く
                elif result["head_sensor"]:
                    pass#ここに表情とdiscoの処理を書く
                elif result["greeting"]:
                    pass#ここに表情と挨拶の処理を書く
            """
        ws.close()
ws = UniboWs()
wss = Thread(target=ws.unibo_ws_send)
wsr = Thread(target=ws.unibo_ws_recv)

wss.start()
wsr.start()
