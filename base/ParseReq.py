from data.data_get import getData


class ParseRequest:
    def __init__(self, filePath):
        self.data = getData(filePath)

    def ParseReq(self, row_count):
        # 逐行读取excel中的数据并返回
        excel_data = {}
        excel_data['case_id'] = self.data.get_case_id(row_count)  # 获取caseId
        excel_data['url'] = self.data.get_request_url(row_count)  # y行不变遍历获取x列的请求地址
        excel_data['method'] = self.data.get_request_method(row_count)  # y行不变遍历获取x列的请求方式
        excel_data['is_run'] = self.data.get_is_run(row_count)  # y行不变遍历获取x列的是否运行
        excel_data['data'] = self.data.get_data_for_json(
            row_count)  # y行不变遍历获取x列的请求数据，这里面时三次调用，依次分别是get_data_for_json丶get_key_words丶get_request_data
        excel_data['header'] = self.data.get_is_token(row_count)  # 根据是否需要token返回不同的header
        excel_data['module'] = self.data.get_module(row_count)
        excel_data['expect_result'] = self.data.get_expect_data(row_count)
        print('url:', excel_data['url'])
        print('模块:', excel_data['module'])
        print('case_id:', excel_data['case_id'])
        print('method:', excel_data['method'])
        print('is_run:', excel_data['is_run'])
        print('data:', excel_data['data'])
        print('header:', excel_data['header'])
        return excel_data