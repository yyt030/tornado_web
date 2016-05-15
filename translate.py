#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import requests

url = 'https://translate.google.co.jp/translate_a/single?client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=2&ssel=0&tsel=0&kc=1&tk=851683.707920&q=%E4%BB%8A%E5%A4%A9%E5%A4%A9%E6%B0%94%E5%A5%BD%E5%90%97%EF%BC%9F'

proxies = {'http': "socks5://127.0.0.1:1080"}
r = requests.get(url, proxies=proxies, timeout=10)
