#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 计算时钟误差

代码逻辑：

- Client: 起一个线程循环发数据，主线程循环读。发的数据中包含时间 T1，
  读的数据包含时间 T2，同时获取当前时间 T3。误差就等于：T2 - (T1 + T3)/2。
- Server: 主程序循环读数据，其中数据包含 T1 的值，然后带上服务端当前的时间 T2，
  发送给 Client。

消息格式：
因为 python 只支持发送 string，所以先发送长度为 3 的字符串表示报文的长度。
例如：030 表示报文长度为 30。再发送具体的报文。

运行：
    python roundtrip_udp.py -s
    python roundtrip_udp.py -c localhost
"""

import logging
logging.basicConfig(level=logging.INFO)

import sys
import socket
import threading
import time

PORT = 3033
DATA_SIZE = 3


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', port))
    while True:
        data_size = int(sock.recv(DATA_SIZE))
        t1, (host, port) = sock.recvfrom(data_size)
        logging.info('Recv from {} {}'.format(host, port))
        t2 = now()
        data = '{},{}'.format(t1, t2)
        sock.sendto(get_data_size(data), (host, port))
        sock.sendto(data, (host, port))


def now():
    return long(time.time() * 1000000)


def get_data_size(data):
    return str(len(data)).zfill(DATA_SIZE)


def client(host, port):

    def send_data(sock, host, port):
        while True:
            data = str(now())
            sock.sendto(get_data_size(data), (host, port))
            sock.sendto(data, (host, port))
            time.sleep(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_thread = threading.Thread(target=send_data, args=(sock, host, port, ))
    send_thread.daemon = True  # 如果主线程退出，子线程也跟着退出
    send_thread.start()

    while True:
        data_size = int(sock.recv(DATA_SIZE))
        data = sock.recv(data_size)
        times = data.split(',')
        t1, t2 = long(times[0]), long(times[1])
        t3 = now()
        logging.info("Now {} round trip {} clock error {}".format(
            t3, t3 - t1, t2 - (t3 + t1) / 2
        ))


def run():
    if sys.argv[1] == '-s':
        server(PORT)
    elif sys.argv[1] == '-c':
        host = sys.argv[2]
        client(host, PORT)


if __name__ == '__main__':
    run()
