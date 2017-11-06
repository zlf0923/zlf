import unittest
import os
import HTMLTestRunner

test_dir = r"D:\selenium\baidu\case\baidu"

# 用testsuit收集测试用例（测试套件）
# test_suit = unittest.TestSuite()

discover = unittest.defaultTestLoader.discover(test_dir,
                                               pattern="test*.py",
                                               top_level_dir=None)
print(discover)

# 测试用例的集合
# test_suit.addTest(discover)
# print(test_dir)

# 运行用例
# runner = unittest.TextTestRunner()
# runner.run(discover)

# runner.run(test_suit)

report_file = r"D:\selenium\baidu\report\result.html"
fp = open(report_file, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title=u"自动化测试用例",
                                       description=u'用例执行情况：')
runner.run(discover)
fp.close()





# case_path = os.path.join(os.getcwd(), "case")
# # 报告存放路径
# report_path = os.path.join(os.getcwd(),"report")
#
# def all_case():
#     discover = unittest.defaultTestLoader.discover(case_path,
#                                                    pattern="test*.py",
#                                                    top_level_dir=None)
#     print(discover)
#     return discover
#
# if __name__=="__main__":
#     report_path = os.path.join(report_path, "result.html")
#     fp = open(report_path, "wb")
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
#                                            title=u'自动化测试用例',
#                                            description=u'用例执行情况：')
#
#     # 调用add_case函数返回值
#     runner.run(all_case())
#     fp.close()