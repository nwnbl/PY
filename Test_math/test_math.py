from calculate import Math  # 导入Calculate

import unittest  # 导入unitest


class TestMath(unittest.TestCase):  # 测试类，继承unittest里面的testcase类


    def setUp(self):  # setup测试之前的准备
        print("test start")
    
    def test_add(self):  # 定义个变量
        j = Math(5, 10)  # 传入值
        self.assertEqual(j.add(), 15)  # 断言。两个参数，判断第一个参数和第二个参数是不是相等
        #self.assertEqual(j.add(),12)

    def tearDown(self):  # 测试完成后打印测试完成
        print("test end")


if __name__ == '__main__':  # 调试unittest
    suite = unittest.TestSuite()  # 定义变量suite。
    suite.addTest(TestMath("test_add"))  # 调用addtest装载
    runer = unittest.TextTestRunner()  # 运行
    runer.run(suite)
