# -*- coding: utf-8 -*-
from base.run_method import RunMain
from data.data_get import getData
from data.op_data import DataDepend
from base.ParseRes import Parse
from base.ParseReq import ParseRequest
import sys


class RunTest(object):

    def __init__(self, filePath):
        self.runmain = RunMain()
        self.data = getData(filePath)
        self.depend = DataDepend(filePath)
        self.req = ParseRequest(filePath)
        self.parseRes = Parse(filePath)

    def run(self):
        row_counts = self.data.get_case_lines()  # 获取excel表格行数
        for row_count in range(1, row_counts):
            excel_data = self.req.ParseReq(row_count)  # 读取excel中的数据

            if excel_data['is_run']:
                res = self.runmain.run_main(excel_data['url'], excel_data['method'], excel_data['data'],
                                            excel_data['header'])
                if isinstance(res, dict):  # 请求正常时才写入excel中
                    self.depend.SetParam(excel_data['case_id'], row_counts, res)  # 存储依赖返回的数据
                self.parseRes.parseRes(excel_data['module'], res, excel_data['expect_result'], row_count)
                print(res)
                print("*" * 60 + "分割线" + "*" * 60)

        self.data.set_json('token', None)  # 每次完成测试，清空token
        self.data.set_json('userInfo', None)  # 每次完成测试，清空token


if __name__ == '__main__':
    """
    # 命令行运行时使用
    file = sys.argv[1]  # 接收python命令中的第二个参数
    filePath = None
    if file == 'platform':
        filePath = "../test_data/platform.xls"
    elif file == 'customer':
        filePath = "../test_data/customer.xls"
    # RunTest(filePath).run()
    try:
        RunTest(filePath).run()
    except TypeError as e:
        print('file name is error')
        print('file name only is: platform/customer')
    """
    RunTest("../test_data/platform.xls").run()