

def test_search():
    print("开始search")

def test_cart():
    print("开始cart")

# @pytest.mark.usefixtures("login") autouse=True # 没有返回值 装饰器调用
def test_order(connect_db,login):              # 有返回值 函数名调用
    url = f"http://xxxxx.xxx={login}"
    print(url)
    print("开始order")

def test_data(data):
    print(f"测试数据：{data}")
    assert data <5