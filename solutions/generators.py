"""
generators and functional patterns
"""
import itertools
from typing import Callable
from functools import partial

# flatten lists with itertools

list(itertools.chain([1,2,3],[4,5,6]))

# sorted() can sort lists and generators
d = [5, 3, 2, 9, 1]
sorted(d)

g = (x for x in d)
sorted(g)

# all and any perform boolean operations
e = [1, 1, 1, 1]
f = [1, 1, 0, 1]
g = [0, 0, 0, 0]
all(e), all(f), all(g)
any(e), any(f), any(g)

# enumerate adds a counter variable
for i, char in enumerate(s):
    print(i, char)

# tuple unpacking inside for
coord = [("E","4"), ("A", "3"), ("H", "8")]
for i, (long, lat) in enumerate(coord):
    print(i, long, lat)


# inline tuple unpacking
t = 1, 2, 3, 4
a, b, c, d = t
a, *b = t
t = 1, 2, (3, 4)
a, b, (c, d) = t

# tricks with zip()
fruechte = ["apfel", "banane", "cantaloupe", "dattel"]
preise = [1.2, 3.4, 5.6, 7.8]

zip(fruechte, preise)
tabelle = list(zip(fruechte, preise))
list(zip(range(len(fruechte)), fruechte))  # this is enumerate
dict(zip(fruechte, preise))

list(zip(*tabelle))  # transpose()

# simple generator
def zahlen():
    yield 1
    yield 2
    yield 3

g = zahlen()
next(g)
next(g)

list(zahlen())


# square numbers
def squares():
    for i in range(10):
        yield i**2

g = squares()
list(g)
next(g, "alle")  # default value for expired generator

# generators have their own state
m, n = squares(), squares()
next(m), next(m), next(m)
next(n)

# endless generator
def squares():
    i = 1
    while True:
        yield i**2
        i += 1


g = squares()
[next(g) for _ in range(10)]
[next(g) for _ in range(10)]
next(g)


# fibonacci series
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def take(g, n):
    yield [next(g) for _ in range(n)]


g = itertools.count()  # endless integers

# create 3 endless functions + labels
gens = [itertools.count, squares, fibonacci]
names = [f.__name__ for f in gens]
d = dict(zip(names, gens))

# use one function
mode = "squares"
next(d[mode]())


# take n-th value from a generator
def skip(gen: Callable, n: int) -> int:
    """liefere den n-ten Wert aus gen"""
    g = gen()
    for _ in range(n-1):
        next(g)
    return next(g)

skip(squares, 10)
skip(fibonacci, 7)

skip_ten = partial(skip, n=10)
skip_ten(squares)
skip_ten(fibonacci)
skip_ten = partial(skip, n=10)
skip_seven = partial(skip, n=7)
skip_twenty = partial(skip, n=20)
skip_funcs = [skip_seven, skip_ten, skip_twenty]

# combine everything with everything
itertools.product([1,2,3], "ABC")
list(itertools.product([1,2,3], "ABC"))
[f(g) for f,g in itertools.product(skip_funcs, gens)]

# some more itertools functions
p = itertools.permutations()
g = itertools.cycle([1,2,3])
list(itertools.permutations(s))
list(itertools.combinations(s, 2))
list(itertools.combinations_with_replacement(s, 2))
