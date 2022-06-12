import time
import pyautogui

def mock():
    width, height = pyautogui.size()
    pyautogui.moveTo(width*0.2, height*0.1)
    time.sleep(2)
    pyautogui.click()
    pyautogui.moveTo(width*0.5, height*0.5)
    time.sleep(2)
    pyautogui.moveTo(width*0.2, height*0.1)
    time.sleep(2)
    pyautogui.click()
    pyautogui.moveTo(width*0.5, height*0.5)


if _name_ == '_main_':  
    while True:
        mock()
        time.sleep(120)