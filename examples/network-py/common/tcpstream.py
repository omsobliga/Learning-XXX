#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket


class TcpServer(object):

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置 SO_REUSEADDR，端口释放后立即就可以再次被使用
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def listen(self, port):
        self.socket.bind(('', port))  # '' 表示可以绑定任何 IP
        self.socket.listen(5)

    def accept(self):
        conn, addr = self.socket.accept()
        return IOStream(conn), addr

    def close(self):
        self.socket.close()


class TcpClient(object):

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.socket.connect((host, port))
        return IOStream(self.socket)

    def close(self):
        self.socket.close()


class IOStream(object):

    def __init__(self, socket):
        self.socket = socket

    def shutdown_read(self):
        self.socket.shutdown(socket.SHUT_RD)

    def shutdown_write(self):
        self.socket.shutdown(socket.SHUT_WR)

    def close(self):
        self.socket.close()
