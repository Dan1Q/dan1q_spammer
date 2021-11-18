import pyautogui as auto
from time import sleep
import pickledb
import sys, os
import cfg

db = pickledb.load('login.db', True)
delay = cfg.delay

def login():
    if not db.exists('login'):
        db.set('login', input("Create a username: "))
        db.set('password', input("Create a password: "))
    else:
        if input("Enter your username: ") != db.get('login'):
            print("Incorrect username!")
            sys.exit()
        elif input("Enter your password: ") != db.get('password'):
            print("Incorrect password!")
            sys.exit()

def main():
    print(f"\nFunctions:\n[1] Spamming\n[2] Rage Spamming\n[0] Exit")
    choosing = input(">>> ")
    match choosing:
        case '1':
            count = int(input("How many words in one cycle: "))
            cycle = int(input("How many messsages program should send (0 - infinity): "))
            spam_text = input("Spam text: ")
            print("\nYou have 3 seconds!\n")
            sleep(3)
            if cycle == '0':
                while True:
                    for i in range(count):
                        auto.typewrite(rage_text + " ")
                        sleep(delay / 2)
                    auto.press('enter')
                input("Go back")
                main()
            for i in range(cycle):
                for i in range(count):
                    auto.typewrite(spam_text + " ")
                    sleep(delay)
                auto.press('enter')
            input("Go back")
            main()
            
        case '2':
            count = int(input("How many words in one cycle: "))
            rage_text = input("Spam text: ")
            print("\nYou have 4 seconds!\n")
            sleep(4)
            while True:
                for i in range(count):
                    auto.typewrite(rage_text + " ")
                auto.press('enter')
            input("Go back")
            main()

        case '0':
            print("See you later! :)")
            sys.exit()

        case _:
            print("Invalid function!")
            main()
login()
main()