# -*- coding: utf-8 -*-
# @Time:2021-02-23 23:30
# @Author:EvenZhaoYJ
# @File:test_yield.py


# 当前的模块想用某个包里的类或者方法/函数的话，都需要进行导入
# 归功于pytets的实现机制，在执行当前模块或包时，会先去加载conftest.py文件
def test_search(login):
    print("搜索")

def test_cart():
    print("购物")


def test_order():
    print("下单")