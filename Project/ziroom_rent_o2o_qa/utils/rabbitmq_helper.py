import pika

def send_mq_msg(conn, producer_conf):
    channel = conn.channel()
    channel.queue_declare(queue=producer_conf['queue'], durable=True)  # 声明队列以向其发送消息消息
    channel.basic_publish(exchange=producer_conf['exchange'], routing_key=producer_conf['routing_key'],
                          body=producer_conf['body'])
    print('send success msg to rabbitmq')

# 关闭RabbitMQ连接
def close_mq_conn(conn):
    conn.close()


# 获取RabbitMQ连接
def get_mq_conn(conn_conf):
    crdl = pika.PlainCredentials(conn_conf['uname'], conn_conf['passwd'])

    conn = pika.BlockingConnection(pika.ConnectionParameters(
        host=conn_conf['host'], port=conn_conf['port'], virtual_host=conn_conf['vhost'], credentials=crdl))  # 定义连接池

    return conn