# coding:utf-8

"""
@author: smartgang
@contact: zhangxingang92@qq.com
@file: IpDataHelper.py
@time: 2017/12/19 18:33
"""
from db.SqliteHelper import SqliteHelper
from config import DB_CONFIG_FILE
from config import DB_CONFIG_TABLE


class IpDataHelper(SqliteHelper):
    '''
    proxy ip data
    ip:,port:,types:,protocol:,country:,area:,speed:
    '''

    def __init__(self):
        self.index = 0

    def initdb(self):
        self.sqlhelper = SqliteHelper(DB_CONFIG_FILE)

    def __del__(self):
        del self

    def create(self):
        create_table_sql = '''CREATE TABLE %s (
                                      `id` int(10) NOT NULL,
                                      `ip` varchar(16) DEFAULT NULL,
                                      `port` int DEFAULT NULL,
                                      `types` int DEFAULT NULL,
                                      `protocol` int DEFAULT NULL,
                                      `country` varchar(100) DEFAULT NULL,
                                      `area` varchar(100) DEFAULT NULL,
                                      `speed` int DEFAULT NULL,
                                      `score` int DEFAULT NULL,
                                       PRIMARY KEY (`id`)
                                    )''' % DB_CONFIG_TABLE
        self.sqlhelper.create(create_table_sql)

    def insert(self, data):
        '''
        insert items
        :param data:data tuple
        :return:
        '''
        save_sql = 'INSERT INTO %s values (?, ?, ?, ?, ?, ?, ?, ?, ?)' % DB_CONFIG_TABLE
        self.sqlhelper.insert(save_sql, data)

if __name__ == '__main__':
    ip = IpDataHelper()
    ip.initdb()
    ip.create()
    data = [(1, '192.168.1.1', 8080, 0, 0, u'中国', u'吉林', 0, 0),
            (2, '192.168.1.10', 5050, 0, 0, u'中国', u'长春', 0, 0)]
    ip.insert(data)
