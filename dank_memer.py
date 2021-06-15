import time
from threading import Thread
from pyautogui import typewrite, sleep, press
from random import choice

#ctrl+c on terminal to stop the program.

def postmemes():
    arr = ['f','r','i','c','k']
    sleep(3)
    typewrite('pls postmemes')
    press('enter')

    sleep(1)
    typewrite(choice(arr))
    press('enter')

def trivia():
    arr = ['a','b','c','d']
    sleep(3)
    typewrite('pls trivia')
    press('enter')
    
    sleep(1)
    typewrite(choice(arr))
    press('enter')
    
def beg():
    sleep(3)
    typewrite('pls beg')
    press('enter')

def dig():
    sleep(3)
    typewrite('pls dig')
    press('enter')

def fish():
    sleep(3)
    typewrite('pls fish')
    press('enter')

def hunt():
    sleep(3)
    typewrite('pls hunt')
    press('enter')

def main():
    x = 1
    while x:
        trivia()
        beg()
        dig()
        fish()
        hunt()
        sleep(40)
        postmemes()
        
if __name__ == '__main__':
    print("running")
    sleep(5)
    main()
