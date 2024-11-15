"""
generators and functional patterns
"""

2174/35: data = []
2174/36:
for i in range(10):
    data.append(i ** 2)
2175/1: import itertools
2175/2: dir(itertools)
2175/3: ls
2175/4: help(itertools.cycle)
2175/5: help(itertools.chain)
2175/6:
list(itertools.chain([1,2,3],[4,5,6])
)
2175/7: # ipython
2175/8: d = [5, 3, 2, 9, 1]
2175/9: sorted(d)
2175/10: d
2175/11: g = (x for x in d)
2175/12: g
2175/13: sorted(g)
2175/14: e = [1, 1, 1, 1]
2175/15: f = [1, 1, 0, 1]
2175/16: all(e), all(f)
2175/17: g = [0, 0, 0, 0]
2175/18: all(g)
2175/19: any(e), any(f), any(g)
2175/20: s = "hello"
2175/21: i = 0
2175/22:
for char in s:
    print(i, char)
    i += 1
2175/23:
for i, char in enumerate(s):
    print(i, char)
2175/24: coord = [("E","4"), ("A", "3"), ("H", "8")]
2175/25:
for i, c in enumerate(coord):
    print(i, c[0], c[1])
2175/26:
for i, (long, lat) in enumerate(coord):
    print(i, long, lat)
2175/27: t = 1, 2, 3, 4
2175/28: t = 1, 2, 3, 4
2175/29: a, b, c, d = t
2175/30: a, *b = t
2175/31: b
2175/32: t = 1, 2, (3, 4)
2175/33: a, b, (c, d) = t
2175/34: v = 7,
2175/35: type(v)
2175/36: v = (7)
2175/37: type(v)
2175/38: tuple(7)
2175/39: v = tuple("hello")
2175/40: v
2175/41: fruechte = ["apfel", "banane", "cantaloupe", "dattel"]
2175/42: preise = [1.2, 3.4, 5.6, 7.8]
2175/43: zip(fruechte, preise)
2175/44: list(zip(fruechte, preise))
2175/45: list(zip(range(len(fruechte)), fruechte))
2175/46: dict(zip(fruechte, preise))
2175/47: tabelle = list(zip(fruechte, preise))
2175/48: tabelle
2175/49: list(zip(*tabelle))
2175/50: daten = fruechte, preise
2175/51: list(zip(*daten))
2175/52: tabelle = list(zip(fruechte, preise, "ABCD"))
2175/53: tabelle
2175/54: list(zip(*tabelle))
2175/55: tabelle
2175/56: list(zip(tabelle[0], tabelle[1], tabelle[2]))
2175/57: d = 1, 2, 3, 4
2175/58: d = [1, 2, 3, 4]
2175/59: e = *d
2175/60: e = *d,
2175/61: e
2175/62: e = [*d, *d]
2175/63: print(*d)
2175/64:
def zahlen():
    yield 1
    yield 2
    yield 3
2175/65: zahlen()
2175/66: g = zahlen()
2175/67: next(g)
2175/68: next(g)
2175/69: next(g)
2175/70: next(g)
2175/71: list(zahlen())
2175/72: import time
2175/73:
def zahlen():
    yield 1
    time.sleep(3)
    yield 2
    time.sleep(3)
    yield 3
2175/74: g = zahlen()
2175/75: next(g)
2175/76: next(g)
2175/77: next(g)
2175/78: d
2175/79: dir(d)
2175/80: d.__iter__()
2175/81: i = d.__iter__()
2175/82: next(i)
2175/83: next(i)
2175/84:
def squares():
    for i in range(10):
        yield i**2
2175/85: squares()
2175/86: g = squares()
2175/87: list(g)
2175/88: list(g)
2175/89: next(g, "alle")
2175/90: dir(g)
2175/91:
def squares():
    for i in range(10):
        yield i**2
2175/92: m, n = squares(), squares()
2175/93: next(m), next(m), next(m)
2175/94: next(n)
2175/95: next(n)
2175/96:
def squares():
    i = 1
    while True:
        yield i**2
        i += 1
