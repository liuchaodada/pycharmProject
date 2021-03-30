import pytest
import yaml

from calculator import *

def get_datas():
    with open(r"./data/data_calculator.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas

class TestCalculator:

    def setup_class(self):
        print("开始测试")
        self.c = Calculator()

    def teardown_class(self):
        print("结束测试")

    # 测试加法
    @pytest.mark.parametrize(
        "a, b, expect", get_datas()["add"]
    )
    def test_add(self, a, b, expect):
        result = self.c.add(a, b)
        if (isinstance(result,float)):
            result = round(result, 2)
        assert result == expect

    # 测试减法
    @pytest.mark.parametrize(
        "a, b, expect", get_datas()["sub"]
    )
    def test_sub(self, a, b, expect):
        result = self.c.sub(a, b)
        if (isinstance(result, float)):
            result = round(result, 2)
        assert result == expect

    # 测试乘法
    @pytest.mark.parametrize(
        "a, b, expect", get_datas()["mul"]
    )
    def test_mul(self, a, b, expect):
        result = self.c.mul(a, b)
        if (isinstance(result, float)):
            result = round(result, 2)
        assert result == expect

    # 测试除法
    @pytest.mark.parametrize(
        "a, b, expect", get_datas()["div"]
    )
    def test_div(self, a, b, expect):
        result = self.c.div(a, b)
        if (isinstance(result, float)):
            result = round(result, 2)
        assert result == expect