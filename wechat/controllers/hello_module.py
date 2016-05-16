#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import tornado.web


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('hello.html')


class HelloModule(tornado.web.UIModule):
    def render(self):
        return '<h1>Hello, world!</h1>'


class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string(
            "modules/book.html",
            book=book,
        )

    def embedded_javascript(self):
        return ".book {background-color:#F5F5F5}"


class RecommentHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('recommended.html',
                    page_title="Yantao's Books",
                    header_text="Recommended Reading",
                    books=[{
                        "title": "Programming Colleer",
                        "subtitle": "Building Smart Web 2.0 Applications",
                        "image": "/static/images/collective_intelligence.gif",
                        "author": "Toby Segaran",
                        "date_added": 1310248056,
                        "date_released": "August 2007",
                        "isbn": "978-0-596-52932-1",
                        "description": "<p>This fascinating book demonstrates how you "
                                       "can build web applications to mine the enormous amount of data created by people "
                                       "on the Internet. With the sophisticated algorithms in this book, you can write "
                                       "smart programs to access interesting datasets from other web sites, collect data "
                                       "from users of your own applications, and analyze and understand the data once "
                                       "you've found it.</p>"
                    }
                    ])
