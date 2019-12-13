import json


class operationJson(object):
    def __init__(self, file_path="../test_data/request_data.json"):
        self.file_path = file_path
        self.data = self.get_data()

    def get_data(self):
        with open(self.file_path) as f:
            data = json.load(f)
            return data

    def get_key_words(self, key=None):
        if key:
            return self.data[key]
        else:
            return self.data

    # 修改json文件：json转dict后修改dict，再把修改后的dict用dump存入文件
    def set_data(self, key, value):
        data = self.get_data()
        if data[key] is None:  # key不为空时修改其value
            data[key] = value
            with open(self.file_path, 'w') as f:
                json.dump(data, f)
            return True
        elif value is None:  # 删除某个key的值
            data[key] = value
            with open(self.file_path, 'w') as f:
                json.dump(data, f)
            return True
        else:
            return 'modify fail'

    def set_data_more(self, key_top, key_second, value):
        data = self.get_data()
        if isinstance(data[key_top], dict):
            data[key_top][key_second] = value
            with open(self.file_path, 'w') as f:
                json.dump(data, f)
            return True
        else:
            return 'modify fail'

    def get_data_more(self, key_top, key_second):
        data = self.get_data()
        value = data[key_top][key_second]
        return value


if __name__ == '__main__':
    # print(operationJson().get_key_words())
    # print(operationJson().get_key_words("token"))
    print(operationJson().get_data_more('addDept_001', 'deptName'))