# -*- coding: utf-8 -*-
# @Time:2021-02-24 0:04
# @Author:EvenZhaoYJ
# @File:test_fixture_demo.py

# fixture高级用法-参数化
import pytest


@pytest.fixture(params=['harry','hemin'])
def login(request):
    print("login")
    return request.param #通过request(request也是fixture)来获取params里的值


def test_search(login):
    print(login)
    print("搜索")

