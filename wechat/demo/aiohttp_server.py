#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import asyncio

from aiohttp import ClientSession


async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)


loop = asyncio.get_event_loop()
tasks = []

url = 'https://www.python.org'
for i in range(5):
    task = asyncio.ensure_future(hello(url))
    tasks.append(task)


loop.run_until_complete(asyncio.wait(tasks))
