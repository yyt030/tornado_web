#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import random
from tornado.web import RequestHandler


class ReverseHandler(RequestHandler):
    def get(self, input):
        self.write(input[::-1])


class WrapHandler(RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(text.zfill(20))


class IndexHandler(RequestHandler):
    def get(self):
        # greeting = self.get_argument('greeting', 'hello')
        # self.write(greeting + ', friendly user!')
        self.render('index.html',
                    header_text='Header goes here',
                    footer_text='Footer goes here')

    def write_error(self, status_code, **kwargs):
        self.write('Error, {}\n'.format(status_code))


class PoemPageHandler(RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb,
                    difference=noun3)


class MungedPageHandler(RequestHandler):
    def map_by_first_letter(self, text):
        mapped = {}
        for line in text.split('\r\n'):
            for word in [x for x in line.split(' ') if len(x) > 0]:
                if word[0] not in mapped:
                    mapped[word[0]] = []
                    mapped[word[0]].append(word)
        return mapped

    def post(self):
        source_text = self.get_argument('source')
        text_to_change = self.get_argument('change')
        source_map = self.map_by_first_letter(source_text)
        change_lines = text_to_change.split('\r\n')
        print('-' * 100)
        self.render('munged.html', source_map=source_map, change_lines=change_lines,
                    choice=random.choice)
