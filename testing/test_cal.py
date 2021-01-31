# -*- coding: utf-8 -*-
# @Time:2021-01-30 11:39
# @Author:EvenZhaoYJ
# @File:test_cal.py
import yaml

from pythoncode.Calculator import Calculator
import pytest
import sys

print(sys.path)
sys.path.append('..')

# 获取yaml文件中的数据
def get_datas():
    with open('datas/calc.yml') as f:
        # 将yaml数据流转为python对象
        datas = yaml.safe_load(f)
        datas_add = datas['add']['datas']
        datas_div = datas['div']['datas']
    # return data['add']['datas']
    return [datas_add,datas_div]
    # print(datas['div']['datas'])


class Testcal():
    # 定义一个类变量存储从yaml获取到的数据
    datas:list = get_datas()
    # print(datas[0])


    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    # 为测试用例添加标签后，pytest无法识别自定义的标签，需要在pytest.ini中进行配置
    @pytest.mark.add
    @pytest.mark.parametrize("a,b,result",datas[0],ids=['int','float','zero','minus','bignum'])
    # 测试计算器的相加功能
    def test_add(self,a,b,result):
        # 在每一个方法都进行计算器类实例化代码比较冗余，可以使用类级的setup/teardown
        # cal = Calculator()
        print(f"a={a},b={b},result={result}")
        print("加法")
        assert result == self.cal.add(a,b)

    @pytest.mark.div
    @pytest.mark.parametrize("a,b,result",datas[1],ids=['int','float','zero','minus','bignum'])
    def test_div(self,a,b,result):
        # 在每一个方法都进行计算器类实例化代码比较冗余，可以使用类级的setup/teardown
        # cal = Calculator()
        print("除法")
        assert result == self.cal.div(a,b)



