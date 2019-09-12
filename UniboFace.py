import RPi.GPIO as GPIO
import time

#ダイナミック点灯をする関数
def loop_face(face):
    GPIO.setmode(GPIO.BCM)
    
    PIN_ANO = [16, 4, 5, 11, 7, 12, 18, 19]
    PIN_CAT = [10, 17, 9, 13, 2, 8, 3, 6]
    time_count = 0
    for ano in range(8):
        GPIO.setup(PIN_ANO[ano], GPIO.OUT)
    for cat in range(8):
        GPIO.setup(PIN_CAT[cat], GPIO.OUT)

    normal_face = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                        [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                        [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

    moved_normal_face = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                                [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                                [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                                [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

    child_face = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 1, 1, 0, 0, 1, 1, 0 ],
                        [ 0, 1, 1, 0, 0, 1, 1, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                        [ 0, 0, 1, 1, 1, 1, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

    moved_child_face = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                [ 0, 0, 1, 1, 0, 0, 1, 1 ],
                                [ 0, 0, 1, 1, 0, 0, 1, 1 ],
                                [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                                [ 0, 0, 1, 1, 1, 1, 0, 0 ],
                                [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

    parent_face = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 1, 0, 0, 0, 0, 1, 0 ],
                        [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 1, 1, 1, 1, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

    moved_parent_face = [[ 0, 1, 0, 0, 0, 0, 1, 0 ],
                        [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 1, 1, 1, 1, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ]]
    
    grandparent_face = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 1, 1, 0, 0, 1, 1, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 0, 1, 1, 0, 0, 0 ],
                        [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ]]
    
    moved_grandparent_face = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 1, 1, 0, 0, 1, 1, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                        [ 0, 0, 0, 1, 1, 0, 0, 0 ],
                        [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                        [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

    #カソードのループ
    for cat in range(8):
        GPIO.output(PIN_CAT[cat], False) # LOWに変更
        # アノードのループ
        for ano in range(8):
            #1.5秒ごとに表情を変化
            if face == "normal":
                if time_count % 1500 <= 750:
                    GPIO.output(PIN_ANO[ano], normal_face[cat][ano]) # HIGH or LOW
                else:
                    GPIO.output(PIN_ANO[ano], moved_normal_face[cat][ano]) # HIGH or LOW
            elif face == "child":
                if time_count % 1500 <= 750:
                    GPIO.output(PIN_ANO[ano], child_face[cat][ano]) # HIGH or LOW
                else:
                    GPIO.output(PIN_ANO[ano], moved_child_face[cat][ano]) # HIGH or LOW
            elif face == "parent":
                GPIO.output(PIN_ANO[ano], parent_face[cat][ano]) # HIGH or LOW
            elif face == "grandparent":
                GPIO.output(PIN_ANO[ano], grandparent_face[cat][ano]) # HIGH or LOW
        time.sleep(0.0001) 
        for ano in range(8):
            GPIO.output(PIN_ANO[ano], False) # LOWに戻す
        GPIO.output(PIN_CAT[cat], True) # HIGHに戻す
    time_count += 1
