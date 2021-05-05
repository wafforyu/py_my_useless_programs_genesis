import time
from threading import Thread
import pyautogui

#ctrl+c on terminal to stop the program.
def idle_rpg():
    def adventure():
        pyautogui.typewrite("$adventure 1") #just change adventure
        pyautogui.press("enter")

    def status():
        pyautogui.typewrite("$status")
        pyautogui.press("enter")

    time.sleep(5)
    x = 1 
    while (x):
        adventure()
        status()
        time.sleep(3610) #1hour = 3600seconds, added 10 for delay
        status()
    
def pokemon():
    def route():
            pyautogui.typewrite(".route 6") #change route number
            pyautogui.press('enter')
            time.sleep(6) #delay

    def leech_seed():
        pyautogui.typewrite("3")
        pyautogui.press('enter')
        time.sleep(6)

    def tackle():
        pyautogui.typewrite("1")
        pyautogui.press('enter')
        time.sleep(6)

    def vine_whip():
        pyautogui.typewrite("4")
        pyautogui.press('enter')
        time.sleep(6)

    time.sleep(10)
    x = 1 
    while (x):
        route() #route 
        for i in range(0,2): #number of times you attack
            vine_whip()


if __name__ == '__main__':
    Thread(target = idle_rpg).start()
    Thread(target = pokemon).start()