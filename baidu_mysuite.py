from bigbaidu.ditu import Ditu
import unittest
import HTMLTestRunner

if __name__ == "__main__":

    my_suite=unittest.TestSuite()

    my_suite.addTest(Ditu('test_ditu'))
    my_suite.addTest(Ditu('test_tieba'))
    my_suite.addTest(Ditu('test_xinwen'))

    # my_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Yihaodian))
    filename1 = "result.html"
    fp = open(filename1, 'wb')
    # 定义测试报告的路径，标题，描述等内容
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'自动化测试报告')
    # 执行测试脚本，并生成测试报告runner.run(suite)



    # runner = unittest.TextTestRunner(verbosity=2)
    runner.run(my_suite)


