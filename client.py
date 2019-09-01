import time
import json
import random
from websocket import create_connection
from threading import Thread
#websocket通信のためのクラス
class UniboWs:
    def __init__(self):

        self.ws = create_connection("wss://neruneru.higashi.dev/uniHome/ws")
        with open("./Unibodata.json", "r") as f
            self.unibo_data = json.load(f)
        #ユーザーの設定
        unibo_user = "child"
        self.unibo_data["user"] = unibo_user
    #uniboからのデータ送信
    def unibo_ws_send(self):
        while True:
            #ここにjsonのFalseを変化させる処理を書きたい
            result = json.dumps(self.unibo_data)
            self.ws.send(result)
        ws.close()
    def unibo_ws_recv(self):
        while True:
            result = json.loads(self.ws.recv())
            if result["user"] != self.unibo_user:
                print("Received '%s'" % result["message"]) 
                if result["human_sensor"]:
                    #ここにLED点滅と表情変化の処理を書く
                elif result["head_sensor"]:
                    #ここに表情とdiscoの処理を書く
                elif result["greeting"]:
                    #ここに表情と挨拶の処理を書く
        ws.close()
ws = UniboWs()
wss = Thread(target=ws.unibo_ws_send)
wsr = Thread(target=ws.unibo_ws_recv)

wss.start()
wsr.start()
