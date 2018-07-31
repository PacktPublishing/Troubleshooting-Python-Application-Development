import timeit


# 2.1
class Foo:
    __slots__ = ('foo', 'bar', 'baz')


class Bar:
    pass


class EmptySlots:
    __slots__ = ()


slotted = Foo()
not_slotted = Bar()


def set_delete_slotted():
    slotted.foo = 'foo'
    del slotted.foo
    slotted.bar = 'bar'
    del slotted.bar
    slotted.baz = 'baz'
    del slotted.baz


def set_delete_not_slotted():
    not_slotted.foo = 'Foo'
    del not_slotted.foo
    not_slotted.bar = 'Foo'
    del not_slotted.bar
    not_slotted.baz = 'Foo'
    del not_slotted.baz


# time the slotted version
print(timeit.repeat(set_delete_slotted))

# time the non-slotted version
print(timeit.repeat(set_delete_not_slotted))

# 2.2
# demonstrated on the command line

# 2.3
import memory_profiler
import itertools

@memory_profiler.profile
def all_in_memory():
    return [''.join(p) for p in itertools.permutations('0123456789')]


@memory_profiler.profile
def with_generator():
    return (''.join(p) for p in itertools.permutations('0123456789'))

x = all_in_memory()
y = with_generator()

