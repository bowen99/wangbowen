
import os
from selenium import webdriver

#新浪微博登录类
class SinaMicroBlogLogin():
    #初始化方法：设置浏览器驱动
    def __init__(self):
        chromeDriverPath = ("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
    #模拟登录方法
    def login(self,account,passwd):
        '''
            account:账号
            passwd：密码
        '''
        chrome = self.brower;
        #chrome浏览器打开微博登录页
        chrome.get("http://weibo.com/login.php")
        #获取账号输入框
        elemAccount = chrome.find_element_by_id("loginname")
        #填充账号信息
        elemAccount.send_keys(account)
        #获取密码输入框
        elemPasswd = chrome.find_element_by_name("password")
        #填充密码信息
        elemPasswd.send_keys(passwd)
        #获取提交按钮
#         elemSubmit = chrome.find_element_by_xpath("//input[@class='W_btn_a btn_32px ']")
        elemSubmit = chrome.find_element_by_class_name("W_btn_a")
        #模拟提交
        elemSubmit.click()
        #登录成功判断：判断登录后网页源码中是否含有字符串“我的收藏”
        if "我的收藏" in chrome.page_source:
            print("登录成功！")
            return True
        else:
            print("登录失败！")
            return False

sinaLogin = SinaMicroBlogLogin()
sinaLogin.login("18037500531", "Wang1993")
