#_*_ coding:utf-8 _*_

import time
import MySQLdb

def get_time_str():
    l = time.localtime()
    res = ''
    for i in l:
        res += str(i)
    return res


#
# Exexute sql statements for database 4bbs
#

def execute_sql_in_4bbs(sql,l):
    conn = MySQLdb.connect(host='localhost',user='root',passwd='666666')
    cursor = conn.cursor()
    conn.select_db('4bbs')
    if l == 'SHOW':
        count = cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        conn.close()
        return (count,res)
    res = cursor.execute(sql,l)
        
    conn.commit()
    conn.close()
    return res


