# -*- coding: utf-8 -*-
# @Time:2021-03-03 21:37
# @Author:EvenZhaoYJ
# @File:main_page.py
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium_po.adress_page.address_page import AddressPage


class MainPage():
    def __init__(self):
        # 声明Chrome参数
        chrome_arg = webdriver.ChromeOptions()
        # 调试模式，加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)  # 每次都会弹出一个新的界面
        self.driver.implicitly_wait(5)

    def goto_adress(self):
        # 点击通讯录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.find_element_by_xpath("//*[@id='menu_contacts']").click()
        self.driver.find_element(By.XPATH,"//*[@id='menu_contacts']").click()
        return AddressPage(self.driver)
