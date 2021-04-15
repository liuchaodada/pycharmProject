from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:

    def SetUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

    def Teardown(self):
        self.driver.quit()

    def test_demo(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address='127.0.0.1:9222'
        driver = webdriver.Chrome(options=opt)
        self.driver.get("https://www.baidu.com")