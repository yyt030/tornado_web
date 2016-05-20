#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import socket

server_address = ('localhost', 8000)
print('starting up on %s port %s' % server_address)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)
sock.listen()

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    if data:
        print('data:', data)
        conn.sendall(data)
    conn.close()
