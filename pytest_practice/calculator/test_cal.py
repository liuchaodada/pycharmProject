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

    @pytest.mark.parametrize("a, b, expect", datas['add_int']['datas'], ids=datas['add_int']['ids'])
    def test_add_int(self, a, b, expect):
        assert self.cal.add(a, b) == expect

    @pytest.mark.parametrize("a, b, expect", datas['add_float']['datas'], ids=datas['add_float']['ids'])
    def test_add_float(self, a, b, expect):
        assert round(self.cal.add(a, b), 2) == expect

    @pytest.mark.parametrize("a, b, expect", datas['add_minus']['datas'], ids=datas['add_minus']['ids'])
    def test_add_minus(self, a, b, expect):
        assert self.cal.add(a, b) == expect

    @pytest.mark.parametrize("a, b, expect", datas['div_error']['datas'], ids=datas['div_error']['ids'])
    def test_div_error(self, a, b, expect): # 可预期的错误
        with pytest.raises(ZeroDivisionError):
                assert self.cal.div(a, b) == expect

    @pytest.mark.parametrize("a, b, expect", datas['div_int']['datas'], ids=datas['div_int']['ids'])
    def test_div_error(self, a, b, expect):
        assert self.cal.div(a, b) == expect

    # 浮点数取精度进行计算测试
    @pytest.mark.parametrize("a, b, expect", datas['div_float']['datas'], ids=datas['div_float']['ids'])
    def test_div_float(self, a, b, expect):
        assert round(self.cal.div(a, b), 2) == expect

    @pytest.mark.parametrize("a, b, expect", datas['div_minus']['datas'], ids=datas['div_minus']['ids'])
    def test_div_minus(self, a, b, expect):
        assert self.cal.div(a, b) == expect