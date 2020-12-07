import pyautogui
import time
#minimize
pyautogui.click(1259,12)

for x in range(30):
    for g in range(10):
        pyautogui.click(1275,232)
    #list
    pyautogui.click(1095,552)
    #start price
    time.sleep(3)
    pyautogui.click(1037,666)
    pyautogui.click(1037, 666)
    time.sleep(3)
    pyautogui.typewrite("750")
    #scroll
    for y in range(0, 6):
        pyautogui.click(1279, 677)
    #buynow
    time.sleep(2)
    pyautogui.click(1047, 508)
    pyautogui.typewrite("800")
    pyautogui.click(1054,639)
    time.sleep(5)


