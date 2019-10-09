#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import string


host = 'localhost'   # Raspberry PiのIPアドレス
port = 10500         # juliusの待ち受けポート

# パソコンからTCP/IPで、自分PCのjuliusサーバに接続
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

data = ""
while True:

    # "/RECOGOUT"を受信するまで、一回分の音声データを全部読み込む。
    while (string.find(data, "\n.") == -1):
        data = data + sock.recv(1024)

    # 音声XMLデータから、<WORD>を抽出して音声テキスト文に連結する。
    strTemp = ""
    for line in data.split('\n'):
        index = line.find('WORD="')

        if index != -1:
            line = line[index + 6:line.find('"', index + 6)]
            if line != "[s]":
                strTemp = strTemp + line

    if strTemp != "":
        print("結果:" + strTemp)
    data = ""
