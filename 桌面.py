from pywinauto.keyboard import send_keys
from pywinauto import application
from datetime import datetime
import time
import pyautogui
import pyperclip
import os



def copy(str):
    pyperclip.copy(str)
    pyautogui.hotkey('ctrl', 'v')


def hotkey(x, y, *args):
    pyautogui.hotkey(x, y)


def send_key(str):
    '''
    ^ --> Ctrl
    % --> Alt
    '''
    send_keys(str)


def press(x):
    pyautogui.press(x)


def desktop():
    hotkey('win', 'r')
    copy(desk)
    press('enter')
    # time.sleep(3)
    hotkey('alt', 'm')
    # time.sleep(0.5)
    hotkey('alt', 'U')
    # time.sleep(0.5)
    hotkey('alt', 'N')
    # time.sleep(0.5)
    hotkey('alt', 'R')
    press('enter')


def mail():
    hotkey('win', 'r')
    copy(email)
    press('enter')
    send_key('%D')
    press('shift')
    pyautogui.typewrite('123')
    press('enter')
    press('enter')
    press('enter')
    hotkey('alt', 'r')
    hotkey('alt', 'f')
    hotkey('alt', 'a')
    send_key('%D')
    if not os.path.exists(mail_address):
        os.makedirs(mail_address)
    copy(mail_address)

    # send_key('^v')
    hotkey('shift', 'enter')
    hotkey('alt', 'n')
    copy(mouth)
    press('enter')
    hotkey('alt', 'd')
    hotkey('alt', 'y')
    press('left')
    hotkey('alt', 'f')
    hotkey('alt', 'y')
    press('enter')
    hotkey('alt', 'c')
    hotkey('alt', 'c')
    press('enter')


if __name__ == "__main__":
    time.sleep(3)
    pyautogui.PAUSE = 2
    pyautogui.FAILSAFE = True
    desk = "rundll32.exe shell32.dll,Control_RunDLL desk.cpl,,0"
    cmd = "C:\Windows\system32\conhost.exe"
    email = "C:\Program Files (x86)\Miscrosoft Office\Office14\MLCFG32.CPL"
    mail_address = "d:\mail"
    m = datetime.now()
    mouth = m.strftime('%Y%m%d')
    desktop()
    mail()