2175/97: g = squares()
2175/98: next(g)
2175/99: next(g)
2175/100: list(zip(range(10), g))
2175/101: list(zip(range(10), g))
2175/102: [next(g) for _ in range(10)]
2175/103: [next(g) for _ in range(10)]
2175/104: next(g)
2175/105: from copy import copy, deepcopy
2175/106: h = deepcopy(g)
2175/107:
def squares():
    i = 1
    while True:
        yield i**2
        i += 1
2175/108: # TODO: generate fibonacci numbers
2175/109: # TODO: schreibe einen Generator, der die
2175/110: # ersten 10 Zahlen aus einem anderen Generator zurückgibt
2175/111:
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
2175/112:
def take(g, n):
    yield [next(g) for _ in range(n)]
2175/113:
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
2175/114:
def squares():
    i = 1
    while True:
        yield i**2
        i += 1
2175/115: import itertools
2175/116: itertools.count
2175/117: g = itertools.count()
2175/118: next(g)
2175/119: next(g)
2175/120: next(g)
2175/121: gens [itertools.count, squares, fibonacci]
2175/122: gens = [itertools.count, squares, fibonacci]
2175/123: gens
2175/124: next(gens[0]())
2175/125: names = [f.__name__ for f in gens]
2175/126: names
2175/127: d = dict(zip(names, gens))
2175/128: d
2175/129: d
2175/130: mode = "fibonacci"
2175/131:
if mode == "fibonacci":
    next(fibonacci())
elif mode == "squares":
    ...
2175/132: next(d[mode]())
2175/133:
from typing import Callable
def skip(gen: Callable, n: int) -> int:
    """liefere den n-ten Wert aus gen"""
    g = gen()
    for _ in range(n-1):
        next(g)
2175/134:
from typing import Callable
def skip(gen: Callable, n: int) -> int:
    """liefere den n-ten Wert aus gen"""
    g = gen()
    for _ in range(n-1):
        next(g)
    return next(g)
2175/135: skip(squares, 10)
2175/136: skip(fibonacci, 7)
2175/137: from functools import partial
2175/138: skip_ten = partial(skip, n=10)
2175/139: skip_ten(squares)
2175/140: skip_ten(fibonacci)
2175/141: skip_ten = partial(skip, n=10)
2175/142: skip_seven = partial(skip, n=7)
2175/143: skip_twenty = partial(skip, n=20)
2175/144: skip_funcs = [skip_seven, skip_ten, skip_twenty]
2175/145: gens
2175/146: [[f(g) for f in skip_funcs] for g in gens]
2175/147: [[f(g) for f in skip_funcs] for g in gens]
2175/148: [[f(g) for f in skip_funcs] for g in gens]
2175/149: itertools.product([1,2,3], "ABC")
2175/150: list(itertools.product([1,2,3], "ABC"))
2175/151: [f(g) for f,g in itertools.product(skip_funcs, gens)]
2175/152: [f(g) for f,g in itertools.product(gens, skip_funcs)]
2175/153: [f(g) for f,g in itertools.product(skip_funcs, gens)]
2175/154: [f(g) for g,f in itertools.product(gens, skip_funcs)]
2175/155: t = [[f(g) for f in skip_funcs] for g in gens]
2175/156: t
2175/157: list(itertools.chain(t))
2175/158: list(itertools.chain(*t))
2175/159: p = itertools.permutations()
2175/160: list(itertools.chain(*t))
2175/161: t
2175/162:
def chain(*args):
    for a in args:
        for b in a:
            yield b
2175/163: list(itertools.chain(*t))
2175/164: list(chain(*t))
2175/165: d
2175/166: e = [1,2,3]
2175/167: itertools.cycle(e)
2175/168: g = itertools.cycle(e)
2175/169: [next(g) for _ in range(10)]
2175/170: dir(itertools)
2175/171:
for i in itertools.cycle():
    print(i)
2175/172:
for i in itertools.count():
    print(i)
2175/173: s = list("ABCD")
2175/174: list(itertools.permutations(s))
2175/175: list(itertools.combinations(s, 2))
2175/176: list(itertools.combinations_with_replacement(s, 2))
2175/177:

2175/242: square
2175/243: help(square)
2175/244: import time
2175/245: time.asctime()
2175/246: # Schreibe einen Dekorator (Funktion oder Klasse), der Start- und Endzeit ausgibt
2176/1: %time len(range(100000))
2176/2: %timeit len(range(100000))
