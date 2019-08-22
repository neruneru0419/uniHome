import time
from websocket import create_connection
from threading import Thread
class Ws:
    def __init__(self):
        self.ws = create_connection("wss://neruneru.higashi.dev/sampleapp/ws")
    def ws_send(self):
        while True:
            i = input()
            self.ws.send(i)
        ws.close()
    def ws_recv(self):
        while True:
            result = self.ws.recv()
            print("Received '%s'" % result) 
        ws.close()
ws = Ws()
wss = Thread(target=ws.ws_send)
wsr = Thread(target=ws.ws_recv)

wss.start()
wsr.start()
