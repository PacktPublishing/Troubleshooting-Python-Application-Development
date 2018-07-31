import time


words = ['afbdfb', 'asvref', 'ddc', '2ff', 's'] * 10000000

print('Decorate, sort, undecorate:')
start = time.time()
decorated = [(len(w), w) for w in words]
decorated.sort()
# undecorating
result =  [d[1] for d in decorated]
print(time.time() - start)

print('Using a sort key:')
start = time.time()
sorted(words, key=len)
print(time.time() - start)
