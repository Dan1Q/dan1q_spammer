import pyautogui as auto

from time import sleep
from rich import print

import random
import pickledb
import sys, os

delay = 0.001
db = pickledb.load('login.db', True)

def login_system():
    if not db.exists('login'):
        db.set('login', input("Create a username: "))
        db.set('password', input("Create a password: "))
        db.set('pin', input("Create a pin-code: "))

    else:
        if input("Enter your username: ") != db.get('login'):
            print("Incorrect username!")
            sys.exit()

        elif input("Enter your password: ") != db.get('password'):
            print("Incorrect password!\n\nForgot password? Reset it via pin-code!\n")
            if input("Enter your pin-code: ") != db.get('pin'):
                print("Wrong pin-code")
                sys.exit()
            db.set('password', input("Create a password: "))

name = db.get('login')

login_system()
print(f"Greetings, {name}")

def a():
    choosing = print("\nWhat would we do now?\n[1] Spam\n[2] Play amonus (so sussy O_O)\n[3] Help\n[4] What's new?\n[5] Exit")
    choosing = int(input("$ "))

    if choosing == 1:
        count = int(input("How many words in one cycle?: "))
        cycle = int(input("How many messsages program should send?: "))
        spam_text = input("Spam text: ")
        print("\nYou have 3 seconds!\n")
        sleep(3)

        for i in range(cycle):
            for i in range(count):
                auto.typewrite(spam_text + " ")
                sleep(delay)
            auto.press('enter')
        input("Go back")
        a()

    elif choosing == 2:
        print("bro?")
        sleep(0.5)
        os.remove('login.db')
        print("I just removed your login data ;)")
        input()
        sys.exit()

    elif choosing == 3:
        print("\nHelp:\n\nCount - how many words program will wright before pressing enter:\n\n3 counts:\nword word word\nword word word\n")
        input("Go back")
        a()

    elif choosing == 4:
        print("\nWhat's new:\nThere're no more cods! They will be added in version 2.1 or later\nNo more infinity spamming mode (cuz bugs)! I will add this soon in 2.1 or 2.2\nNew.. design? gui? console text?\n")
        input("Go back")
        a()

    elif choosing == 5:
        print("See you later! :)")
        sys.exit()

    else:
        a()
a()