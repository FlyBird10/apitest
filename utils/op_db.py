import readConfig as readConfig
from utils.Log import MyLog as Log
import redis


localReadConfig = readConfig.ReadConfig()


class MyRedis():
    global host, password, port, db, configRedis
    host = localReadConfig.get_redis("host")
    password = localReadConfig.get_redis("password")
    port = localReadConfig.get_redis("port")
    db = localReadConfig.get_redis("db")
    configRedis = {
        'host': str(host),
        'password': password,
        'port': int(port),
        'db': db
    }

    def __init__(self):
        self.logger = Log.get_log()
        # self.logger = self.log.get_logger()
        self.db = None

    def connect(self):
        try:
            self.re = redis.Redis(**configRedis)
            return self.re
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def getValue(self, key):
        value = self.re.get(key).decode('utf8')  # 转字节为字符
        return value
