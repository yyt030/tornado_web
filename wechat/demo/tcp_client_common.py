#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import socket

address = ('127.0.0.1', 8000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
s.sendall(b'test')
if s:
    s.close()
