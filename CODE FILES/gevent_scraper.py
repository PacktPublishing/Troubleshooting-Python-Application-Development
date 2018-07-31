import gevent
from gevent.lock import Semaphore
import requests
import time

def batch_requests(urls):
    semaphore = Semaphore(100)
    requests = [gevent.spawn(fetch_website, u, semaphore) for u in urls]
    for response in gevent.iwait(requests):
        yield response


def fetch_website(url, semaphore):
    with semaphore:
        r = requests.get(url)
        return r.status_code

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

start = time.time()
futures = batch_requests(urls)
status_codes = [f.value for f in futures]
print(status_codes)
print('Done in {:.3}s.'.format(time.time()-start))