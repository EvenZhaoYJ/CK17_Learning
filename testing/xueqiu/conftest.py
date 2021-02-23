# -*- coding: utf-8 -*-
# @Time:2021-02-23 23:39
# @Author:EvenZhaoYJ
# @File:conftest.py

import datetime

import pytest


@pytest.fixture(scope='session')
def login():
    print("登录操作")
    name = "哈利波特"
    # 执行测试用例之前，会先执行yield之前的代语句，测试用例执行之后，会执行yield之后的语句
    yield  name  #yield相当于return
    print("登出操作")