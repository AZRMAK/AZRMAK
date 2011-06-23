#_*_ coding:utf-8 _*_

import MySQLdb

def create_all_tables():
    """
    create all database * tables
    database = 4bbs
    """
    conn = MySQLdb.connect(host='localhost',user='root',passwd='666666')
    cursor = conn.cursor()

    # create 4bbs database
    sql = """create database if not exists 4bbs"""
    try:
        cursor.execute(sql)
    except:
        pass

    # select database 4bbs
    conn.select_db('4bbs')
    
    # create table 'kind'
    sql = """create table kind (kind_id bigint,kind_name char(20),kind_count bigint,kind_shortname char(20))"""
    try:
        cursor.execute(sql)
    except:
        pass

    # create table 'post'
    sql = """create table post (kind_id bigint,post_tittle char(50),post_date char(20),post_id bigint,
            post_content varchar(200),user_id bigint)
          """
    try:
        cursor.execute(sql)
    except:
        pass
    
    # create table 'comment'
    sql = """create table comment (comment_id bigint,comment_content varchar(200),comment_date char(20),
            post_id bigint,user_id bigint)
          """
    try:
        cursor.execute(sql)
    except:
        pass
    
    # create table 'user'
    sql = """
            create table user (user_id bigint,user_name char(20),user_password char(20))
          """
    try:
        cursor.execute(sql)
    except:
        pass

    conn.commit()
    conn.close()
    print "All done!" 

def test_database():
    """test database"""
    conn = MySQLdb.connect(host='localhost',user='root',passwd='666666')
    cursor = conn.cursor()
    
    sql = ""
    res = cursor.execute(sql)
    print res
    conn.close()

def main():
    """main"""
    create_all_tables()
    
if __name__ == '__main__':
    main()  

