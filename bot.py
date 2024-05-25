import pyautogui
import pyscreeze
import time
import random

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False


def chrome_open():
    x,y = pyautogui.locateCenterOnScreen("images/chrome.png",confidence =0.9)
    pyautogui.click(x,y)

def select_2048():
    x,y = pyautogui.locateCenterOnScreen("images/2048.png",confidence =0.9)
    pyautogui.click(x,y+268)

def start():
    x,y = pyautogui.locateCenterOnScreen("images/start.png",confidence =0.9)
    pyautogui.click(x,y)

def gain():
    x,y = pyautogui.locateCenterOnScreen("images/gain.png",confidence =0.9)
    pyautogui.click(x,y) 

def play():

    pixel = pyautogui.pixel(981,261)

    while 1:
        if pyautogui.pixel(981,261) != pixel:
            break

        arrow = random.choice(['down','up','left','right'])
        pyautogui.press(arrow)
    
    

if __name__ == "__main__":
    chrome_open()
    time.sleep(1)
    select_2048()
    time.sleep(4)
    start()
    time.sleep(4)
    play()
    time.sleep(1)
    gain()



