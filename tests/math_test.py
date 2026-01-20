from mylib import add as mylib_add

from biz import demo_biz_add


def test_add():
    assert mylib_add(1, 2) == 3


def test_demo_biz_add():
    assert demo_biz_add(1, 2) == 3
