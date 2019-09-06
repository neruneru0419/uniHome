import RPi.GPIO as GPIO
import time
import json
import disco
import seiden
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
        print(self.unibo_data)
    #uniboからのデータ送信
    def unibo_sensor(self):
        self.unibo_data["head_sensor"] = seiden.seiden()
    def unibo_ws_send(self):
        while True:
            result = json.dumps(self.unibo_data)
            self.ws.send(result)
            time.sleep(60)
        self.ws.close()
    #uniboやスマホからのデータ受信
    def unibo_ws_recv(self):
        while True:
            result = json.loads(self.ws.recv())
            if result["user"] != self.unibo_user:
                print("Received '%s'" % result) 
                if result["human_sensor"]:
                    pass#ここにLED点滅と表情変化の処理を書く
                elif result["head_sensor"]:
                    disco.disco()
                elif result["greeting"]:
                    pass#ここに表情と挨拶の処理を書く
        ws.close()
ws = UniboWs()
unibo_wss = Thread(target=ws.unibo_ws_send)
unibo_wsr = Thread(target=ws.unibo_ws_recv)
sensor = Thread(target=ws.unibo_sensor)

unibo_wss.start()
unibo_wsr.start()
sensor.start()
