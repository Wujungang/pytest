import pytest
import requests
import json
import allure


def return_test_data():
    return [(1, 2), (0, 3)]

class Test_ABC:

    def setup_class(self):
        print("------->setup_class")
        return 999

    def teardown_class(self):
        print("------->teardown_class")

    # @pytest.mark.parametrize("a,b", return_test_data())  # 使用函数返回值的形式传入参数值

    def test_a(self):
        print(123456)
        assert 1

    def test_b(self):
        print(999)
        assert 0

    def test_c(self):
        print(123)
        assert 1

    def test_d(self):
        print(123)
        assert 1



if __name__ == '__main__':
  pytest.main(["-s","Test_App7.py"])