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

@asyncio.coroutine
def print_all_pages(urls):
    # takes a list of coroutines and returns an iterator 
    # that yields the coroutines in the order in which they are completed, 
    # so that when you iterate on it, you get each result as soon as it's available.
    for item in asyncio.as_completed(urls):
        yield from item

loop = asyncio.get_event_loop()
# loop.run_until_complete(print_page('http://www.chatimity.com'))

# asyncio.wait takes a list a coroutines and returns a single coroutine that wrap them all
# loop.run_until_complete(asyncio.wait([print_page('http://chatimity.com'),
#                                       print_page('http://google.com')]))
loop.run_until_complete(print_all_pages([print_page('http://chatimity.com'),
                                      print_page('http://google.com')]))
