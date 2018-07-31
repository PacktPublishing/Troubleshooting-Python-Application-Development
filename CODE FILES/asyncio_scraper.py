import asyncio
import requests
import time


async def batch_requests():
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
    event_loop = asyncio.get_event_loop()
    futures = [event_loop.run_in_executor(None, requests.get, u) for u in urls]
    return await asyncio.gather(*futures)

event_loop = asyncio.get_event_loop()
start = time.time()
result = event_loop.run_until_complete(batch_requests())
print(result)
print('Done in {:.3}s.'.format(time.time()-start))