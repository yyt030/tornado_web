#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import tornado.gen
import tornado.httpclient
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        cookie = self.get_secure_cookie('count')
        count = int(cookie) + 1 if cookie else 1
        countString = "1 time" if count == 1 else "%d times" % count
        self.set_secure_cookie("count", str(count))
        self.render('index.html')


class IndexAsyncHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        url = 'http://localhost:5000/questions/newest'
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch(url, callback=self.on_response)

    def on_response(self, response):
        if response:
            self.write(response.body.decode('utf-8'))
        else:
            self.write('ok')
        self.finish()


class IndexAsyncGenHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        url = 'http://localhost:5000/questions/newest'
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch, url)
        if response:
            self.write(response.body)
        else:
            self.write('ok')
        self.finish()
