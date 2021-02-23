# -*- coding: utf-8 -*-
# @Time:2021-02-24 1:49
# @Author:EvenZhaoYJ
# @File:test_encode.py
import pytest


@pytest.mark.parametrize('name',['小莉莉','花花'])
def test_encode(name):
    print(name)
