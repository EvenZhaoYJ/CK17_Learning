# -*- coding: utf-8 -*-
# @Time:2021-02-24 1:39
# @Author:EvenZhaoYJ
# @File:setup.py.py
# setup.py是一个构建工具。离线安装：安装源码，即安装setup.py即可，如命令python setup.py install

from setuptools import setup
setup(
    name='pytest_encode',#名字与包的名称一致
    url='https://github.com/xxx/pytest-encode',#github地址
    version='1.0',
    author="xixi",
    author_email='418974188@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[# 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages=['pytest_encode'],
    keywords=[
        'pytest', 'py.test', 'pytest_encode',
    ],

    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 入口模块 或者入口函数
    entry_points={
        'pytest11': [
            'pytest-encode = pytest_encode',
        ]
    },
    zip_safe=False
)