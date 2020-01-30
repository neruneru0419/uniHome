import pygame
from pygame.locals import *
import sys
import json
import time
from threading import Thread
from websocket import create_connection
from UniboLibrary import *

SCREEN = Rect(0, 0, 750, 600)   # 画面サイズ
start_time = time.time()


class UniboData:
    def __init__(self):
        self.ws = create_connection("ws://192.168.11.40:8080/uniHome/ws")
        unibojulius.julius()
        time.sleep(1)
        with open("data/UniboVirtualData.json", "r") as f:
            self.unibo_data = json.load(f)
            self.action = self.unibo_data

    class UniboBody(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image_name = "img/face/unibo_face_1.png"
            self.image = pygame.image.load(self.image_name).convert_alpha()
            self.image = pygame.transform.scale(self.image, (417, 490))
            self.isAnime = True
            self.x, self.y = 180, 50
            self.w = self.image.get_width()
            self.h = self.image.get_height()
            self.rect = Rect(self.x, self.y, self.w, self.h)

        def unibo_animation(self, flgnmb):
            if flgnmb:
                self.image = pygame.image.load(
                    "img/face/unibo_face_1.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (417, 490))
            else:
                self.image = pygame.image.load(
                    "img/face/unibo_face_2.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (417, 490))

        def unibo_danceing(self, time_cnt, user):
            print(time_cnt)
            flg = False
            if user == "child":
                dance1 = "dance_child_1.png"
                dance2 = "dance_child_2.png"
            elif user == "parents":
                dance1 = "dance_parents_1.png"
                dance2 = "dance_parents_2.png"
            elif user == "grand_parents":
                dance1 = "dance_grand_parents_1.png"
                dance2 = "dance_grand_parents_2.png"

            if time_cnt == 1:
                self.image = pygame.image.load(
                    "img/dance/" + dance1).convert_alpha()
                dance_w = self.image.get_width()
                dance_h = self.image.get_height()
                self.image = pygame.transform.scale(
                    self.image, (int(dance_w * 0.5), int(dance_h * 0.5)))
                self.rect = Rect(self.x - 60, self.y, self.w, self.h)
                flg = False
            elif time_cnt == 41:
                self.image = pygame.image.load(
                    "img/dance/" + dance2).convert_alpha()
                dance_w = self.image.get_width()
                dance_h = self.image.get_height()
                self.image = pygame.transform.scale(
                    self.image, (int(dance_w * 0.5), int(dance_h * 0.5)))
                self.rect = Rect(self.x - 60, self.y, self.w, self.h)
                flg = False
            elif time_cnt == 81:
                self.image = pygame.image.load(
                    "img/dance/" + dance1).convert_alpha()
                dance_w = self.image.get_width()
                dance_h = self.image.get_height()
                self.image = pygame.transform.scale(
                    self.image, (int(dance_w * 0.5), int(dance_h * 0.5)))
                self.image = pygame.transform.flip(self.image, True, False)
                self.rect = Rect(self.x - 60, self.y, self.w, self.h)
                flg = False
            elif time_cnt == 121:
                self.image = pygame.image.load(
                    "img/dance/" + dance2).convert_alpha()
                dance_w = self.image.get_width()
                dance_h = self.image.get_height()
                self.image = pygame.transform.scale(
                    self.image, (int(dance_w * 0.5), int(dance_h * 0.5)))
                self.image = pygame.transform.flip(self.image, True, False)
                self.rect = Rect(self.x - 60, self.y, self.w, self.h)
                flg = False
            elif time_cnt == 161:
                self.image = pygame.image.load(
                    "img/face/unibo_face_1.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (417, 490))
                self.rect = Rect(self.x, self.y, self.w, self.h)
                flg = True
            return flg
        def unibo_posing(self, time_cnt, user, greeting_word):
            flg = False
            if greeting_word == "おはよう":
                if user == "child":
                    greeting = "goodmorning_child.png"
                elif user == "parents":
                    greeting = "goodmorning_parents.png"
                elif user == "grand_parents":
                    greeting = "goodmorning_grand_parents.png"
            elif greeting_word == "おやすみ":
                if user == "child":
                    greeting = "goodnight_child.png"
                elif user == "parents":
                    greeting = "goodnight_parents.png"
                elif user == "grand_parents":
                    greeting = "goodnight_grand_parents.png"
            if greeting_word == "ただいま":
                if user == "child":
                    greeting = "welcomehome_child.png"
                elif user == "parents":
                    greeting = "welcomehome_parents.png"
                elif user == "grand_parents":
                    greeting = "welcomehome_grand_parents.png"

            if time_cnt == 1:
                self.image = pygame.image.load(
                    "img/pause/" + greeting).convert_alpha()
                dance_w = self.image.get_width()
                dance_h = self.image.get_height()
                self.image = pygame.transform.scale(
                    self.image, (int(dance_w * 0.5), int(dance_h * 0.5)))
                self.rect = Rect(self.x - 60, self.y, self.w, self.h)
                flg = False
            elif time_cnt == 101:
                self.image = pygame.image.load(
                    "img/pause/" + greeting).convert_alpha()
                dance_w = self.image.get_width()
                dance_h = self.image.get_height()
                self.image = pygame.transform.scale(
                    self.image, (int(dance_w * 0.5), int(dance_h * 0.45)))
                self.rect = Rect(self.x - 60, self.y + 50, self.w, self.h)
                flg = False
            elif time_cnt == 201:
                self.image = pygame.image.load(
                    "img/pause/" + greeting).convert_alpha()
                dance_w = self.image.get_width()
                dance_h = self.image.get_height()
                self.image = pygame.transform.scale(
                    self.image, (int(dance_w * 0.5), int(dance_h * 0.5)))
                self.rect = Rect(self.x - 60, self.y, self.w, self.h)
                flg = False
            elif time_cnt >= 301:
                self.image = pygame.image.load(
                    "img/face/unibo_face_1.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (417, 490))
                self.rect = Rect(self.x, self.y, self.w, self.h)
                flg = True
            return flg
        def unibo_led_light(self, time_cnt, user):
            flg = False
            if user == "child":
                light1 = "unibo_child_face.png"
                light2 = "unibo_light_child_face.png"
            elif user == "parents":
                light1 = "unibo_parents_face.png"
                light2 = "unibo_light_parents_face.png"
            elif user == "grand_parents":
                light1 = "unibo_grand_parents_face.png"
                light2 = "unibo_light_grand_parents_face.png"
            if time_cnt == 1 or time_cnt == 201:
                self.image = pygame.image.load(
                    "img/face/" + light1).convert_alpha()
                dance_w = self.image.get_width()
                dance_h = self.image.get_height()
                self.image = pygame.transform.scale(
                    self.image, (int(dance_w * 0.5), int(dance_h * 0.5)))
                self.rect = Rect(self.x, self.y, self.w, self.h)
                flg = False
            elif time_cnt == 101 or time_cnt == 301:
                self.image = pygame.image.load(
                    "img/face/" + light2).convert_alpha()
                dance_w = self.image.get_width()
                dance_h = self.image.get_height()
                self.image = pygame.transform.scale(
                    self.image, (int(dance_w * 0.5), int(dance_h * 0.5)))
                self.rect = Rect(self.x, self.y, self.w, self.h)
                flg = False
            elif time_cnt == 401:
                self.image = pygame.image.load(
                    "img/face/" + light1).convert_alpha()
                self.image = pygame.transform.scale(self.image, (417, 490))
                self.rect = Rect(self.x, self.y, self.w, self.h)
                flg = True
            return flg
    class UniboCursor(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("img/hand.png").convert_alpha()
            self.w = self.image.get_width()
            self.h = self.image.get_height()
            self.image = pygame.transform.scale(
                self.image, (int(self.w / 10), int(self.h / 10)))
            self.x, self.y = 0, 0
            self.rect = Rect(self.x, self.y, self.w, self.h)

        # カーソル移動に合わせて画像を移動
        def update(self, screen):
            self.x, self.y = pygame.mouse.get_pos()
            self.x -= int(self.image.get_width() / 2)
            self.y -= int(self.image.get_height() / 2)
            self.rect = Rect(self.x, self.y, self.w, self.h)

    class UniboEmotion(pygame.sprite.Sprite):
        def __init__(self, filename):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(filename).convert_alpha()
            self.w = self.image.get_width()
            self.h = self.image.get_height()
            self.x, self.y = -1000, 0
            self.image = pygame.transform.scale(
                self.image, (int(self.w / 4), int(self.h / 4)))
            self.rect = Rect(self.x, self.y, self.w, self.h)

        # ハートやメッセージアイコンを出現させる
        def put_emotion(self, filename):
            self.image = pygame.image.load(filename).convert_alpha()
            self.image = pygame.transform.scale(
                self.image, (int(self.w / 4), int(self.h / 4)))
            self.x, self.y = 330, 270
            self.rect = Rect(self.x, self.y, self.w, self.h)

        def update(self, screen):
            self.y -= 10
            if self.y == 0:
                self.x = -1000
            self.rect = Rect(self.x, self.y, self.w, self.h)

    def desktop(self):
        pygame.init()
        screen = pygame.display.set_mode(SCREEN.size)
        pygame.display.set_caption("バーチャルゆにぼ")

        self.unibo_body = self.UniboBody()
        self.unibo_cursor = self.UniboCursor()
        self.unibo_hurt = self.UniboEmotion("img/hurt.png")
        self.unibo_message = self.UniboEmotion("img/callout.png")
        mouse_move = 0
        time_cnt = 0
        bg = pygame.image.load("img/background.png").convert_alpha()
        bg = pygame.transform.scale(bg, (750, 600))

        group = pygame.sprite.RenderUpdates()

        group.add(self.unibo_body)
        group.add(self.unibo_cursor)
        group.add(self.unibo_hurt)
        group.add(self.unibo_message)
        clock = pygame.time.Clock()
        while (1):
            clock.tick(100)
            # 背景を描画
            screen.blit(bg, (0, 0))
            now_time = round(time.time() - start_time)
            # アクションに応じてリクエストを送る

            if self.unibo_data["greeting"]:
                self.unibo_message.put_emotion("img/callout.png")
            if 1000 <= mouse_move:
                self.unibo_data["head_sensor"] = True
                self.unibo_hurt.put_emotion("img/hurt.png")
                mouse_move = 0
            
            if self.unibo_body.isAnime:
                time_cnt = 0
                self.unibo_body.unibo_animation(now_time % 2)
            else:
                if self.action["head_sensor"]:
                    self.unibo_body.isAnime = self.unibo_body.unibo_danceing(
                        time_cnt, self.action["user"])
                elif self.action["human_sensor"]:
                    self.unibo_body.isAnime = self.unibo_body.unibo_led_light(
                        time_cnt, self.action["user"])
                elif self.action["greeting"]:
                    self.unibo_body.isAnime = self.unibo_body.unibo_posing(
                        time_cnt, self.action["user"], self.action["words"])
            time_cnt += 1
            group.update(screen)
            group.draw(screen)
            # 画面更新
            pygame.display.update()
            # イベント処理
            for event in pygame.event.get():
                # 終了用のイベント処理
                if pygame.mouse.get_pressed()[0] and pygame.sprite.collide_rect(self.unibo_body, self.unibo_cursor):
                    mouse_move += (abs(sum(pygame.mouse.get_rel())))
                if event.type == QUIT:          # 閉じるボタンが押されたとき
                    pygame.quit()
                    sys.exit()

    def virtual_unibo_mic(self):
        while True:
            try:
                self.unibo_data["words"], self.unibo_data["greeting"] = unibomic.mic()
                print(self.unibo_data["words"], self.unibo_data["greeting"])
            except ConnectionResetError:
                unibojulius.julius()
                time.sleep(1)
                self.unibo_data["words"], self.unibo_data["greeting"] = unibomic.mic()
            

    def virtual_unibo_face_recognition(self):
        while True:
            self.unibo_data["human_sensor"] = unibocv2.face_recognition()
            if self.unibo_data["human_sensor"]:
                time.sleep(60)

    def unibo_ws_send(self):
        while True:
            send_unibo_data = json.dumps(self.unibo_data)
            self.ws.send(send_unibo_data)
            if self.unibo_data["head_sensor"]:
                self.unibo_data["head_sensor"] = False
            if self.unibo_data["greeting"]:
                self.unibo_data["greeting"] = False
            if self.unibo_data["human_sensor"]:
                self.unibo_data["human_sensor"] = False
            time.sleep(1)
        self.ws.close()
    # uniboやスマホからのデータ受信

    def unibo_ws_recv(self):
        while True:
            result = json.loads(self.ws.recv())
            if result["user"] != self.unibo_data["user"]:
                if result["head_sensor"]:
                    self.action = result.copy()
                    self.unibo_body.isAnime = False
                    result["head_sensor"] = False

                elif result["human_sensor"]:
                    self.action = result.copy()
                    self.unibo_body.isAnime = False
                    result["human_sensor"] = False

                elif result["greeting"]:
                    self.action = result.copy()
                    self.unibo_body.isAnime = False
                    result["greeting"] = False
        self.ws.close()


ws = UniboData()
wss = Thread(target=ws.unibo_ws_send)
wsr = Thread(target=ws.unibo_ws_recv)
unibo_desktop = Thread(target=ws.desktop)
unibo_face_recognition = Thread(target=ws.virtual_unibo_face_recognition)
unibo_mic = Thread(target=ws.virtual_unibo_mic)

wss.start()
wsr.start()
unibo_desktop.start()
unibo_face_recognition.start()
unibo_mic.start()
