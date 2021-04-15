import pytest
import yaml

from calculator import Calculator


class TestCalc:
    with open("./data/data_calculator.yml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    print(data)

    def setup(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown(self):
        print("结束计算")

    # 整数 加法
    @pytest.mark.parametrize("a,b,expect", data["add_int"]["datas"], ids=data["add_int"]["ids"])
    def test_add_int(self, a, b, expect):
        print("计算整数加法")
        assert self.calc.add(a, b) == expect

    # 浮点数 加法
    @pytest.mark.parametrize("a,b,expect", data["add_float"]["datas"], ids=data["add_float"]["ids"])
    def test_add_float(self,a,b,expect):
        print("计算浮点数加法")
        assert round(self.calc.add(a, b),2) == expect

    # 整数 减法
    @pytest.mark.parametrize("a,b,expect", data["sub_int"]["datas"], ids=data["sub_int"]["ids"])
    def test_sub_int(self, a, b, expect):
        print("计算整数减法")
        assert self.calc.sub(a, b) == expect

    # 浮点数数 减法
    @pytest.mark.parametrize("a,b,expect", data["sub_int"]["datas"], ids=data["sub_int"]["ids"])
    def test_sub_float(self, a, b, expect):
        print("计算浮点数减法")
        assert round(self.calc.sub(a, b),2) == expect

    # 整数 乘法
    @pytest.mark.parametrize("a,b,expect", data["mul_int"]["datas"], ids=data["mul_int"]["ids"])
    def test_mul_int(self, a, b, expect):
        print("计算整数乘法")
        assert self.calc.mul(a, b) == expect

    # 浮点数 乘法
    @pytest.mark.parametrize("a,b,expect", data["mul_float"]["datas"], ids=data["mul_float"]["ids"])
    def test_mul_float(self, a, b, expect):
        print("计算浮点数乘法")
        assert self.calc.mul(a, b) == expect

    # 整数除法
    @pytest.mark.parametrize("a,b,expect", data["div_data"]["datas"], ids=data["div_data"]["ids"])
    def test_div(self, a, b, expect):
        print("计算整除")
        assert self.calc.div(a, b) == expect