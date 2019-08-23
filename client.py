import time
import json
import random
from websocket import create_connection
from threading import Thread
class Ws:
    def __init__(self):
        self.ws = create_connection("wss://neruneru.higashi.dev/sampleapp/ws")
        self.unibo_id = random.randint(1, 100000)
        print("userid="+str(self.unibo_id))
    def ws_send(self):
        while True:
            i = input()
            data = {"user": self.unibo_id, "message": i}
            jsn = json.dumps(data)
            self.ws.send(jsn)
        ws.close()
    def ws_recv(self):
        while True:
            result = json.loads(self.ws.recv())
            if result["user"] != self.unibo_id:
                print("Received '%s'" % result["message"]) 
        ws.close()
ws = Ws()
wss = Thread(target=ws.ws_send)
wsr = Thread(target=ws.ws_recv)

wss.start()
wsr.start()
