import time
#from threading import Thread
from pyautogui import typewrite, sleep, press
from random import choice, randint, shuffle

#ctrl+c on terminal to stop the program.

def memey():
    arr = ['4chan', 'antiantjoke', 'blacktwitter','chucknorris','comics','discordmeme','joke','meirl','prequel','pun','sequel']
    typewrite('pls ' + choice(arr))
    sleep(2)
    press('enter')

def bal():
    typewrite('pls bal')
    press('enter')

def shop_inv():
    random_sleep = randint(2,6)
    number = str(randint(2,5))
    typewrite('pls shop '+ number)
    sleep(random_sleep)
    press('enter')

    number = str(randint(2,6))
    typewrite('pls inv '+ number)
    sleep(random_sleep)
    press('enter')

def dep():
    random_sleep = randint(2,6)
    typewrite('pls dep all')
    sleep(random_sleep)
    press('enter')

def postmemes():
    random_sleep = randint(2,6)
    arr = ['f','r','i','c','k']
    typewrite('pls postmemes')
    sleep(random_sleep)
    press('enter')

    random_sleep = randint(2,4)
    typewrite(choice(arr))
    sleep(random_sleep)
    press('enter')

def trivia():
    random_sleep = randint(2,6)
    arr = ['a','b','c','d']
    typewrite('pls trivia')
    sleep(random_sleep)
    press('enter')
    
    random_sleep = randint(2,4)
    typewrite(choice(arr))
    sleep(random_sleep)
    press('enter')
    
def beg():
    random_sleep = randint(2,6)
    typewrite('pls beg')
    sleep(random_sleep)
    press('enter')

def dig():
    random_sleep = randint(2,6)
    typewrite('pls dig')
    sleep(random_sleep)
    press('enter')

def fish():
    random_sleep = randint(2,6)
    typewrite('pls fish')
    sleep(random_sleep)
    press('enter')

def hunt():
    random_sleep = randint(2,6)
    typewrite('pls hunt')
    sleep(random_sleep)
    press('enter')

def level():
    random_sleep = randint(2,6)
    typewrite('pls level')
    sleep(random_sleep)
    press('enter')

arr_functions = [memey, bal, shop_inv, postmemes,trivia, beg, dig, fish, hunt, memey]

def main():
    random_sleep = randint(18,24)
    x = 1
    while x:
        shuffle(arr_functions)
        for f in arr_functions:
            f()
        sleep(random_sleep)
        dep()
        
if __name__ == '__main__':
    print("running")
    sleep(5)
    main()

