from biz import demo_biz_add
from my_sdk import add as my_sdk_add


def test_add():
    assert my_sdk_add(1, 2) == 3


def test_demo_biz_add():
    assert demo_biz_add(1, 2) == 3
