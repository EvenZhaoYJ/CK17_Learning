# -*- coding: utf-8 -*-
# @Time:2021-02-23 22:53
# @Author:EvenZhaoYJ
# @File:test_fixture.py
import datetime

import pytest

# fixture相当于setup和teardown，在方法的前和后会被调用
# fixture的yield特殊用法可以激活teardown的

@pytest.fixture()
def login():
    print("登录操作")
    token = datetime.datetime.now()
    # 执行测试用例之前，会先执行yield之前的代语句，测试用例执行之后，会执行yield之后的语句
    yield  token  #yield相当于return
    print("登出操作")

# fixture可以调用fixture
@pytest.fixture()
def get_username(login):
    print(login)
    name = "Jenny"
    print(name)
    return name

# 直接调用定义的fixture
def test_search(get_username):
    print("搜索")

# 通过参数化调用fixture，靠近测试用例的fixture先执行
# 需要注意，这种方式调用时，无法获取到fixture的返回值
@pytest.mark.usefixtures("get_username")
@pytest.mark.usefixtures("login") #注意双引号
def test_cart():
    print("购物")


def test_order():
    print("下单")