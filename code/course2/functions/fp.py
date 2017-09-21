# -*- coding: utf-8 -*-


# map

def work(value):
    return value * 2

t = [1, 2, 10]
m = map(work, t)
print(m)

# The same, but using lambda function
m1 = map(lambda x: x * 2, t)
print(list(m1))


# filter

print(list(filter(lambda v: v > 0, [-1, -5, -9, 20, 3, 0])))


# reduce

from functools import reduce

r = [1, 4, 2, 3]

result = reduce(lambda x, y: x + y, r)
print(result)
