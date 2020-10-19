# coding=utf-8
import pytest
import allure

def return_test_data():
    return [(1, 2),(0, 3)]

@allure.feature("工作日报")
class Test_ABC:

    def setup_class(self):
        print("------->setup_class")
    def teardown_class(self):
        print("------->teardown_class")

    @allure.story("暂存日报")
    @pytest.mark.parametrize("a,b",return_test_data()) # 使用函数返回值的形式传入参数值
    def test_a(self,a,b):
        print("test data:a=%d,b=%d"%(a,b))
        assert a+b == 3