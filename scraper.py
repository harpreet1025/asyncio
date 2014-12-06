import asyncio
import aiohttp
import bs4

@asyncio.coroutine
def get(*args, **kwargs):
    response = yield from aiohttp.request("GET", *args, **kwargs)
    return (yield from response.read())

def first_magnet(page):
    soup = bs4.BeautifulSoup(page)
    a = soup.find("a", title="Download this torrent using magnet")
    return a["href"]


@asyncio.coroutine
def print_magnet(query):
    url = 'http://fastpiratebay.eu/thepiratebay.se/s/?q={}&category=0&page=0&orderby=99'.format(query)
    with (yield from sem):
        page = yield from get(url, compress=True)
    magnet = first_magnet(page)
    print('{}: {}'.format(query, magnet))


# TODO: Using progress bar

distros = ['archlinux', 'ubuntu', 'debian']
# Ensures 5 parallel requests at a time
sem = asyncio.Semaphore(5)
loop = asyncio.get_event_loop()
f = asyncio.wait([print_magnet(d) for d in distros])
loop.run_until_complete(f)
