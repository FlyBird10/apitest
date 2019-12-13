# -*- coding: utf-8 -*-

from utils.op_excel import operationExcel
from utils.op_json import operationJson
from data import data_conf
from utils.op_db import MyRedis


class getData(object):
    def __init__(self, filePath):
        self.op_excel = operationExcel(filePath)

    def get_case_lines(self):
        """获取表格行数"""
        return self.op_excel.get_rows()

    def get_case_id(self, x):
        """获取caseID"""
        y = data_conf.get_id()
        case_id = self.op_excel.get_cell_value(x, y)
        return case_id

    def get_module(self, x):
        """获取测试模块"""
        y = data_conf.get_module()
        module_value = self.op_excel.get_cell_value(x, y,)
        return module_value

    def get_is_run(self, x):
        """获取case是否运行"""
        flag = None
        y = data_conf.get_run()
        run_value = self.op_excel.get_cell_value(x, y)
        if run_value == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def get_is_header(self, x):
        """是否携带header"""
        y = data_conf.get_request_header()
        header = self.op_excel.get_cell_value(x, y)
        if header != '':
            return data_conf.get_header_value(header)
        else:
            return None

    def get_is_token(self, x):
        y = data_conf.get_request_token()
        is_token = self.op_excel.get_cell_value(x, y)
        y_pk = data_conf.get_request_pkManagerCorp()
        is_pk = self.op_excel.get_cell_value(x, y_pk)
        header = self.get_is_header(x)
        op_json = operationJson()

        if is_token == 'yes' and is_pk == 'yes':  # token和pkManagerCorp同时需要
            pkUser = op_json.get_data_more('userInfo', 'pkUser')
            pkManagerCorp = self.get_pkManagerCorp(pkUser)
            token = self.get_by_key("token")
            header["Authorization"] = "Bearer " + token
            header['pkManagerCorp'] = pkManagerCorp
        elif is_pk == 'no' and is_token == 'yes':  # 只需要token，暂时不存在只需要pkManagerCorp
            token = self.get_by_key("token")
            header["Authorization"] = "Bearer " + token

        return header

    def get_request_method(self, x):
        """获取请求方式"""
        y = data_conf.get_request_type()
        request_method = self.op_excel.get_cell_value(x, y)
        return request_method

    def get_request_url(self, x):
        """获取请求地址"""
        y = data_conf.get_url()
        request_url = self.op_excel.get_cell_value(x, y)
        return request_url

    def get_request_data(self, x):
        """获取请求数据"""
        y = data_conf.get_request_data()
        request_data = self.op_excel.get_cell_value(x, y)
        if request_data == '':
            return None
        return request_data

    def get_data_for_json(self, x):
        """通过excel中的关键字去获取json数据"""
        op_json = operationJson()
        data = op_json.get_key_words(self.get_request_data(x))
        return data

    def get_expect_data(self, x):
        """获取预期结果数据"""
        y = data_conf.get_expect_result()
        expect_data = self.op_excel.get_cell_value(x, y)
        if expect_data == '':
            return None
        return expect_data

    def write_data(self, x, data):
        '''写入测试结果'''
        y = data_conf.get_reality_result()
        self.op_excel.write_result_data(x, y, data)

    def write_depend_res(self, x, data):
        """写入依赖返回的字段"""
        y = data_conf.get_response_data_depend()
        self.op_excel.write_result_data(x, y, data)

    def set_json(self, key, value):
        op_json = operationJson()
        result = op_json.set_data(key, value)
        return result

    def get_by_key(self, key):
        op_json = operationJson()
        result = op_json.get_key_words(key)
        return result

    def get_case_depend(self, x):
        """返回依赖的caseID"""
        y = data_conf.get_case_depend()
        depend_value = self.op_excel.get_cell_value(x, y)
        return depend_value

    def get_pkUser(self, key):
        """获取登录账号的用户主键"""
        op_json = operationJson()
        result = op_json.get_key_words(key)
        pkUser = result['pkUser']
        return pkUser

    def get_pkManagerCorp(self, pkUser):
        redis = MyRedis()
        redis.connect()
        pkCorp = redis.getValue(pkUser)  # 通过pkUser去redis中查询对应的pkCorp
        return pkCorp

    def get_request_data_depend(self, x):
        y = data_conf.get_request_data_depend()
        value = self.op_excel.get_cell_value(x, y)
        return value

    def get_response_data_depend(self, x):
        y = data_conf.get_response_data_depend()
        value = self.op_excel.get_cell_value(x, y)
        return value

    def get_response_data_depend_need(self, x):
        y = data_conf.get_response_data_depend_need()
        value = self.op_excel.get_cell_value(x, y)
        return value


if __name__ == '__main__':
    caseData = getData("../test_data/platform.xls")
    print(caseData.get_case_lines())
    print(caseData.get_is_run(2))
    print(caseData.get_request_data(4))
    print(caseData.get_data_for_json(4))