#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import socket

from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer


class SimpleTcpClient:
    clients = set()

    def __init__(self, stream):
        SimpleTcpClient.clients.add(self)
        self.stream = stream
        self.stream.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.stream.socket.setsockopt(socket.IPPROTO_TCP, socket.SO_KEEPALIVE, 1)
        self.stream.set_close_callback(self.on_disconnect)

    @coroutine
    def on_connect(self):
        raddr = 'closed'
        try:
            raddr = '%s:%d' % self.stream.socket.getpeername()
        except Exception:
            pass
        self.log('new, %s' % raddr)
        yield self.dispatch_client()

    @coroutine
    def dispatch_client(self):
        try:
            while True:
                line = yield self.stream.read_until(b'\n')
                self.log('got [%s]' % line)
                yield self.stream.write(line)
        except StreamClosedError:
            pass

    @coroutine
    def on_disconnect(self):
        self.log("disconnected")
        SimpleTcpClient.clients.remove(self)
        yield []

    def log(self, msg, *args, **kwargs):
        print('[connection %d] %s' % (len(SimpleTcpClient.clients), msg.format(*args, **kwargs)))


class SimpleTcpServer(TCPServer):
    @coroutine
    def handle_stream(self, stream, address):
        conn = SimpleTcpClient(stream)
        yield conn.on_connect()


if __name__ == '__main__':
    server = SimpleTcpServer()
    server.bind(8000)
    server.start(1)
    IOLoop.instance().start()
