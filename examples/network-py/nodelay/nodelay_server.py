#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 测试 NODELAY 对延迟率的影响
"""

import argparse
import time

from common.tcpstream import TcpServer

INT_LENGTH = 8


def parse_args():
    parser = argparse.ArgumentParser(description="Allowed options")
    parser.add_argument('-nd', nargs='?', const=True, default=False,
                        help='delay')
    parser.add_argument('-p', help='port')
    args = parser.parse_args()
    return args


def now():
    return time.time()


def run(args):
    port = int(args.p)
    tcp_server = TcpServer()
    tcp_server.listen(port)
    while True:
        stream, addr = tcp_server.accept()
        print 'Accept add {}'.format(addr)

        if args.nd:
            stream.set_nodelay()

        while True:
            data_length = stream.recvall(INT_LENGTH)
            if len(data_length) <= 0:
                break

            data = stream.recvall(int(data_length))
            assert len(data) == int(data_length)

            print '{} recv {} bytes.'.format(now(), len(data))

            ack = str(len(data)).zfill(INT_LENGTH)
            stream.socket.sendall(ack)
            print '{} send {} bytes.'.format(now(), len(ack))


if __name__ == '__main__':
    args = parse_args()
    run(args)
