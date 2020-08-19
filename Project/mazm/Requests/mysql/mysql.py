import pymysql

class MysqlDB():
    def __init__(self,host,port,user,passwd,db):
        # 建立数据库连接
        self.conn=pymysql.Connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db
        )

        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql):
        """查询"""
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data

    def execute_db(self, sql):
        """更新/插入/删除"""
        try:
            # 使用 execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print("操作出现错误：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()

    if __name__ == '__main__':
        db = MysqlDb("192.168.89.128", 3306, "root", "123456", "test2020")

        select_sql = 'SELECT * FROM user WHERE username="张三2"'
        update_sql = 'UPDATE user SET username = "张三2" WHERE id = 1'
        insert_sql = 'INSERT INTO user(id, username, password) VALUES(11, "王五", "333333")'
        delete_sql = 'DELETE FROM user WHERE id = 11'

        data = db.select_db(select_sql)
        print(data)
        db.execute_db(update_sql)
        db.execute_db(insert_sql)
        db.execute_db(delete_sql)