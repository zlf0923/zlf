import unittest
from selenium import webdriver

class Test1(unittest.TestCase):
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
        print("测试百度的案例")

    def test_02(self):
        '''测试百度搜索：yellow'''
        self.driver.find_element_by_id("kw").send_keys("yellow")

if __name__ == "__main__":
    unittest.main()