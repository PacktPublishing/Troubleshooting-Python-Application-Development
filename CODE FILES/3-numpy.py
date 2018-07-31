import numpy as np
import numexpr as ne
import timeit

# 3.1


# 3.2
# 3.3

def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    return a + b

def pythonsum(n):
    a = [i ** 2 for i in range(n)]
    b = [i ** 3 for i in range(n)]
    return [a[i] + b[i] for i in range(n)]

# 3.5

xs = np.random.random((1000, 3))

def calc_numpy(xs):
    squared_error = (xs[:, None, :] - xs) ** 2
    sum_squared_error = (squared_error).sum(-1)
    return np.sqrt(sum_squared_error)

def calc_numexpr(xs):
    expanded = xs[:, np.newaxis, :]
    sum_squared_error = ne.evaluate('sum((expanded-xs)**2, axis=2)')
    return ne.evaluate('sqrt(sum_squared_error)')


