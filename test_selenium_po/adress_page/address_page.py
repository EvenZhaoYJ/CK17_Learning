# -*- coding: utf-8 -*-
# @Time:2021-03-03 21:44
# @Author:EvenZhaoYJ
# @File:address_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage():
    def __init__(self,driver):
        self.driver = driver

    def add_member(self):
        def wait_time(driver):
            eles = driver.find_element(By.XPATH,"//*[@class='qui_btn ww_btn js_add_member']")
            # eles[-1].click()
            if len(eles) < 3:
                eles[0].click()
            else:
                eles[1].click()
            eles = driver.find_element(By.XPATH,"//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(eles) > 0

        WebDriverWait(self.driver,10).until(wait_time)

        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("zhao")
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("12882812")
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()




