

#计算器相加
def add(a, b):
    return a + b

# __init__.py
# 测试用例命名规范
# 文件要在test_开头，或者_test结尾
# 类要以Test开头，方法要以test_开头
def test_add():
    assert  2 == add(1, 1)
