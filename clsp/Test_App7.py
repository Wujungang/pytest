import pytest
import requests
import json


def return_test_data():
    return [(1, 2), (0, 3)]

class Test_ABC:
    @pytest.fixture()
    def setup_class(self):
        print("------->setup_class")
        return 999

    def teardown_class(self):
        print("------->teardown_class")

    # @pytest.mark.parametrize("a,b", return_test_data())  # 使用函数返回值的形式传入参数值
    @pytest.fixture()
    def test_a(self):
        headers = {
            "Content-Type":"application/json",
            "x-okapi-tenant":"l001736"
        }
        data = {
            "username": "administrator",
            "password": "letmein"
        }
        data = json.dumps(data)
        res = requests.post("http://39.106.33.252/okapia/bl-users/login",data=data,headers = headers)

        assert len(res.headers["x-okapi-token"]) == 277
        return res.headers["x-okapi-token"]

    @pytest.fixture()
    def test_c(self):
        return 456


    def test_b(self,test_a,test_c,setup_class):
        headers = {
            "x-okapi-tenant":"l001736",
            "x-okapi-token":test_a
        }
        res = requests.get("http://39.106.33.252/okapia/_/discovery/modules/mod-validatecode-0.0.1-SNAPSHOT")
        print(res.text)
        print(test_c)
        print(setup_class)

if __name__ == '__main__':
  pytest.main(["-s","Test_App7.py"])