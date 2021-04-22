from selenium import webdriver
# 谷歌浏览器驱动地址
#driver = webdriver.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")

# Ie浏览器驱动地址
driver = webdriver.Ie(
    "C:\\Program Files (x86)\\Internet Explorer\\IEDriverServer.exe")
#driver.implicitly_wait(10)
driver.get("http://sz6web.fic.com.tw")
# 控制浏览器窗口大小
#driver.set_window_size(1360, 1800)
# 输入框输入内容
driver.find_element_by_class_name("login-hd-account").click()
driver.find_element_by_id("J-userName").send_keys("18037500531")
driver.find_element_by_id("J-password").send_keys("Wang1993")
driver.find_element_by_id("J-loginImg").click()

