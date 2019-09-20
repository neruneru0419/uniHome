import time
import json
import random
from websocket import create_connection
from threading import Thread
# websocket通信のためのクラス


class UniboWs:
    def __init__(self):
        print("hoge")
        self.ws = create_connection("wss://neruneru.higashi.dev/uniHome/ws")
    # uniboからのデータ送信

    def unibo_ws_send(self):
        while True:
            # ここにjsonのフラグを変化させる処理を書きたい
            self.ws.send("hoge")
        self.ws.close()
    # uniboやスマホからのデータ受信

    def unibo_ws_recv(self):
        while True:
            pass
        ws.close()


ws = UniboWs()
wss = Thread(target=ws.unibo_ws_send)
wsr = Thread(target=ws.unibo_ws_recv)

wss.start()
wsr.start()
