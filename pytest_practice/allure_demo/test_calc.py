import allure
import pytest
import yaml


with open("data_calc.yml", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print(data)
    print(data["add_float"]["datas"],data["add_float"]["ids"])
@allure.feature("计算器加法")
class TestCal_add:

    # fixture params ids 传递参数
    @allure.story("整数相加功能")
    def test_add_int(self, get_calc,get_datas):
        print("计算整数加法")
        print(get_datas)
        assert get_calc.add(get_datas[0],get_datas[1]) == get_datas[2]

    @allure.story("浮点数相加功能")
    @pytest.mark.parametrize("a,b,expect",data["add_float"]["datas"], ids=data["add_float"]["ids"])
    def test_add_float(self, get_calc,a, b, expect):
        print("计算浮点数加法")
        assert round(get_calc.add(a, b), 2) == expect

@allure.feature("计算器减法")
class TestCal_sub:
    @allure.story("整数相减功能")
    @pytest.mark.parametrize("a,b,expect", data["sub_int"]["datas"], ids=data["sub_int"]["ids"])
    def test_sub_int(self,get_calc,a,b,expect):
        print("计算整数减法")
        assert get_calc.sub(a, b) == expect

    @allure.story("浮点数数相减功能")
    @pytest.mark.parametrize("a,b,expect", data["sub_int"]["datas"], ids=data["sub_int"]["ids"])
    def test_sub_float(self,get_calc,a,b,expect):
        print("计算浮点数减法")
        assert round(get_calc.sub(a, b), 2) == expect

@allure.feature("计算器乘法")
class TestCal_mul:
    @allure.story("整数相乘功能")
    @pytest.mark.parametrize("a,b,expect", data["mul_int"]["datas"], ids=data["mul_int"]["ids"])
    def test_mul_int(self,get_calc,a,b,expect):
        print("计算整数乘法")
        assert get_calc.mul(a, b) == expect

    @allure.story("浮点数相乘功能")
    @pytest.mark.parametrize("a,b,expect", data["mul_float"]["datas"], ids=data["mul_float"]["ids"])
    def test_mul_float(self,get_calc,a,b,expect):
        print("计算浮点数乘法")
        assert get_calc.mul(a, b) == expect

@allure.feature("计算器除法")
class TestCal_div:
    @allure.story("整除功能")
    @pytest.mark.parametrize("a,b,expect", data["div_data"]["datas"], ids=data["div_data"]["ids"])
    def test_div(self,get_calc,a,b,expect):
        print("计算整除")
        assert get_calc.div(a, b) == expect