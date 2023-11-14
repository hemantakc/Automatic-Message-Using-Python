import pyautogui
import time
time.sleep(5)
count=0
while count<=150: #This number stands for how many messages you want to send
    pyautogui.typewrite("hello Hem"+str(count)) #"Hello Hem" This is the Message you want to send
    pyautogui.press("enter")
    count=count+1
