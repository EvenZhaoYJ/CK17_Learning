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


def get_datas(name,type='int'):
    # windows系统的编码默认为GBK，当yaml文件中包含中文时，需要指定编码格式为utf-8
    with open('datas/calc.yml',encoding='utf-8') as f:
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

    # 为测试用例添加标签后，pytest无法识别自定义的标签，需要在pytest.ini中进行配置
    # @pytest.mark.add
    # @pytest.mark.parametrize("a,b,result",add_int_data[0],ids=add_int_data[1])
    # 测试计算器的相加功能
    # 异常场景:浮点数相加，可以再写一个测试用例方法，异常场景与场景分开，便于维护
    # def test_add(self,a,b,result,get_instance):
    #     # 在每一个方法都进行计算器类实例化代码比较冗余，可以使用类级的setup/teardown
    #     # cal = Calculator()
    #     print(f"a={a},b={b},result={result}")
    #     print("加法")
    #     assert result == round(get_instance.add(a, b), 4)  # 控制结果的小数位数为4位

    def test_add(self,get_instance,get_adddatas_with_fixture):
        # 在每一个方法都进行计算器类实例化代码比较冗余，可以使用类级的setup/teardown
        # cal = Calculator()
        f = get_adddatas_with_fixture
        print(f)
        # print("加法")
        assert f[2] == round(get_instance.add(f[0], f[1]), 4)  # 控制结果的小数位数为4位

    # @pytest.mark.div
    # @pytest.mark.parametrize("a,b,result",div_int_data[0],ids=div_int_data[1])
    # def test_div(self,a,b,result,get_instance):    # 需要考虑除数为0的异常场景
    #     # 在每一个方法都进行计算器类实例化代码比较冗余，可以使用类级的setup/teardown
    #     # cal = Calculator()
    #     print("除法")
    #     # raises为pytest自带的异常捕获机制，发生异常的时候会执行通过，不发生异常的时候，不会执行通过
    #     with pytest.raises(ZeroDivisionError):
    #         assert result == get_instance.div(a, b)

    def test_div(self, get_instance, get_divdatas_with_fixture):
        f = get_divdatas_with_fixture
        # print("除法")
        if f[1] == 0:
            with pytest.raises(ZeroDivisionError):
                assert f[2] == round(get_instance.div(f[0], f[1]), 4)
        else:
            assert f[2] == round(get_instance.div(f[0], f[1]), 4)


