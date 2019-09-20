import pygame
from pygame.locals import *
import sys
import json
import time
from threading import Thread
from websocket import create_connection

import unibocv2
import unibomic

SCREEN = Rect(0, 0, 750, 600)   # 画面サイズ
start_time = time.time()
class UniboWs:
    def __init__(self):
        with open("./UniboRoboData.json", "r") as f:
            self.unibo_data = json.load(f)
        self.ws = create_connection("wss://neruneru.higashi.dev/uniHome/ws")
    # uniboからのデータ送信

    def unibo_ws_send(self):
        while True:
            # ここにjsonのフラグを変化させる処理を書きたい
            #print(self.unibo_data)
            send_unibo_data = json.dumps(self.unibo_data)
            self.ws.send(send_unibo_data)
        self.ws.close()
    # uniboやスマホからのデータ受信

    def unibo_ws_recv(self):
        while True:
            pass
        ws.close()

class GetMic():
    def __init__(self):
        pass
class UniboBody(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_name = "img/unibo_face_1.png"
        self.image = pygame.image.load(self.image_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (417, 490)) 
        self.x, self.y = 180, 50
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.rect = Rect(self.x, self.y, self.w, self.h)
    def unibo_animation(self, flgnmb):
        if flgnmb == 1:
            self.image = pygame.image.load("img/unibo_face_1.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (417, 490))
        if flgnmb == 2:
            self.image = pygame.image.load("img/unibo_face_2.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (417, 490))
    def unibo_danceing(self, start_time, dance_time):
        now_time = start_time - dance_time
        if now_time == 0:
            self.image = pygame.image.load("img/dance1_1.png").convert_alpha()
            dance_w = self.image.get_width()
            dance_h = self.image.get_height()
            self.image = pygame.transform.scale(self.image, (int(dance_w * 0.5), int(dance_h * 0.5)))
            self.rect = Rect(self.x - 60, self.y, self.w, self.h)
            return False
        elif now_time == 1:
            self.image = pygame.image.load("img/dance1_2.png").convert_alpha()
            dance_w = self.image.get_width()
            dance_h = self.image.get_height()
            self.image = pygame.transform.scale(self.image, (int(dance_w * 0.5), int(dance_h * 0.5)))
            self.rect = Rect(self.x - 60, self.y, self.w, self.h)
            return False
        elif now_time == 2:
            self.image = pygame.image.load("img/dance2_1.png").convert_alpha()
            dance_w = self.image.get_width()
            dance_h = self.image.get_height()
            self.image = pygame.transform.scale(self.image, (int(dance_w * 0.5), int(dance_h * 0.5)))
            self.rect = Rect(self.x - 60, self.y, self.w, self.h)
            return False
        elif now_time == 3:
            self.image = pygame.image.load("img/dance2_2.png").convert_alpha()
            dance_w = self.image.get_width()
            dance_h = self.image.get_height()
            self.image = pygame.transform.scale(self.image, (int(dance_w * 0.5), int(dance_h * 0.5)))
            self.rect = Rect(self.x - 60, self.y, self.w, self.h)
            return False
        elif now_time == 4:
            self.image = pygame.image.load("img/unibo_face_1.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (417, 490))
            self.rect = Rect(self.x, self.y, self.w, self.h)
            return True

    def update(self, screen):
        if self.image_name == "img/unibo_dance.png":
            pass

class UniboCursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/hand.png").convert_alpha()
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.w / 10), int(self.h / 10))) #200 * 130に画像を縮小
        self.x, self.y = 0, 0
        self.rect = Rect(self.x, self.y, self.w, self.h)
    #カーソル移動に合わせて画像を移動
    def update(self, screen):
            self.x, self.y = pygame.mouse.get_pos()
            self.x -= int(self.image.get_width() / 2)
            self.y -= int(self.image.get_height() / 2)
            self.rect = Rect(self.x, self.y, self.w, self.h)

class UniboEmotion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/hurt.png").convert_alpha()
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x, self.y = -1000, 0
        self.image = pygame.transform.scale(self.image, (int(self.w / 4), int(self.h / 4)))
        self.rect = Rect(self.x, self.y, self.w, self.h)
    #ハートを出現させる
    def put_emotion(self, filename):
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.w / 4), int(self.h / 4)))
        self.x, self.y = 330, 270
        self.rect = Rect(self.x, self.y, self.w, self.h)
    def update(self, screen):
            self.y -= 5
            self.rect = Rect(self.x, self.y, self.w, self.h)
class Greeting():
        words = ""
        isGreeting = False
class FaceRecognition():
        isFaceRecognition = False

# メイン

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN.size)
    pygame.display.set_caption("バーチャルゆにぼ") 
    mouse_move = 0
    unibo_body = UniboBody()
    unibo_cursor = UniboCursor()
    unibo_emotion = UniboEmotion()
    bg = pygame.image.load("img/background.png").convert_alpha()
    bg = pygame.transform.scale(bg, (750, 600))     
    # スプライトグループの作成
    group = pygame.sprite.RenderUpdates()
    # スプライトの追加
    group.add(unibo_body)
    group.add(unibo_cursor)
    group.add(unibo_emotion)
    clock = pygame.time.Clock()
    while (1):
        clock.tick(100)  # フレームレート(100fps)
        #背景を描画
        screen.blit(bg, (0, 0))
        #時間によってゆにぼの顔を変化
        now_time = round(time.time() - start_time)
        isTimeOdd = now_time % 2
        #print(FaceRecognition.isFaceRecognition)
        if Greeting.isGreeting or FaceRecognition.isFaceRecognition:
            unibo_emotion.put_emotion("img/callout.png")
            Greeting.isGreeting = False
        if 1000 <= mouse_move:
            unibo_emotion.put_emotion("img/hurt.png")
            mouse_move = 0
        if isTimeOdd:
            unibo_body.unibo_animation(1)
        else:
            unibo_body.unibo_animation(2)

        group.update(screen)
        group.draw(screen)
        # 画面更新
        pygame.display.update()
        # イベント処理
        for event in pygame.event.get():
            # 終了用のイベント処理
            if pygame.mouse.get_pressed()[0] and pygame.sprite.collide_rect(unibo_body, unibo_cursor):
                mouse_move += (abs(sum(pygame.mouse.get_rel())))
            #if event.type == MOUSEBUTTONDOWN and event.button == 1:
            #    print(unibomic.mic())
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()

def virtual_unibo_mic():
    while True:
        Greeting.isGreeting = unibomic.mic()

def virtual_unibo_face_recognition():
    while True:
        FaceRecognition.isFaceRecognition = unibocv2.face_recognition()
#main()       
ws = UniboWs()
wss = Thread(target=ws.unibo_ws_send)
wsr = Thread(target=ws.unibo_ws_recv)
unibo_main = Thread(target=main)
unibo_time = Thread(target=virtual_unibo_face_recognition)
unibo_mic = Thread(target=virtual_unibo_mic)

wss.start()
wsr.start()
unibo_main.start()
unibo_time.start()
unibo_mic.start()