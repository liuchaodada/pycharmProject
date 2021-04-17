import time
import yaml
from selenium import webdriver


class TestWeChatWork:

    # 复用浏览器获得cookie 保存在yaml中
    # 在linux平台 root用户安装的chrome需要 --no-sandbox运行
    # 如果再报错需要配置 chrome应用和chromedriver的位置

    def test_get_cookie(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--no-sandbox')
        options.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookie = driver.get_cookies()
        print(cookie)
        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)


    # 获取已有cookies 加入driver 可免扫码登录
    def test_login(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(2)