import cProfile
import timeit
import profile
import textwrap
import functools
import time


print('Troubleshooting Python Application Development: Chapter 1')
print('-' * 79)

# --------------------------------------------------------------------------------
# 1.1
print('Measuring time between two lines of code with timeit')
print('-' * 79)

t = timeit.Timer(
    "print('this line is timed')",
    "print('put setup code here')")

print('TIMEIT:')
print(t.timeit(3))

print('REPEAT:')
print(t.repeat(5, 2))

range_size = 2000
count = 2000
vars_for_testing = ';'.join([
    "xs = [(str(x), x) for x in range(2000)]",
    "d = {}",
])
code_for_testing = textwrap.dedent(
        """
        for str_x, x in xs:
            d[str_x] = x
        """)


def show_results(result):
    global count, range_size
    print('{:6.2f} usec/pass'.format(
        1000000 * (result / count)), end=' ')
    print('{:6.2f} usec/item'.format(
        (1000000 * (result / count)) / range_size))


print("list len = {}, trying {} iterations".format(
    range_size, count))

print('experiment:', end=' ')
t = timeit.Timer(code_for_testing, vars_for_testing)
show_results(t.timeit(number=count))


# --------------------------------------------------------------------------------
# 1.2
print('Figuring out where time is spent with the profile module')
print('-' * 79)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq


profile.run('print(fib_seq(20)); print()')


@functools.lru_cache(maxsize=None)
def fib_memoized(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_memoized(n - 1) + fib_memoized(n - 2)


def fib_seq_memoized(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq_memoized(n - 1))
    seq.append(fib_memoized(n))
    return seq


profile.run('print(fib_seq_memoized(20)); print()')

# Running with context
profile.runctx(
        'print(fib_seq(n)); print()',
        globals(),
        {'n': 20},
    )


# --------------------------------------------------------------------------------
# 1.3
print('More precise time tracking with cProfile')
print('-' * 79)

print('Profiling 2 + 2 with cProfile:')
cProfile.run("2 + 2")

print('Profiling 3 functions with cProfile:')


def fast_function():
    print('fast')


def medium_func():
    print('medium')
    time.sleep(1)


def slow_func():
    print('slow')
    time.sleep(2)


def test_func():
    fast_function()
    medium_func()
    slow_func()


cProfile.run('test_func()')

# --------------------------------------------------------------------------------
# 1.4
print('Looking at memory consumption with memory_profiler')
print('-' * 79)

import memory_profiler


@memory_profiler.profile
def test_func():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    addition = 0

    for num in numbers:
        addition += num

    return addition


test_func()


@memory_profiler.profile
def memory_clearing_func():
    x = [1] * (10 ** 5)
    y = [2] * (10 ** 7)
    del y
    return x


memory_clearing_func()
