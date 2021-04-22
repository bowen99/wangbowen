from pywinauto.keyboard import send_keys
from pywinauto import application
from datetime import datetime
from time import time
import pyautogui
import pyperclip
import os
# screenWidth, screenHeight = pyautogui.size()
# currentMouseX, currentMouseY = pyautogui.position()


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
    hotkey('alt', 'c')
    hotkey('alt', 'c')
    pyautogui.typewrite('sz.fic.com.tw')
    time.sleep(3)
    pyautogui.typewirte('adddomain')
    hotkey('tab')
    pyautogui.typewrite('MisB130')
    press('enter')
    press('enter')
    press('enter')
# 桌面配置


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

# Mail配置


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
    pyautogui.PAUSE = 2
    pyautogui.FAILSAFE = True
    pyautogui.confirm(text='请先退出微信', title='警告', buttons=['确定', '取消'])
    
    #dom = "C:\Windows\System32\SystemPropertiesComputerName.exe"
    desk = "rundll32.exe shell32.dll,Control_RunDLL desk.cpl,,0"
    #wechat = "C:\Program Files (x86)\Tencent\WeChat\WeChat.exe"
    email = "D:\software\office\Office14\MLCFG32.CPL"
    #email = "C:\PROGRA~2\MICROS~1\Office14\MLCFG32.CPL"
    mail_address = "d:\mail"
    m = datetime.now()
    mouth = m.strftime('%Y%m%d')
    #cmd = "C:\Windows\system32\conhost.exe"

# os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
    
    mail()

# app = application.Application().start(
#     'C:\Windows\System32\SystemPropertiesComputerName.exe')
# send_key('%c')
# send_key('%d')
# press('tab')
# send_key('sz.fi')
# # pyautogui.typewrite('sz.fic.com.tw')
# press('enter')


# def move():

#     pyautogui.hotkey('win', 'r')
#     pyperclip.copy("wechat)
#     pyautogui.hotkey('ctrl', 'v')
#     time.sleep(3)
#     pyautogui.press('enter')
#     pyautogui.hotkey('ctrl', 'f')
#     time.sleep(3)


# def user(string):
#     pyperclip.copy(string)
#     pyautogui.hotkey('ctrl', 'v')
#     time.sleep(2)
#     pyautogui.press('enter')

# def message():
#     s = ["要放假了", "太好了"]
#     for i in s:
#         pyperclip.copy(i)
#         pyautogui.hotkey('ctrl', 'v')
#         pyautogui.press('enter')


# move()
# user("汪狗")
# message()
