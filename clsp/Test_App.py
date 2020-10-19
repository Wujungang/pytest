import pytest

class Test_ABC:
    def setup_class(self):
        print("------->setup_class")
    def teardown_class(self):
        print("------->teardown_class")
    def test_a(self):
        print("------->test_a")
        assert 1
    def test_b(self):
        print("------->test_b")
        name = "wujg"
        assert name == "wujg"

if __name__ == '__main__':
    pytest.main(["-s","Test_App.py"])