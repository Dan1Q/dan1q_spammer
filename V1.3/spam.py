import pyautogui as auto  # main library for writing
from time import sleep  # sleep function
from rich import print  # how i made title green
from rich.progress import track  # loading bar
import random  # loading bar work
import pickledb  # simple db for authorization
import sys  # closing program if login or password was incorrect

print("---------------------")
print("[bold green]Dan1Q's Spammer V1.2[/bold green]")  # title
print("---------------------")

db = pickledb.load('test.db', True)  # if db file don't exist we make it, but if db file exist we skip this function
n = 0.001  # delay
y = 4  # words in message count

if not db.exists('login'):  # if db don't exist we make it and setting login and password
    db.set('login', input("Create a username: "))  # login
    db.set('password', input("Create a password: "))  # password
else:  # if db exist
    if input('Enter your username: ') != db.get('login'):  # entering username
        print('Incorrect Username!')  # if username is incorrect we closing program
        sys.exit()  # close function
    elif input('Enter your password: ') != db.get('password'):  # entering password
        print('Incorrect password!')  # if password is incorrect we closing program
        sys.exit()  # close function

print("\nHi, {}!".format(db.get('login')))  # if username and password are correct, program wil give greetings
print("")

print("Enter the number of spam cycles [dim](0 to infinity)[/dim]: ")
count = int(input(">>> "))  # how many times we will send messages
print("")
print("Enter spam text: ")
spam_msg = input(">>> ")  # message text
print("")
print("Code [dim](if you dont have code just press enter)[/dim]:")  # ( ͡° ͜ʖ ͡°)
code = input(">>> ")

print("")

def do_step(step):  # progress bar steps function
    sleep(random.uniform(0.01, 0.1))  # random delay for steps


for step in track(range(100), description="Loading spam function..."):  # progress bar
    do_step(step)

print("")
print("[bold red]Let's Go![/bold red]")

if code == 'i miss the rage':
    while True:
        for x in range(y):
            auto.typewrite("!? I MISS THE RAGE !? ")  # writing message
            sleep(n)  # delay
        auto.press("enter")  # pressing enter

elif code == 'zxc':

    # ⢸⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠆⠀⣰⡗⣿⣿⠃⠀⠀
    #   ⢸⣽⣿⣿⣿⣷⣤⡀⠀⢀⣠⠀⠀⠀⠀⠀⢴⢚⣿⣧⣰⣿⣿⣿⣿
    # ⠀⠀⠈⢿⣿⣿⣿⣷⣿⣏⢰⣾⣿⡄⠀⣠⣷⣾⣵⣿⣿⣿⣿⣿⣿⣿⠋
    # ⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀
    # ⠀⠀⠀⠐⢬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
    # ⠀⠀⠀⠀⠀⠘⣿⡟⠛⠿⢿⣿⣿⣿⣿⣿⣿⡟⣿⣿⠋⠉⢹⣿⠀⠀⠀⠀⠀⠀
    # ⠀⠀⠀⠀⠀⠀⠸⣿⣦⣤⣤⣌⣿⣿⣿⣿⣿⣶⣿⣥⣤⣴⣿⣿⠀⠀⠀⠀⠀⢺
    # ⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀⠀⠀⣼
    # ⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿
    # ⣴⠄⠀⠀⠀⠀⠀⢱⣦⠀⠀⠈⣿⣿⣿⡟⢻⡏⠀⣥⣀⡔⠀⠀⠀⠀⠀⢼⣵⣿
    # ⣿⣷⡄⠀⠀⠀⠀⠀⣿⣆⡆⢠⠈⠈⠿⠁⠘⣠⢠⣿⣿⠃⠀⠀⢀⣶⣶⣿⣿⣿
    # ⣿⡟⢋⡀⠀⠀⠀⠀⠸⣿⣷⣾⣆⠀⠀⠀⠀⣿⣾⣿⣿⠀⠀⠀⣾⣿⣟⣿⣿⣿
    # ⣿⣿⣿⣧⡀⠀⠀⠀⠀⢻⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣷⡀⠀⠀⠀⠈⣿⣿⣿⣷⠀⠀⣸⣿⣿⠁⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠘⠙⣿⡏⠀⠀⢻⡿⠉⢀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿

    print()
    print("coil coil coil")
    print()
    a = 1000
    while a != -1:
        auto.typewrite(f"{a} - 7?")
        a = a - 7
        auto.press("enter")

    auto.typewrite(f"{a} - 7?")

else:
    if count == 0:  # infinity spamming mode
        while True:
            for z in range(y):
                auto.typewrite(spam_msg + " ")  # writing message
                sleep(n)  # delay
            auto.press("enter")  # pressing enter

    else:  # limited mode
        for i in range(count):
            for c in range(y):
                auto.typewrite(spam_msg + " ")  # writing message
                sleep(n)  # delay
            auto.press("enter")  # pressing enter
