#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TCP Client.

Send message to Server from stdin.
"""

import socket
import sys

HOST = ''
PORT = 3033


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    handle_write(s)
    s.close()


def handle_write(_socket):
    while True:
        try:
            data = sys.stdin.readline()[0:-1]
            if data == 'q':
                break
        except KeyboardInterrupt:
            break

        _socket.sendall(data)
        data = _socket.recv(1024)
        print 'Received', repr(data)


if __name__ == '__main__':
    main()
