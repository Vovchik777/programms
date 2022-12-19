import hashlib
import keyboard,mouse
import time
import pyautogui
import io
from PIL import Image, ImageGrab






def h():
    test = ImageGrab.grab([214, 102,1046, 813])
    m = hashlib.md5()
    with io.BytesIO() as memf:
        test.save(memf, 'PNG')
        data = memf.getvalue()
        m.update(data)
    hash = m.hexdigest()
    print(hash)
    o = open('otvets.py','a')
    o.write(f'{str(hash)}\n')
    o.close()
keyboard.add_hotkey('ctrl+p',h())
keyboard.send('ctrl+p')
