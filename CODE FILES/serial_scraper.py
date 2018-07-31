import requests
import time

results = []
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

for u in urls:
    r = requests.get(u)
    results.append(r.status_code)

print(results)
print('Done in {:.3}s.'.format(time.time()-start))