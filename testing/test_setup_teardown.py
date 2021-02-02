import pytest

def test_a():
    print('aaa')

def setup_function():
    print('测试前')

def teardown_function():
    print('测试后')