# -*- encoding=utf8 -*- 
'''
@Time:  2022/4/1-18:31
@User:  Administrator
@File:  test3.py
@Email：  liuxiong@fcbox.com
'''
import pytest

'''
开始创建一个测试
'''
# def func(x):
#     return x+1
#
#
#
# def test_anwser():
#     assert func(3) ==4
#
# def test_anwser_error():
#     assert func(3) ==5

'''
使用raise
'''

# def f():
#     raise SystemExit(1)
#
# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()


# class TestClass():
#     def test_one(self):
#         x = "this"
#         assert 'h' in x
#
#     def test_two(self):
#         x1 = "hello"
#         assert 'h' in x1

import sys
class MyPlugin():
    def pytest_sessionfinish(self):
        print("***test run reporting***")


if __name__ == "__main__":
    sys.exit(pytest.main(["-qq"],plugins=[MyPlugin()]))