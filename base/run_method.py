# -*- coding: utf-8 -*-
import requests
from readConfig import ReadConfig
from retrying import retry

localReadConfig = ReadConfig()


class RunMain(object):
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")

    # 请求异常时重试5次，每次随机等待1-2s
    @retry(wait_random_min=1000, wait_random_max=2000, stop_max_attempt_number=5)
    def get_main(self, url, data=None, header=None):
        # res = None
        if header is not None:
            res = requests.get(url=url, data=data, headers=header, timeout=10)
        else:
            res = requests.get(url=url, data=data, timeout=10).json()
        if res.status_code == 200:
            res = res.json()
        return res

    @retry(wait_random_min=1000, wait_random_max=2000, stop_max_attempt_number=5)
    def post_main(self, url, data, header=None):
        # res = None
        if header is not None:
            res = requests.post(url=url, data=data, headers=header, timeout=10)
        else:
            res = requests.post(url=url, data=data, timeout=10)
        if res.status_code == 200:
            res = res.json()
        return res

    def run_main(self, url, method, data=None, header=None):
        url = host + ':' + port + url
        # res = None
        if method.lower() == 'post':
            res = self.post_main(url, data, header)
        elif method.lower() == 'get':
            res = self.get_main(url, data, header)
        else:
            return "what ?????"
        return res