import pymysql


# 获取一条查询信息
def get_info_mysql(conn, sql):
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 定义要执行的SQL语句
    sql = sql
    # 执行SQL语句
    cursor.execute(sql)
    ret = cursor.fetchone()
    cursor.close()
    return ret


# 关闭MySQL连接
def close_mysql_conn(conn):
    conn.close()


# 获取MySQL连接
def get_mysql_conn(conn_conf):
    conn = pymysql.connect(
        host=conn_conf['host'],
        port=conn_conf['port'],
        user=conn_conf['uname'],
        password=conn_conf['passwd'],
        database=conn_conf['db'],
        charset=conn_conf['charset']
    )

    return conn
