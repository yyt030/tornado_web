#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html',
                    page_title='Yan tao',
                    header_text="Welcome to Yantao's books")


class RecommentHandler(tornado.web.RequestHandler):
    def get(self):
        coll = self.application.db.books
        books = coll.find()
        self.render('recommended.html',
                    page_title="Burt's Books | Recommended Reading",
                    header_text="Recommended Reading",
                    books=books
                    )


class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string("modules/book.html", book=book)

    def css_files(self):
        return "/static/css/recommended.css"

    def javascript_files(self):
        return "/static/js/recommended.js"
