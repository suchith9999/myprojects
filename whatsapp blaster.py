from string import digits
from unicodedata import numeric
import pyautogui as spam
import time
from pyautogui import FailSafeException

print("Working on Whatsapp and telegram")
print("use https://web.whatsapp.com/ or https://web.telegram.org/k/ Use chrome browser")


while True:
    try:
        limit = input("Enter no. of massage to send>:")
        msg = input("Enter massage you want to send>:")
        limit = int(limit)
    except FailSafeException:
        print("Please try agian")
    except ValueError:
        print("Please enter numeric digits")
    except TypeError:
        print("object cannot be interpreted as an integer")           

    
    i = 0
    time.sleep(10)

    for i in range(limit):
        spam.typewrite(msg)
        spam.press('Enter')
        print("Massage sent successfully")

