# -*- coding: utf-8 -*-
# @Time:2021-02-23 23:28
# @Author:EvenZhaoYJ
# @File:conftest.py

# conftest.py 文件名字是固定的，不能改

# 用fixture替代setup和teardown
from typing import List

import pytest

from pythoncode.Calculator import Calculator
from testing.test_cal import get_datas


@pytest.fixture(scope='class')
def get_instance():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("结束计算")

@pytest.fixture(params=get_datas('add','int')[0],ids=get_datas('add','int')[1])
def get_adddatas_with_fixture(request):
    return request.param

@pytest.fixture(params=get_datas('div','int')[0],ids=get_datas('div','int')[1])
def get_divdatas_with_fixture(request):
    return request.param


