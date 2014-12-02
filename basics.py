# pip3 install aiohttp for getting aiohttp library

import asyncio
import aiohttp

@asyncio.coroutine
def print_page(url):
    response = yield from aiohttp.request('GET', url)
    # read_and_close function is deprecated
    # read(True) is deprecated, use .json instead
    body = yield from response.read()
    print(body)


loop = asyncio.get_event_loop()
loop.run_until_complete(print_page('http://www.chatimity.com'))
