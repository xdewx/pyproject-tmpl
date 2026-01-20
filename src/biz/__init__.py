from ipa.decorator import deprecated
from mylib import add as mylib_add


@deprecated("use mylib.add instead")
def demo_biz_add(a: int, b: int) -> int:
    c = mylib_add(a, b)
    print(f"add({a}, {b}) = {c}")
    return c
