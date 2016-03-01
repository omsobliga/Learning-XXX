#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 正确 send/receive 的方式::

Corrent send: send() + shutdown(WR) + read() == 0 + close()
Corrent receive: read() == 0 + if nothing more to send + close()

Usage:
    python sender/sender.py filename port
"""

import os
import sys
import threading

from common.tcpstream import TcpServer


def sender(accepter, filename):
    SIZE = 8192
    base = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
    f = open(os.path.join(base, filename), 'rb')
    while True:
        data = f.read(SIZE)
        if not data:
            break
        accepter.socket.sendall(data)
    f.close()
    # Wrong close:
    # accepter.close()
    # Right close:
    accepter.shutdown_write()
    while accepter.socket.recv(SIZE):
        continue
    accepter.close()


def run():
    if len(sys.argv) < 3:
        raise Exception('Usage: python sender.py filename port')
    server = TcpServer()
    server.listen(int(sys.argv[2]))
    while True:
        accepter, addr = server.accept()
        print 'Accept addr {}'.format(addr)
        thread = threading.Thread(target=sender, args=(accepter, sys.argv[1], ))
        thread.daemon = True
        thread.start()
    server.close()


if __name__ == '__main__':
    run()
