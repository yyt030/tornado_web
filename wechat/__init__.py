#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import os
import pymongo
import tornado.web
from .controllers.definitions_readonly import WordHandler
from .controllers.hello_module import HelloHandler, HelloModule, RecommentHandler, BookModule
from .controllers.site import MainHandler


class CreateApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/(\w+)', WordHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True,
        )
        mongo_client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = mongo_client['example']
        tornado.web.Application.__init__(self, handlers, **settings)
