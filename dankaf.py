import time
from threading import Thread
from pyautogui import typewrite, sleep, press
from random import choice, randint

#ctrl+c on terminal to stop the program.

random_sleep = randint(1,6)

def bal():
    typewrite('pls bal')
    press('enter')

def shop_inv():
    number = str(randint(1,6))
    sleep(random_sleep)
    typewrite('pls shop '+ number)
    press('enter')

    number = str(randint(1,6))
    sleep(random_sleep)
    typewrite('pls inv '+ number)
    press('enter')

def dep():
    sleep(random_sleep)
    typewrite('pls dep all')
    press('enter')

def postmemes():
    arr = ['f','r','i','c','k']
    sleep(random_sleep)
    typewrite('pls postmemes')
    press('enter')

    sleep(random_sleep)
    typewrite(choice(arr))
    press('enter')

def trivia():
    arr = ['a','b','c','d']
    sleep(random_sleep)
    typewrite('pls trivia')
    press('enter')
    
    sleep(random_sleep)
    typewrite(choice(arr))
    press('enter')
    
def beg():
    sleep(random_sleep)
    typewrite('pls beg')
    press('enter')

def dig():
    sleep(random_sleep)
    typewrite('pls dig')
    press('enter')

def fish():
    sleep(random_sleep)
    typewrite('pls fish')
    press('enter')

def hunt():
    sleep(random_sleep)
    typewrite('pls hunt')
    press('enter')

def main():
    sec = randint(18,24)
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
        sleep(sec)
        bal()
        
if __name__ == '__main__':
    print("running")
    sleep(5)
    main()
