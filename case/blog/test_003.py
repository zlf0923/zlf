import unittest
import  time

class Test(unittest.TestCase):
    def setUp(self):
        print("start!")

    def tearDown(self):
        print("end!")

    def test01(self):
        print("执行测试用例01")

    def test02(self):
        print("执行测试用例02")

    def test03(self):
        print("执行测试用例03")

if __name__ == "__main__":
    unittest.main()