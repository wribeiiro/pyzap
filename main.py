from datetime import datetime
import pywhatkit
import keyboard
import time

def send_message(message: str, number: str) -> None:
    pywhatkit.sendwhatmsg(
        number, 
        message, 
        datetime.now().hour, 
        datetime.now().minute + 1
    )

    time.sleep(60)
    keyboard.press_and_release('ctrl + w')

def read_list_numbers() -> None:
    with open('./list_number.txt') as list_number:
        for number in list_number:
            print('Sending to number: ', number)
            send_message('Python is so good! Thanks!', number)

    print('By :)')

read_list_numbers()
