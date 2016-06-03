#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import asyncio

from aiohttp import ClientSession


async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()


async def run(loop, r):
    tasks = []
    url = 'https://www.python.org'
    for i in range(5):
        task = asyncio.ensure_future(fetch(url))
        tasks.append(task)
    responses = await asyncio.gather(*tasks)
    print(responses)


def print_response(result):
    print(result)


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(loop, 4))
loop.run_until_complete(future)
