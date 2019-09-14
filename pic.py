import pygame
from pygame.locals import *
import sys

SCREEN = Rect(0, 0, 750, 600)   # 画面サイズ

# 職業のクラス
class UniboBody(pygame.sprite.Sprite):
    # スプライトを作成(画像ファイル名, 位置(x, y), 速さ(vx, vy), 回転angle)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/unibo_noface_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (417, 490)) #200 * 130に画像を縮小
        x, y = 180, 50
        w = self.image.get_width()
        h = self.image.get_height()
        self.rect = Rect(x, y, w, h)
    def unibo_update(self):
        self.image = pygame.image.load("img/face_normal_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (417, 490))

class UniboFace(pygame.sprite.Sprite):
    # スプライトを作成(画像ファイル名, 位置(x, y), 速さ(vx, vy), 回転angle)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/face_normal_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (121, 115)) #200 * 130に画像を縮小
        x, y = 328, 215
        w = self.image.get_width()
        h = self.image.get_height()
        self.rect = Rect(x, y, w, h)
    def unibo_update(self, flgnmb):
        if flgnmb == 1:
            self.image = pygame.image.load("img/face_normal_2.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (121, 115))
        if flgnmb == 2:
            self.image = pygame.image.load("img/face_normal_1.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (121, 115))

        
# メイン
cnt = 0
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN.size)#, FULLSCREEN)
    unibo_body = UniboBody()
    unibo_face = UniboFace()
    bg = pygame.image.load("img/background.png").convert_alpha()
    bg = pygame.transform.scale(bg, (750, 600))     
    # スプライトグループの作成
    group = pygame.sprite.RenderUpdates()
    # スプライトの追加
    group.add(unibo_body)
    group.add(unibo_face)

    clock = pygame.time.Clock()
    cnt = 0
    while (1):
        clock.tick(60)  # フレームレート(30fps)
        screen.fill((0, 20, 0)) # 画面の背景色
        #背景を描画
        screen.blit(bg, (0, 0))
        if cnt == 50:
            unibo_face.unibo_update(1)
        elif cnt == 100:
            unibo_face.unibo_update(2)
            cnt = 0
        group.update(screen)
        group.draw(screen)
        # 画面更新
        pygame.display.update()
        cnt += 1
        # イベント処理
        for event in pygame.event.get():
            # 終了用のイベント処理
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
        


if __name__ == "__main__":
    main()