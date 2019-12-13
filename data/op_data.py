# -*- coding: utf-8 -*-
from data.data_get import getData
import json
from utils.op_json import operationJson


class DataDepend():
    """
    处理用例中数据依赖
    """
    def __init__(self, filePath):
        self.data = getData(filePath)
        self.json = operationJson()

    """依赖返回的数据存入excel对应行"""
    def SetParam(self, case_id, row_counts, DependRes):
       for x in range(1, row_counts):
           ex_case = self.data.get_case_depend(x)
           if ex_case == case_id:
               self.data.write_depend_res(x, json.dumps(DependRes))

    # 修改请求数据依赖的值
    def setRequestDepend(self, x, values):
        data_depend = self.data.get_request_data_depend(x)
        print('请求依赖的字段：', data_depend)
        data_list = data_depend.split(';')
        i = 0
        for l in data_list:
            topKey, secondKey = l.split('.')
            if isinstance(values, list):
                self.json.set_data_more(topKey, secondKey, values[i])
            else:
                self.json.set_data_more(topKey, secondKey, values)
            i = i+1
        return 'success'

    # 读取某行的依赖数据（其所依赖的case在之前执行时已存入所需的对应行中），
    # 在依赖返回的所有数据中按所需字段提取出来后按请求所需字段设置到json文件中
    def getResDepend(self, x):
        res_data = self.data.get_response_data_depend(x)
        res_data_dict = json.loads(res_data)
        res_data_need = self.data.get_response_data_depend_need(x)
        res_data_need_list = res_data_need.split(';')
        print('依赖数据中有用的字段：', res_data_need_list)
        for l in res_data_need_list:
            topKey, secondKey = l.split('.')
            objs = res_data_dict[topKey]
            for obj in objs:
                value = obj[secondKey]  # 在依赖返回的所有数据中按所需字段提取
                self.setRequestDepend(x, value)  # 按请求所需字段设置到json文件中
                break


if __name__ == '__main__':
    data = DataDepend("../test_data/platform.xls")
    print(data.getResDepend(4))




