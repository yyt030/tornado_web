#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import os
import pymongo
import tornado.web

from .controllers.burts_books_db import MainHandler, RecommentHandler, BookModule


class CreateApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/recommended", RecommentHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True,
            ui_modules={'Book': BookModule}

        )
        mongo_client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = mongo_client['example']
        tornado.web.Application.__init__(self, handlers, **settings)
