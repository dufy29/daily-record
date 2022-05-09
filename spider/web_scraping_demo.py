# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2022/5/9 23:36
File : web_scraping_demo.py

网页抓取demo
实现对网页内 所有链接的抓取
参考：[如何用Python爬数据？（一）网页抓取](https://zhuanlan.zhihu.com/p/34206711)
==============================================================================
"""

import traceback
from requests_html import HTMLSession
from mysql.insert_data import MysqlDataBase


# 根据之前的提取过程，自动提取所有文本和链接
def get_text_link_from_sel(sel):
    mylist = []
    try:
        results = r.html.find(sel)
        for result in results:
            mytext = result.text
            mylink = list(result.absolute_links)[0]
            mylist.append((mytext, mylink))
        return mylist
    except:
        return None


if __name__ == "__main__":
    pass
    session = HTMLSession()
    url= 'https://www.jianshu.com/p/85f4624485b9'
    r = session.get(url)
    print(r.html.text)

    sel = '#__next > div._21bLU4._3kbg6I > div > div._gp-ck > section:nth-child(1) > article > p > a'
    res = get_text_link_from_sel(sel)
    print(res, len(res))

    data_base = MysqlDataBase('test')
    cursor = data_base.get_cursor()
    for i in res:
        # SQL 插入语句
        sql = "INSERT INTO text_links(" \
              "text, link) \
               VALUES (%s,%s)"
        param = (i[0], i[1])  # param参数是要输入的数据
        try:
            # 执行sql语句
            cursor.execute(sql, param)
            # 提交到数据库执行
            data_base.conn.commit()
        except:
            # 如果发生错误则回滚
            # print(traceback.format_exc())
            data_base.conn.rollback()

    count = cursor.execute("select * from text_links")
    print(f'总共插入：{count}条')

    # 关闭数据库连接
    data_base.conn.close()
    print('done!')



