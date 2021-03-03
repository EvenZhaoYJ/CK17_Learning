# -*- coding: utf-8 -*-
# @Time:2021-03-03 20:09
# @Author:EvenZhaoYJ
# @File:login_page.py
from selenium.webdriver.common.by import By

from test_selenium_po.login_page.register_page import RegisterPage


class Loginpage():

    def __init__(self,driver):
        self.driver = driver


    def login(self):
        pass



    def goto_register(self):
        self.driver.find_element(By.XPATH,"//*[@class='login_registerBar_link']").click()
        return RegisterPage(self.driver)

