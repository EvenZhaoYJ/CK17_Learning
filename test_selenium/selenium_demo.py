# -*- coding: utf-8 -*-
# @Time:2021-02-28 10:39
# @Author:EvenZhaoYJ
# @File:selenium_demo.py
import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestTmp():
    #在方法前后执行setup、teardown
    def setup_method(self):
        # self.driver = webdriver.Chrome()
        """
        ChromeOptions介绍：https://www.cnblogs.com/yangjintao/p/10599868.html
        :return:
        """
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)


    def teardown_method(self):
        self.driver.quit()


    def test_login_tmp(self):
        """
        基于首页登录
        :return:
        """
        # 遇到ID优先使用ID
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_xpath("//*[@class='index_top_operation_loginBtn']").click()
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']").click()
        sleep(6)
        self.driver.close()


    def test_login_tmp(self):
        """
        基于浏览器复用后的内容进行操作，相当于是直接省去复用浏览器之前的一系列操作，如注释掉的这行代码
        :return:
        """
        # 遇到ID优先使用ID
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.find_element_by_xpath("//*[@class='index_top_operation_loginBtn']").click()
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']").click()
        self.driver.close()

    def test_cookie_login(self):
        """
        利用cookie进行登录，整理思路获取cookie到文件中，读取文件中的cookies进行添加
        步骤：用get_cookies方法获取cookie、add_cookies添加cookie,
             其中add_cookies方法入参是cookie_dict，获取到的cookie是list，
             因此添加cookie时需要借助for循环
        注意点：cookie有有效时间--"expiry": 1646021610
        :return:
        """
        # # 获取登录后的cookkie,将获取的cookie保存到文件中
        # cookies = self.driver.get_cookies()
        # with open("cookies.txt","w",encoding="utf-8") as f:
        #     f.write(json.dumps(cookies))
        #     # json.dump(cookies,f)

        # 指定地址，携带cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        with open("cookies.txt","r",encoding="utf-8") as f:
            raw_cookies = f.read()
            cookies = json.loads(raw_cookies)
            # cookies = json.load(f)

        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        sleep(6)




