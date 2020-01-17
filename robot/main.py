import RPi.GPIO as GPIO
import time
import json
import sys
from websocket import create_connection
from threading import Event, Thread
from UniboLibrary import *
send_event, recv_event = Event(), Event()
#Websocket通信のクラス
class UniboWs:
    def __init__(self):
        #self.ws = create_connection("ws://192.168.11.40:8080/uniHome/ws")
        self.ws = create_connection("wss://neruneru.higashi.dev/uniHome/ws")
        UniboJulius.julius()
        with open("data/UniboRoboData.json", "r") as f:
            self.send_data = json.load(f)
        #if sys.argv[1] == "1":
        self.send_data["user"] = "parents"
        #elif sys.argv[1] == "2":
        #    self.send_data["user"] = "parents"
        #elif sys.argv[1] == "3":
        #    self.send_data["user"] = "grand_parents"

        self.unibo_user = self.send_data["user"]
        self.recv_data = self.send_data.copy()
        self.INIT_RECV_DATA = self.send_data
        self.isHumanSensor = False
        time.sleep(1)
    #頭の静電容量センサーの処理
    #頭を触ったらTrue、触ってないならFalseを返す 
    def unibo_headsensor(self):
        while True:
            self.send_data["head_sensor"] = UniboSeiden.seiden()
            #print("1")
            send_event.wait()
            send_event.clear()
    #人感センサーの処理
    #人を検知したらTrueを返す
    def unibo_humansensor(self):
        while True:
            self.send_data["human_sensor"] = UniboHumanSensor.human_sensor()
            print("2")
            send_event.wait()
            send_event.clear()
            if self.isHumanSensor:
                time.sleep(10)
                self.isHumanSensor = False
    #あいさつの処理
    #おはよう、ただいま、おやすみ、おかえりのいずれかの挨拶を聞いたらTrueを返す
    def unibo_greeting(self):
        while True:
            #print(4)
            try:
                print("3")
                if (not self.send_data["greeting"]):
                    self.send_data["words"] , self.send_data["greeting"] = UniboMic.mic()
                    send_event.wait()
                    send_event.clear()
                    #print(self.send_data["words"], self.send_data["greeting"])
            except ConnectionResetError:
                print("にぎりつぶした")
                UniboJulius.julius()
                time.sleep(1)
                self.send_data["words"], self.send_data["greeting"] = UniboMic.mic()
    #転んでいるかの検知
    def unibo_is_fall(self):
        while True:
            self.send_data["isFall"] = False#UniboFall.isfall()
            if self.send_data["isFall"]:
                cnt = 0
                danger = True
                while cnt <= 600:
                    cnt += 1
                    if self.send_data["head_sensor"]:
                        danger = False
                self.send_data["isFall"] = danger
            send_event.wait()
            send_event.clear()
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
                    self.isHumanSensor = True
                elif self.send_data["greeting"]:
                    self.send_data["greeting"] = False
                    self.send_data["words"] = ""
                send_event.set()
                print("送信した")
                #time.sleep(1)
            else:
                send_event.set()
        self.ws.close()
    def unibo_ws_recv(self):
        while True:
            self.recv_data = json.loads(self.ws.recv())
            if (self.recv_data["user"] != self.unibo_user) and (not self.recv_data["isLog"]):
                if self.recv_data["head_sensor"] or self.recv_data["human_sensor"] or self.recv_data["greeting"]:
                    #print(self.recv_data)
                    recv_event.wait()#ゆにぼのアクションが終わるまで待つ
                    self.recv_data = self.INIT_RECV_DATA
                    recv_event.clear()
        self.ws.close()
    def unibo_dance(self):
        self.can_dance = False
        while True:
            if (self.recv_data["user"] != self.unibo_user) and (not self.recv_data["isLog"]):            
                if self.recv_data["head_sensor"]:
                    UniboDisco.dance()
                #挨拶を聞いたら、挨拶のポーズを取る
                if self.recv_data["greeting"]:
                    UniboArm.greeting(self.recv_data["words"])
                self.can_dance = True
                recv_event.wait()
                recv_event.clear()
                
    def unibo_led(self):
        self.can_led = False
        while True:
            if (self.recv_data["user"] != self.unibo_user) and (not self.recv_data["isLog"]):            
                if self.recv_data["human_sensor"]:
                    UniboLED.led_fade()
                if self.recv_data["isFall"]:
                    UniboLED.danger()
                self.can_led = True
                recv_event.wait()#他のアクションが終わるまで待つ
                recv_event.clear()
    def all_recv_event_set(self):
        while True:
            if self.can_dance and self.can_led:
                self.can_dance = False
                self.can_led = False
                self.recv_data = self.INIT_RECV_DATA
                recv_event.set()
            
def main():
    ws = UniboWs()

    unibo_wss = Thread(target=ws.unibo_ws_send)
    unibo_wsr = Thread(target=ws.unibo_ws_recv)
    head_sensor = Thread(target=ws.unibo_headsensor)
    human_sensor = Thread(target=ws.unibo_humansensor)
    greeting = Thread(target=ws.unibo_greeting)
    #fall = Thread(target=ws.unibo_is_fall)
    dance = Thread(target=ws.unibo_dance)
    led = Thread(target=ws.unibo_led)
    recv_set = Thread(target=ws.all_recv_event_set)

    unibo_wss.start()
    unibo_wsr.start()
    head_sensor.start()
    human_sensor.start()
    greeting.start()
    #fall.start()
    dance.start()
    led.start()
    recv_set.start()
if __name__ == "__main__":
    main()
