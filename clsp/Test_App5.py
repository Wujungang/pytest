import pytest

class Test_ABC:
    def setup_class(self):
        print("------->setup_class")
    def teardown_class(self):
        print("------->teardown_class")
    def test_a(self):
        print("------->test_a")
        assert 1
    @pytest.mark.xfail(2 > 1, reason="标注为预期失败") # 标记为预期失败函数test_b
    def test_b(self):
        print("------->test_b")
        assert 0

if __name__ == '__main__':
  pytest.main(["-s","Test_App5.py"])