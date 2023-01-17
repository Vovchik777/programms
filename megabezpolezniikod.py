import time
import mouse,keyboard
import subprocess

import win32gui,pyautogui

# mouse.click('right')
# subprocess.Popen('calc')
# time.sleep(0.2)
# print(mouse.get_position())
# #280, 104
# #494, 176
# mouse.drag(280, 104,494, 176,duration=0.3)
# keyboard.send('ctrl+/')
# import time
# time.sleep(5)
#keyboard.send('ctrl+z')
c = input('Пример(без пробелов):')
keyboard.send('win')
mouse.move(29, 948,absolute=0.1)
keyboard.write('калькулятор',delay=0.1)
mouse.move(49, 520,absolute=0.1)
mouse.double_click('left')
time.sleep(0.5)
keyboard.write(c,delay=0.01)
keyboard.send('enter')
hwnd = win32gui.FindWindow(None, 'Калькулятор')
rect = win32gui.GetWindowRect(hwnd)
kord = rect[0:2]
kord2 = kord[1]+70
kord3 = kord[0]+30
mouse.move(kord3,kord2,duration=0.1)
mouse.click('right')
mouse.move(kord3+5,kord2+5,duration=0.1)
mouse.click('left')
keyboard.send('alt+F4')
time.sleep(1.5)
mouse.move(1179, 2)
mouse.click('left')
# mouse.move(559, 753,duration=0.1)
c = pyautogui.locateOnScreen('etr.png')
time.sleep(1.5)
pyautogui.click(c)
time.sleep(0.5)
keyboard.send('enter')
keyboard.send('UP')
# keyboard.send('end')
keyboard.press('delete')
time.sleep(1)
keyboard.release('delete')
keyboard.send('ctrl+v')
time.sleep(5)
keyboard.send('alt+F4')
time.sleep(1)
keyboard.send('enter')
# hwnd = win32gui.FindWindow(None,'Блокнот')
# print(hwnd)
# k = win32gui.FindWindowEx(hwnd,0,'Button1',None)
# print(k)
# rect = win32gui.GetWindowRect(k)
#449, 381, 815, 542
# mouse.move(rect[0:2],duration=0.1)
# mouse.click('left')

# mouse.double_click('left')

# keyboard.send('ctrl+c')
#49, 520