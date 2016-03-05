#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 测试 NODELAY 对延迟率的影响

Usage::
    python nodelay/nodelay_server.py -p 3033
    python nodelay/nodelay_client.py -p 3033 -l 1024 -c 10
    python nodelay/nodelay_client.py -p 3033 -l 1024 -c 10 -nd  # set nodelay

TODO:
- 未成功复现 set_nodelay 之后对延迟率的影响
"""

import argparse
import time

from common.tcpstream import TcpClient

INT_LENGTH = 8


def parse_args():
    parser = argparse.ArgumentParser(description="Allowed options")
    parser.add_argument('-b', nargs='?', const=True, default=False,
                        help='buffer')
    parser.add_argument('-nd', nargs='?', const=True, default=False,
                        help='delay')
    parser.add_argument('-ht', nargs='?', const='localhost',
                        default='localhost', help='host')
    parser.add_argument('-p', help='port')
    parser.add_argument('-l', nargs='?', const=1024, default=1024,
                        help='buffer length')
    parser.add_argument('-c', nargs='?', const=10, default=10,
                        help='buffer count')
    args = parser.parse_args()
    return args


def now():
    return time.time()


def run(args):
    host, port = args.ht, int(args.p)
    tcp_client = TcpClient()
    stream = tcp_client.connect(host, port)
    if args.nd:
        print 'set nodelay'
        stream.set_nodelay()

    length = int(args.l)
    fixed_length = str(length).zfill(INT_LENGTH)
    start = now()
    count = int(args.c)
    for i in xrange(count):
        if args.b:
            data = fixed_length + 'S' * length
            stream.socket.sendall(data)
            # time.sleep(0.001)  # prevent kernel merging TCP segments
            print '{} send {} bytes.'.format(now(), length + INT_LENGTH)
        else:
            stream.socket.sendall(fixed_length)
            # time.sleep(0.001)
            data = 'S' * length
            stream.socket.sendall(data)
            print '{} send {} bytes.'.format(now(), length)

    print 'send {} senconds.'.format(now() - start)

    for i in xrange(count):
        ack = stream.recvall(INT_LENGTH)
        print '{} recv {} bytes.'.format(now(), len(ack))

    print 'recv {} senconds.'.format(now() - start)
    stream.close()


if __name__ == '__main__':
    args = parse_args()
    run(args)
