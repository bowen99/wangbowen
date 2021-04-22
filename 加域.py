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


def domain():
    hotkey('win', 'r')
    copy(dom)
    press('enter')
    time.sleep(3)
    hotkey('alt', 'c')
    hotkey('alt', 'd')
    press('tab')
    copy(domname)
    press('enter')
    time.sleep(4)
    copy(name)
    press('tab')
    copy(passwd)
    press('enter')
    time.sleep(3)
    press('enter')
    time.sleep(3)
    press('enter')


if __name__ == "__main__":
    pyautogui.PAUSE = 2
    pyautogui.FAILSAFE = True
    dom = "C:\Windows\System32\SystemPropertiesComputerName.exe"
    domname = "sz.fic.com.tw"
    name = "adddomain"
    passwd = "MisB130"
    domain()
