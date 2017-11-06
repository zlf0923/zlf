import unittest
from selenium import webdriver
import time

class Test1(unittest.TestCase):
    u'''测试百度搜索'''
    def setUp(self):
        print("start!")
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(30)

    def tearDown(self):
        print("end!")
        self.driver.quit()

    def test_01(self):
        '''测试百度搜索：blue'''
        self.driver.find_element_by_id("kw").send_keys("blue")
        self.driver.find_element_by_id("su").click()
        time.sleep(1)
        print("测试百度的案例")

    def test_02(self):
        '''测试百度搜索：yellow'''
        self.driver.find_element_by_id("kw").send_keys("yellow")
        self.driver.find_element_by_id("su").click()
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()