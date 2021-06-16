import time
#from threading import Thread
from pyautogui import typewrite, sleep, press
from random import choice, randint, shuffle

#ctrl+c on terminal to stop the program.

def guess():
    typewrite('pls guess')
    sleep(2)
    press('enter')

    for i in range(0,4):
        typewrite(str(randint(1,20)))
        sleep(1)
        press('enter')

def memey():
    random_sleep = randint(7,12)
    arr = ['4chan', 'blacktwitter','chucknorris','comics','discordmeme','joke','meirl','prequel','pun','sequel']
    typewrite('pls ' + choice(arr))
    sleep(2)
    press('enter')
    sleep(random_sleep)

def bal():
    sleep(2)
    typewrite('pls bal')
    press('enter')

    r = randint(0,1)
    if r:
        dep()

def shop():
    random_sleep = randint(2,6)
    number = str(randint(2,5))
    typewrite('pls shop '+ number)
    sleep(random_sleep)
    press('enter')

def inv():
    random_sleep = randint(2,6)
    number = str(randint(2,4))
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

    random_sleep = randint(1,3)
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

    r = randint(0,1)
    if r:
        random_sleep = randint(2,6)
        typewrite('pls level')
        sleep(random_sleep)
        press('enter')
    
def active():

    r = randint(0,1)
    if r:
        random_sleep = randint(2,6)
        typewrite('pls level --active')
        sleep(random_sleep)
        press('enter')

def random_word():
    random_word = ["bark","mighty","yourself","finally","rays","what"
"climate","any","cabin","sure","laugh","paid"
"city","excitement","different","buy","article","way"
"dinner","soil","hearing","stop","hearing","broad"
"population","hand","off","exclaimed","giving","young"
"riding","buried","poet","including","early","do"
"surface","graph","skin","use","dot","wheel"]
    typewrite(choice(random_word))
    press('enter')

def chance():
    flip = randint(0,19)
    if flip == 1:
        print("5% just happened")
        return True
    return False

arr_functions = [guess, random_word, postmemes , bal, trivia, level, beg, dig, fish, hunt]


def main():
    x = 1
    while x:
        random_sleep = randint(20,35)
        shuffle(arr_functions)
        for f in arr_functions:
            f()
        sleep(random_sleep)
        active()
        if chance():
            sleep(180)
        
if __name__ == '__main__':
    print("running")
    main()

