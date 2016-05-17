#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import parse_command_line, options, define

from wechat import CreateApp

if __name__ == '__main__':
    define('port', default=8000, help='run on the given port', type=int)
    parse_command_line()
    app = CreateApp()
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    IOLoop.instance().start()
