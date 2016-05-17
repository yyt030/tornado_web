#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import time

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html',
                    page_title='Yan tao',
                    header_text="Welcome to Yantao's books")


class RecommendedHandler(tornado.web.RequestHandler):
    def get(self):
        coll = self.application.db.books
        books = coll.find()
        self.render('recommended.html',
                    page_title="Burt's Books | Recommended Reading",
                    header_text="Recommended Reading",
                    books=books
                    )


class BookEditHandler(tornado.web.RequestHandler):
    def get(self, isbn=None):
        book = dict()
        if isbn:
            coll = self.application.db.books
            book = coll.find_one({'isbn': isbn})
        self.render("book_edit.html",
                    page_title="Burt's Books",
                    header_text="Edit book",
                    book=book)

    def post(self, isbn=None):
        book_fields = ['isbn', 'title', 'subtitle', 'image', 'author',
                       'date_released', 'description']
        coll = self.application.db.books
        book = dict()
        if isbn:
            book = coll.find_one({'isbn': isbn})
        for key in book_fields:
            book[key] = self.get_argument(key, None)

        if isbn:
            coll.save(book)
        else:
            book['date_added'] = int(time.time())
            coll.insert(book)

        self.redirect('/recommended/')
