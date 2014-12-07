import asyncio
import aiohttp
import bs4
import tqdm

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

@asyncio.coroutine
def wait_with_progress(coros):
    # tqdm library to make progress bars
    for f in tqdm.tqdm(asyncio.as_completed(coros), total=len(coros)):
        yield from f

distros = ['archlinux', 'ubuntu', 'debian']
# Ensures 5 parallel requests at a time
sem = asyncio.Semaphore(5)
loop = asyncio.get_event_loop()
# Run 1 request at a time for correct progress bar results.
# f = wait_with_progress([print_magnet(d) for d in distros])
f = asyncio.wait([print_magnet(d) for d in distros])
loop.run_until_complete(f)
