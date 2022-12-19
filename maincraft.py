import mouse,keyboard
import time
afkr =False
def r():
    global afkr
    if afkr:
        afkr = False
        print('Афк-рыбалка выключена')
    else:
        afkr = True
        print('Афк-рыбалка включена')
keyboard.add_hotkey('a+f+k',r)
while True:
    if afkr:
        mouse.press('right')
