import pyautogui
import time

#pyautogui.moveTo(100,100,duration=1)

#minimize
pyautogui.click(1259,12)

bidX=1099
bidY=625
PlayerX = 395
PlayerY = 372
for q in range(0,5):
    for x in range(0,10):
        for t in range(0,3):
            pyautogui.click(1076,564)
            pyautogui.typewrite("500")
            pyautogui.click(bidX,bidY)
            #if im the same bidder
            pyautogui.click(x=732, y=507)
            pyautogui.click(PlayerX,PlayerY)
            PlayerY+=123
            time.sleep(3)
        for x in range(0, 12):
            pyautogui.click(929, 617)
        PlayerX = 395
        PlayerY = 372
    pyautogui.click(881,650)
