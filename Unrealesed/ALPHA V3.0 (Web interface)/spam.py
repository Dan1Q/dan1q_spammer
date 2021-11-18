import pyautogui as auto

from pywebio.input import input
from pywebio.output import put_text
from time import sleep

import random
import pickledb
import sys, os

delay = 0.001
db = pickledb.load('login.db', True)

def login_system():
    if not db.exists('login'):
        db.set('login', input("Create a username"))
        db.set('password', input("Create a password"))

    else:
        if input("Enter your username") != db.get('login'):
            put_text("Incorrect username!")
            sys.exit()

        elif input("Enter your password") != db.get('password'):
            put_text("Incorrect password!")
            sys.exit()

def main_system():
    choosing = int(input("(Main page) Choose one:"))
    

    if choosing == 1:
        count = int(input("How many words in one cycle?"))
        cycle = int(input("How many messsages program should send?"))
        spam_text = input("Spam text")
        put_text("\nYou have 3 seconds!\n")
        sleep(3)

        for i in range(cycle):
            for i in range(count):
                auto.typewrite(spam_text + " ")
                sleep(delay)
            auto.press('enter')
        input("Go back")
        main_system()

    elif choosing == 2:
        put_text("bro?")
        sleep(0.5)
        os.remove('login.db')
        put_text("I just removed your login data ;)")
        input("Exit")
        sys.exit()


    elif choosing == 5:
        put_text("See you later! :)")
        sys.exit()

    else:
        main_system()

name = db.get('login')

login_system()
put_text(f"Greetings, {name}\n\nFunctions:\n[1] Spam\n[2] Play amonus (so sussy O_O)\n[5] Exit")

start_server(main_system, port=8080, debug=True)