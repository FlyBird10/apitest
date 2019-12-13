from base.run_method import RunMain
from data.data_get import getData
from utils.Log import Log
from utils.common import Common
from data.op_data import DataDepend


class Parse:
    def __init__(self, filePath):
        self.runmain = RunMain()
        self.data = getData(filePath)
        self.log = Log()
        self.com = Common()
        self.depend = DataDepend(filePath)

    def _parseRes(self, module, res, expect_result, row_count):
        if "登录" in module:
            act = res['token_type']
            token = res['access_token']
            self.com.Uassert(res, act, expect_result)
            self.data.set_json('token', token)  # token存文件
        elif '基础' in module:
            res_userInfo = res['data']['userInfo']
            userInfo = {}
            userInfo['pkUser'] = res_userInfo['pkUser']
            self.data.set_json('userInfo', userInfo)  # userIfo存文件
        else:
            act = res['message']
            self.com.Uassert(res, act, expect_result)
        self.data.write_data(row_count, 'pass')

    def parseRes(self, module, res, expect_result, row_count):
        try:
            self._parseRes(module, res, expect_result, row_count)
        except Exception as e:
            self.log.error(res.request.url)
            self.log.error(res.request.headers)
            self.log.error(res.request.body)
            self.log.error(res.request.method)
            self.log.error(e)
            self.log.error(res)
            self.data.write_data(row_count, 'fail')
