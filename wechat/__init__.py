#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import os
import tornado.web

from .controllers.burts_books_db import MainHandler, RecommendedHandler, BookEditHandler
from .controllers.http_test import IndexHandler, IndexAsyncHandler, IndexAsyncGenHandler
from .controllers.shopping_cart import DetailHandler, CartHandler, StatusHandler,ShoppingCart


class CreateApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', DetailHandler),
            (r'/cart', CartHandler),
            (r'/cart/status', StatusHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True,

        )
        # mongo_client = pymongo.MongoClient(host='localhost', port=27017)
        # self.db = mongo_client['example']
        self.shoppingCart = ShoppingCart()
        tornado.web.Application.__init__(self, handlers, **settings)
