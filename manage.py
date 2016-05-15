#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import os
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import parse_command_line, options, define
from tornado.web import Application
from wechat.controllers.site import IndexHandler, MungedPageHandler

if __name__ == '__main__':
    define('port', default=5000, help='run on the given port', type=int, )
    parse_command_line()
    app = Application(
        handlers=[
            (r'/', IndexHandler),
            (r'/poem', MungedPageHandler)
            # (r'/wrap', WrapHandler),
            # (r'/reverse/(\w+)', ReverseHandler)
        ],
        template_path=os.path.join(os.path.dirname(__file__), 'wechat/templates'),
        static_path=os.path.join(os.path.dirname(__file__), 'wechat/static'),
        debug=True,
    )
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    IOLoop.instance().start()
