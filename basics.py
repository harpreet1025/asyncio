import asyncio
import aiohttp

@asyncio.coroutine
def print_page(url):
    response = yield from aiohttp.request('GET', url)
    body = yield from response.read_and_close(decode=True)
    print(body)


loop = asyncio.get_event_loop()
loop.run_until_complete(print_page('http://www.google.com'))
