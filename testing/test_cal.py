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
# def get_datas():
#     with open('datas/calc.yml') as f:
#         # 将yaml数据流转为python对象
#         datas = yaml.safe_load(f)
#         datas_add = datas['add']['datas']
#         datas_div = datas['div']['datas']
#     return [datas_add,datas_div]

def get_datas(name,type='int'):
    with open('datas/calc.yml') as f:
        # 将yaml数据流转为python对象
        all_datas = yaml.safe_load(f)
    datas = all_datas[name][type]['datas']
    ids = all_datas[name][type]['ids']
    return [datas,ids]

# 测试用例设计规则：正常场景、异常场景测试方法分开，测试数据也分开，这样便于维护
class Testcal():
    # 定义一个类变量存储从yaml获取到的数据
    # datas:list = get_datas()
    # print(datas[0])
    add_int_data = get_datas('add','int')
    div_int_data = get_datas('div','int')

    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    # 为测试用例添加标签后，pytest无法识别自定义的标签，需要在pytest.ini中进行配置
    @pytest.mark.add
    @pytest.mark.parametrize("a,b,result",add_int_data[0],ids=add_int_data[1])
    # 测试计算器的相加功能
    # 异常场景:浮点数相加，可以再写一个测试用例方法，异常场景与场景分开，便于维护
    def test_add(self,a,b,result):
        # 在每一个方法都进行计算器类实例化代码比较冗余，可以使用类级的setup/teardown
        # cal = Calculator()
        print(f"a={a},b={b},result={result}")
        print("加法")
        assert result == round(self.cal.add(a, b), 4)  # 控制结果的小数位数为4位


    @pytest.mark.div
    @pytest.mark.parametrize("a,b,result",div_int_data[0],ids=div_int_data[1])
    def test_div(self,a,b,result):    # 需要考虑除数为0的异常场景
        # 在每一个方法都进行计算器类实例化代码比较冗余，可以使用类级的setup/teardown
        # cal = Calculator()
        print("除法")
        # raises为pytest自带的异常捕获机制，发生异常的时候会执行通过，不发生异常的时候，不会执行通过
        with pytest.raises(ZeroDivisionError):
            assert result == self.cal.div(a, b)




