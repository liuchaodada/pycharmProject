import pytest
from .calculator import Calculator
import yaml

@pytest.fixture(scope="class")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")

def open_files():
    with open("data_calc.yml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data

def get_data():
    add_datas = open_files()['add_int']['datas']
    add_ids = open_files()['add_int']['ids']
    return add_datas,add_ids

@pytest.fixture(params=get_data()[0],ids=get_data()[1])
def get_datas(request):
    return request.param

@pytest.fixture()
def login():
    print("开始login")
    token = "xadafasf3dafaf"
    return token

@pytest.fixture()
def open():
    print("open browser")
    yield

    print("执行 teardwon")

    print("close browser")

@pytest.fixture()
def connect_db():
    print("开始connect db")
    yield
    print("关闭connect db")

