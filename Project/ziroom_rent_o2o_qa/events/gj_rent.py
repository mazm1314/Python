import json
import time

from assertpy import assert_that

from utils.mysql_helper import *
from utils.rabbitmq_helper import *


# 获取RabbitMQ连接设置
def get_mq_conn_conf():
    mq_conn_conf = dict()
    mq_conn_conf['uname'] = 'crm_rabbit_write'
    mq_conn_conf['passwd'] = 'crm_rabbit_write'
    mq_conn_conf['host'] = '10.16.9.34'
    mq_conn_conf['port'] = 5672
    mq_conn_conf['vhost'] = 'crm'

    return mq_conn_conf


# 获取RabbitMQ消息发送设置
def get_mq_producer_conf():
    mq_producer_conf = dict()
    mq_producer_conf['queue'] = 'channel_task.rent.GuanJiaRentHouse'
    mq_producer_conf['exchange'] = 'crm.test'
    mq_producer_conf['routing_key'] = 'rent.sign.contract.payed.confirmed.renter'

    return mq_producer_conf


# 获取MySQL连接设置
def get_mysql_conn_conf():
    mysql_conn_conf = dict()
    mysql_conn_conf['uname'] = 'dev_web'
    mysql_conn_conf['passwd'] = 'ziroomdb'
    mysql_conn_conf['host'] = '10.16.16.15'
    mysql_conn_conf['port'] = 3306
    mysql_conn_conf['db'] = 'wxziroom'
    mysql_conn_conf['charset'] = 'utf8'

    return mysql_conn_conf


# 构造厨房数据
def get_rent_house_data():
    body = dict()
    body['contractCode'] = 'BJZYCW81911270012'
    body['houseSourceCode'] = 'BJZRGY0819320096_01'
    body['keeperCode'] = '60000774'
    body['directChannel'] = 1
    body['resign'] = 0
    body['cityCode'] = '110000'
    body['signTime'] = '2019-11-27 15:05:19'
    return body


if __name__ == '__main__':
    mq_conn_conf = get_mq_conn_conf()
    mq_conn = get_mq_conn(mq_conn_conf)

    mq_producer_conf = get_mq_producer_conf()
    body = get_rent_house_data()
    mq_producer_conf['body'] = json.dumps(body)

    send_mq_msg(mq_conn, mq_producer_conf)

    close_mq_conn(mq_conn)

    time.sleep(3)

    mysql_conn_conf = get_mysql_conn_conf()

    mysql_conn = get_mysql_conn(mysql_conn_conf)

    sql = """
        SELECT * FROM gj_message_queue ORDER BY id DESC LIMIT 1;
        """
    ret = get_info_mysql(mysql_conn, sql)
    print(ret)

    close_mysql_conn(mysql_conn)

    assert_that(ret['system_code']).is_equal_to(body['keeperCode'])
    assert_that(ret['resign']).is_equal_to(body['resign'])
    assert_that(ret['contract_code']).is_equal_to(body['contractCode'])
    assert_that(ret['house_code']).is_equal_to(body['houseSourceCode'])
