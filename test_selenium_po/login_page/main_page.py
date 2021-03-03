# -*- coding: utf-8 -*-
# @Time:2021-03-03 20:08
# @Author:EvenZhaoYJ
# @File:main_page.py
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium_po.login_page.login_page import Loginpage
from test_selenium_po.login_page.register_page import RegisterPage


class MainPage():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")


    def goto_register(self):
        self.driver.find_element(By.XPATH,"//*[@class='index_head_info_pCDownloadBtn']").click()
        return RegisterPage(self.driver)



    def goto_login(self):
        self.driver.find_element(By.XPATH,"//*[@class='index_top_operation_loginBtn']").click()
        return Loginpage(self.driver)


    def download(self):
        pass



