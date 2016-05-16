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

    def post(self, word):
        definition = self.get_argument('definition')
        coll = self.application.db.words
        word_doc = coll.find_one({'word': word})
        if word_doc:
            word_doc['definition'] = definition
            coll.save(word_doc)
        else:
            word_doc = {'word': word, 'definition': definition}
            coll.insert(word_doc)
        del word_doc["_id"]
        self.write(word_doc)
