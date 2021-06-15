import time
from threading import Thread
from pyautogui import typewrite, sleep, press
from random import choice, randint

#ctrl+c on terminal to stop the program.
def bal():
    typewrite('pls bal')
    press('enter')

def shop_inv():
    number = str(randint(1,6))
    sleep(3)
    typewrite('pls shop '+ number)
    press('enter')

    number = str(randint(1,6))
    sleep(3)
    typewrite('pls inv '+ number)
    press('enter')

def dep():
    sleep(2)
    typewrite('pls dep all')
    press('enter')

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
    sleep(2)
    typewrite('pls trivia')
    press('enter')
    
    sleep(3)
    typewrite(choice(arr))
    press('enter')
    
def beg():
    sleep(2)
    typewrite('pls beg')
    press('enter')

def dig():
    sleep(2)
    typewrite('pls dig')
    press('enter')

def fish():
    sleep(2)
    typewrite('pls fish')
    press('enter')

def hunt():
    sleep(2)
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
        postmemes()
        dep()
        shop_inv()
        sleep(15)
        bal()
        
if __name__ == '__main__':
    print("running")
    sleep(5)
    main()
