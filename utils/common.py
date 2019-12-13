import unittest
from utils.Log import MyLog


class Common(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.logger = MyLog.get_log()

    # 断言处理
    def Uassert(self, response, actualResult, ExpectedResult=None, mode='Equal', msg=None):
        try:
            if mode == 'Equal':
                self.assertEqual(ExpectedResult, actualResult, msg=msg)  # 不相等时抛异常
            elif mode == 'NotEqual':
                self.assertNotEqual(ExpectedResult, actualResult, msg=msg)  # 相等时抛异常
            elif mode == 'assertIn':
                self.assertIn(actualResult, ExpectedResult, msg=msg)  # 前者不是后面的子集时抛异常
            elif mode == 'NotIn':
                self.assertNotIn(actualResult, ExpectedResult, msg=msg)  # 前者是后面的子集时抛异常
            elif mode == 'NotNone':
                self.assertIsNotNone(actualResult, msg=msg)
            elif mode == 'None':
                self.assertIsNone(actualResult, msg=msg)

        except Exception as e:

            self.logger.error(self.http.headers)  # 断言失败时保存接口参数、token和接口路径
            self.logger.error(self.http.data)
            self.logger.error(self.http.url)
            self.logger.error(e)
            self.logger.error(response.text)
            raise self.failureException  # 抛出异常使用例执行fail
