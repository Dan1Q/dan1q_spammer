import pyautogui as auto  # main library for writing
from time import sleep  # sleep function
from rich import print
from rich.progress import track
import random

print("---------------------")
print("[bold green]Dan1Q's Spammer V1.1[/bold green]")  # title
print("---------------------")

n = 0.001  # delay
y = 4  # words in message count

print("Enter the number of spam cycles [dim](0 to infinity)[/dim]: ")
count = int(input(">>> "))  # how many times we will send messages
print("Enter spam text: ")
spam_msg = input(">>> ")  # message text
print("Code [dim](if you dont have code just press enter)[/dim]:")
code = input(">>> ")

print("")

def do_step(step):
    sleep(random.uniform(0.01, 0.1))


for step in track(range(100), description="Loading..."):
    do_step(step)

print("")
print("[bold red]Let's Go![/bold red]")

if code == 'i miss the rage':
    while True:
        for x in range(y):
            auto.typewrite("!? I MISS THE RAGE !? ")  # writing message
            sleep(n)  # delay
        auto.press("enter")  # pressing enter

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
