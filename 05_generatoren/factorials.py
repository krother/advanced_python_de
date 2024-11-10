

def factorial():
    a, b = 1, 1
    while True:
        a *= b
        yield a
        b += 1


iterator = factorial()
next(iterator)
