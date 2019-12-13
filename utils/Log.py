import logging
from datetime import datetime
import threading
import readConfig
import os


class Log:
    def __init__(self):
        global logPath,  proDir
        proDir = readConfig.proDir
        self.resultPath = os.path.join(proDir, "result")
        # 配置log文件名称
        self.logname = os.path.join(self.resultPath, '%s.log' % datetime.now().strftime('%Y_%m_%d'))
        self.logname_error = os.path.join(self.resultPath, '%s-error.log' % datetime.now().strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        # 日志输出格式
        self.formatter = logging.Formatter(
            '[%(asctime)s] - %(filename)s[line:%(lineno)d] - fuc:%(funcName)s- %(levelname)s: %(message)s')

    def __console(self, level, message):
        if level == 'info':
            # 创建一个FileHandler，用于写到本地
            fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 追加模式
            fh.setLevel(logging.INFO)
            fh.setFormatter(self.formatter)
            self.logger.addHandler(fh)
            self.logger.info(message)
            self.logger.removeHandler(fh)
            # 关闭打开的文件
            fh.close()
        elif level == 'error':
            # 创建一个FileHandler，用于写到本地
            fh_error = logging.FileHandler(self.logname_error, 'a', encoding='utf-8')  # 追加模式
            fh_error.setLevel(logging.ERROR)
            fh_error.setFormatter(self.formatter)
            self.logger.addHandler(fh_error)
            self.logger.error(message)
            self.logger.removeHandler(fh_error)
            # 关闭打开的文件
            fh_error.close()
        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        self.logger.removeHandler(ch)

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


class MyLog:
    log = None
    mutex = threading.Lock()  # 获取同步锁对象

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()  # 获得锁
            MyLog.log = Log()
            MyLog.mutex.release()  # 释放锁

        return MyLog.log
