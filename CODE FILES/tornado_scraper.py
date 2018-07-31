from tornado import gen, ioloop, httpclient
import functools
import time


@gen.coroutine
def batch_requests():
    http_client = httpclient.AsyncHTTPClient()
    urls = [
        'http://www.bbc.co.uk/news/uk-44190742',
        'http://www.bbc.co.uk/news/uk-44173553',
        'http://www.bbc.co.uk/news/uk-england-44194146',
        'http://www.bbc.co.uk/news/health-44195456',
        'http://www.bbc.co.uk/news/uk-44190742',
        'http://www.bbc.co.uk/news/uk-44173553',
        'http://www.bbc.co.uk/news/uk-england-44194146',
        'http://www.bbc.co.uk/news/health-44195456',
        'http://www.bbc.co.uk/news/uk-44190742',
        'http://www.bbc.co.uk/news/uk-44173553',
        'http://www.bbc.co.uk/news/uk-england-44194146',
        'http://www.bbc.co.uk/news/health-44195456'
    ]
    futures = yield [http_client.fetch(u) for u in urls]
    status_codes = [f.code for f in futures]
    raise gen.Return(value=status_codes)

start = time.time()
io_loop = ioloop.IOLoop.instance()
scraper = functools.partial(batch_requests)
result = io_loop.run_sync(scraper)

print(result)
print('Done in {:.3}s.'.format(time.time()-start))