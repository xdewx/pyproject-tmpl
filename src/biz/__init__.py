from ipa.decorator import deprecated

from my_sdk import add as my_sdk_add


@deprecated("use my_sdk.add instead")
def demo_biz_add(a: int, b: int) -> int:
    c = my_sdk_add(a, b)
    print(f"add({a}, {b}) = {c}")
    return c
