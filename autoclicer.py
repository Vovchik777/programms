import time
import mouse,keyboard
iscl = False
def swt_click():
    global iscl
    if iscl:
        iscl = False
        print("Кликер выключен")
    else:
        iscl = True
        print("Кликер включен")
keyboard.add_hotkey('ctrl+alt',swt_click)
while True:
    if iscl:
        mouse.double_click('left')
        #keyboard.send('space')
        time.sleep(0.1)