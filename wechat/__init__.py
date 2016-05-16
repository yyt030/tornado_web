#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import os
import tornado.web

from .controllers.site import MainHandler


class CreateApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', MainHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
