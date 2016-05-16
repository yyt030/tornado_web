#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import tornado.web


class WordHandler(tornado.web.RequestHandler):
    def get(self, word):
        coll = self.application.db.words
        word_doc = coll.find_one({'word': word})
        if word_doc:
            del word_doc['_id']
            self.write(word_doc)
        else:
            self.set_status(404)
            self.write({'error': 'word not found'})
