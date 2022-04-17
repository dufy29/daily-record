# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2022/4/17 14:33
Author : Dufy
File : insert_data.py

读取 txt 插入 MySQL
建表语句：
CREATE TABLE IF NOT EXISTS `lucene_demo2`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `name` VARCHAR(100) COMMENT '描述',
   `pn` VARCHAR(30) NOT NULL,
	 `brand` VARCHAR(20) NOT NULL,
   `submission_date` timestamp DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
   PRIMARY KEY ( `id` ),
	 unique index(`pn` ,`brand`, `name`) COMMENT '多列唯一索引'
)ENGINE=InnoDB DEFAULT CHARSET=utf8

==============================================================================
"""
from utils import *
import pymysql
import pandas as pd
import traceback


class MysqlDataBase(object):
    def __init__(self, db):
        self.conn = pymysql.connect(host="localhost",
                               port=3306,
                               user="root",
                               passwd="123abc",
                               db=db)

    def get_cursor(self):
        """
        创建游标对象
        :return:
        """
        return self.conn.cursor()



if __name__ == "__main__":
    pass
    data_path = datapath(r'data/mobile.txt')
    print(data_path)
    df = pd.read_csv(data_path, sep=':')
    print(df)
    data_base = MysqlDataBase('test')
    cursor = data_base.get_cursor()
    for index, row in df.iterrows():
        # SQL 插入语句
        sql = "INSERT INTO lucene_demo2(" \
              "name, pn, brand) \
               VALUES (%s,%s,%s)"
        param = (row['名称'], row['型号'], row['品牌'])  # param参数是要输入的数据
        try:
            # 执行sql语句
            cursor.execute(sql, param)
            # 提交到数据库执行
            data_base.conn.commit()
        except:
            # 如果发生错误则回滚
            print(traceback.format_exc())
            data_base.conn.rollback()

    # 关闭数据库连接
    data_base.conn.close()
    print('done!')





