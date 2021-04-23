from selenium import webdriver
import pyautogui
import pyperclip
import time
# 谷歌浏览器驱动地址
driver = webdriver.Chrome(
    "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")

# Ie浏览器驱动地址
#driver = webdriver.Ie("C:\\Program Files (x86)\\Internet Explorer\\IEDriverServer.exe")
# driver.implicitly_wait(10)
driver.get("https://weibo.com/login.php")

# 控制浏览器窗口大小
driver.set_window_size(1920, 1080)
time.sleep(3)
driver.find_element_by_id("loginname").send_keys("18037500531")
driver.find_element_by_name("password").send_keys("Wang1993")
pyautogui.press("enter")
'''
driver.find_element_by_name("user").click()
pyperclip.copy("FSE174")
pyautogui.hotkey("ctrl", "v")
driver.find_element_by_name("pwd").click()
pyperclip.copy("123456")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press("enter")
'''

# driver.find_element_by_id("J-password").send_keys("Wang1993")
# driver.find_element_by_id("J-loginImg").click()
