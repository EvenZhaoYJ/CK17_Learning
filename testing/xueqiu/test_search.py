# -*- coding: utf-8 -*-
# @Time:2021-02-23 23:38
# @Author:EvenZhaoYJ
# @File:test_search.py

# conftest有就近原则，会优先选择当前模块下的conftest，当前模块下没有时，会依次往上找
def test_search(login):
    # f开头表示在字符串内支持大括号内的python 表达式，就是说可以把调用login函数return的username赋值给username
    print(f'username : {login}')
    print("搜行情搜索")