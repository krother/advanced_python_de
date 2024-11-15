import functools


# caching decorator speeds up things
@functools.lru_cache()
def fibonacci(n):
    """inefficient recursive function O(exp(n))"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


fibonacci(200)


# write the decorator ourselves
def cached(f):
    """äußere Funktion"""
    cache = {}
    print("decorator initialized")
    
    @functools.wraps(f)  # kopiert __name__ und __doc__    
    def inner(n):
        print(f"call with {n}")
        if n in cache:
            print("using cache")
            return cache[n]
        else:
            result = f(n)
            cache[n] = result
            print("END")
            return result
    
    return inner


# use the decorator
@cached
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


@cached
def square(n):    
    return n**2
