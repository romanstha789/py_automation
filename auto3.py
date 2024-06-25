import pyautogui
import time

#To open co-pilot
pyautogui.moveTo(1880,1050,duration=1)
pyautogui.click()

pyautogui.hotkey('ctrl','s')
pyautogui.press('enter')
pyautogui.write('hello')

pyautogui.press('win')
time.sleep(0.1)
pyautogui.write('edge',interval=0.05)
pyautogui.press('enter')
time.sleep(0.2)
pyautogui.write('https://www.youtube.com/')
pyautogui.press('enter')

time.sleep(0.3)
pyautogui.hotkey('ctrl','t')
time.sleep(2)
pyautogui.write('https://mail.google.com//')
time.sleep(2)
pyautogui.press('enter')

pyautogui.alert('All tabs opened')


