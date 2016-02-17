#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" TTCP 实现：测试网络吞吐量。

通信逻辑：

1. Client 发送 number 个长度为 length 的数据。
   Client 每发送一个数据包后，等接收到 Server 发送的 ACK 后再接着发送。
2. Server 不断接受数据。每接受一个数据，就发送一个 ACK 给 Client。

Usage:

    `python ttcp_blocking.py -r localhost -p 3333 -l 1024 -n 100000`
    `python ttcp_blocking.py -t localhost -p 3333 -l 1024 -n 100000`
"""

import logging
logging.basicConfig(level=logging.INFO)

import argparse
import socket
import time


def get_acceptted_socket(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置 SO_REUSEADDR，端口释放后立即就可以再次被使用
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(5)
    conn, addr = sock.accept()
    logging.info('Accept addr {}'.format(addr))
    sock.close()
    return conn


def get_connectted_socket(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    logging.info('Connection host {} port {}'.format(host, port))
    return sock


def read_n(sock, length):
    """仅支持 string 类型"""
    nread = 0
    total_data = ''
    while nread < length:
        data = sock.recv(length - nread)
        nr = len(data)
        if nr > 0:
            nread += nr
            total_data += data
        elif nr == 0:
            break
    assert len(total_data) == nread  # 已读完
    return total_data


def write_n(sock, data, length):
    """仅支持 string 类型"""
    assert len(data) == length  # 检查长度是否一致
    written = 0
    while written < length:
        nw = sock.send(data)
        if nw > 0:
            written += nw
        elif nw == 0:
            break
    assert length == written  # 已写完
    return written


def transmit(host, port, buffer_length, number_buffers):
    """ 发送数据
    """
    sock = get_connectted_socket(host, port)
    buffer = 'A' * buffer_length
    total_mb = 1.0 * buffer_length * number_buffers / 1024 / 1024
    logging.info('{:.3f} MiB in total\n'.format(total_mb))

    start_time = int(time.time())
    for i in xrange(number_buffers):
        write_n(sock, buffer, buffer_length)
        read_n(sock, len('ACK'))
    end_time = int(time.time())

    logging.info('{:.3f} seconds in total'.format(end_time - start_time))
    logging.info('{:.3f} MiB/s'.format(total_mb / (end_time - start_time)))

    sock.close()


def receive(host, port, buffer_length, number_buffers):
    """ 接受数据
    """
    sock = get_acceptted_socket(host, port)
    for i in xrange(number_buffers):
        read_n(sock, buffer_length)
        write_n(sock, 'ACK', len('ACK'))
    sock.close()


def parse_args():
    """ 解析参数
    """
    parser = argparse.ArgumentParser(description="Allowed options")
    parser.add_argument('-p', help='TCP port')
    parser.add_argument('-l', help='Buffer Length')
    parser.add_argument('-n', help='Number of buffers')
    parser.add_argument('-t', help='Transmit host')
    parser.add_argument('-r', help='Receive')
    parser.add_argument('-nd', help='set TCP_NODELAY')  # TODO
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    try:
        if args.t:
            transmit(args.t, int(args.p), int(args.l), int(args.n))
        elif args.r:
            receive(args.r, int(args.p), int(args.l), int(args.n))
        else:
            assert False, 'Set -t or -r'
    except TypeError:
        logging.error('Set -t/-r -p -l -n. Example: python ttcp_blocking.py -r localhost -p 3333 -l 1000 -n 100000')


if __name__ == '__main__':
    main()
