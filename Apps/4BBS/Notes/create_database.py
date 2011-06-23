#_*_ coding:utf-8 _*_
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8') 

import MySQLdb



def create_database_and_table(database,table_name):
    conn = MySQLdb.connect(host="localhost",user="root",passwd="666666")
    cursor = conn.cursor()
    sql = "create database if not exists %s" % database
    cursor.execute(sql)
    conn.select_db(database)
    sql = "create table %s (id int,info varchar(100))" % table_name
    cursor.execute(sql)
    conn.commit()
    conn.close()

def insert(id,info):
    conn = MySQLdb.connect(host="localhost",user="root",passwd="666666")
    cursor = conn.cursor()
    conn.select_db("mak")
    sql = "insert into test values(%s,%s)" 
    cursor.execute(sql,[id,info])
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database_and_table("Mak","test")
    insert(3,"大家好吗!")
    
  
