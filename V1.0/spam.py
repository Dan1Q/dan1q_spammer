import pyautogui as auto  # main library for writing
from time import sleep  # sleep function

print("---------------------")
print("Dan1Q's Spammer V1.0")  # title
print("---------------------")

count = int(input("Enter the number of spam cycles (0 to infinity): "))  # how many times we will send messages
spam_msg = input("Enter spam text: ")  # message text

n = 0.001  # delay
y = 4  # words in message count

print("---------------------------------------")  # some useless information
print(f"The number of spam cycles is {count}")
print(f"Your text is '{spam_msg}'")
print("---------------------------------------")

print("Wait 3 seconds")

sleep(3)  # delay for 3 seconds and start

if count == 0:  # infinity spamming mode
    while True:
        for z in range(y):
            auto.typewrite(spam_msg + " ")  # writing message
            sleep(n)  # delay
        auto.press("enter")  # pressing enter

else:  # limited mode
    for i in range(count):
        for x in range(y):
            auto.typewrite(spam_msg + " ")  # writing message
            sleep(n)  # delay
        auto.press("enter")  # pressing enter
