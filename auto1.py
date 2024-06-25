import pyautogui
import time


def greet(name):
    msg=f"Good Morning ,{name}"
    return msg

gname=['Roman','Sandip','Subham','Bikesh']
for name in gname:
    greeting=greet(name)
    time.sleep(1)
    pyautogui.write(greeting)
    pyautogui.press("enter")


