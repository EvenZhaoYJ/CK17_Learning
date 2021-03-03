# -*- coding: utf-8 -*-
# @Time:2021-03-03 21:23
# @Author:EvenZhaoYJ
# @File:test_adress.py
from test_selenium_po.adress_page.main_page import MainPage


class TestAdress():
    def test_address(self):
        main = MainPage()
        main.goto_adress().add_member()

