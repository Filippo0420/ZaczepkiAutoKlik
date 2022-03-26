import os
import numpy as np
import pyautogui
import cv2
import keyboard
from time import sleep, time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

toFind = cv2.imread('Resources/guzikZaczepki.png')
w = int(toFind.shape[1])
h = int(toFind.shape[0])
center_w = int(w/2)
center_h = int(h/2)

x = 100
y = 100
nowy = False

while True:

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    
    result = cv2.matchTemplate(screenshot, toFind, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    if max_val >= .75:
        cv2.rectangle(screenshot, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 255), 2)
        x = max_loc[0] + center_w
        y = max_loc[1] + center_h
        nowy = True
    else:
        nowy = False
    cv2.imshow('Screen Shot', screenshot)
    cv2.waitKey(1)
    if nowy:
        pyautogui.click(x, y)
    sleep(.10)
    if keyboard.is_pressed('q'):
        break
    

print("Done.")