# -*- coding: utf-8 -*-
# @Time:2021-02-24 1:37
# @Author:EvenZhaoYJ
# @File:__init__.py.py

# pytest是不支持中文，因此测试用例名称需要展示中文时，需要在这个hook函数里面进行重新编码
from typing import List


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    for item in items:
        # nodeid为测试用例的名字，name为测试用例的路径包括文件名
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

# def pytest_addoption(parser):
#     group = parser.getgroup