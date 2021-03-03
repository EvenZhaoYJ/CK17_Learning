# -*- coding: utf-8 -*-
# @Time:2021-03-03 21:11
# @Author:EvenZhaoYJ
# @File:test_register.py
from time import sleep

from test_selenium_po.login_page.main_page import MainPage


class TestRegister():
    def test_rigister(self):
        main = MainPage()
        main.goto_register().register()
        sleep(5)

    def test_login_register(self):
        a = MainPage()
        a.goto_login().goto_register()


