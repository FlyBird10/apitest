# -*- coding: utf-8 -*-


class global_var:
    id = 0  # id
    module = 1  # 模块
    url = 2  # url
    run = 3  # 是否运行
    request_type = 4  # 请求类型
    request_header = 5  # 是否携带header
    request_token = 6  # 是否携带token
    request_pkManagerCorp = 7  # 是否需要携带pkManagerCorp
    case_depend = 8  # case依赖
    response_data_depend = 9  # 依赖的返回数据
    response_data_depend_need = 10  # 依赖的返回数据中有用的字段  请求数据依赖指定的字段在响应数据的位置
    request_data = 11  # 请求数据
    request_data_depend = 12  # 请求数据依赖 指明请求数据哪些字段依赖其他用例的返回
    expect_result = 13  # 预期结果
    reality_result = 14  # 实际结果


def get_id():
    return global_var.id


def get_module():
    return global_var.module


def get_url():
    return global_var.url


def get_run():
    return global_var.run


def get_request_type():
    return global_var.request_type


def get_request_header():
    return global_var.request_header


def get_case_depend():
    return global_var.case_depend


def get_response_data_depend():
    return global_var.response_data_depend


def get_request_data():
    return global_var.request_data


def get_expect_result():
    return global_var.expect_result


def get_reality_result():
    return global_var.reality_result


def get_request_pkManagerCorp():
    return global_var.request_pkManagerCorp


def get_request_data_depend():
    return global_var.request_data_depend


def get_response_data_depend_need():
    return global_var.response_data_depend_need


# 返回的header类型 默认pkManagerCorp为空
def get_header_value(type='json'):
    if type == 'json':
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'pkManagerCorp': None
        }
    elif type == 'form':
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'pkManagerCorp': None
        }
    elif type == 'multipart':
        headers = {
            'Content-Type': 'multipart/form-data;charset=UTF-8',
            'pkManagerCorp': None
        }
    else:
        headers = None
    return headers


def get_request_token():
    return global_var.request_token

