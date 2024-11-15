"""
examples of different comprehensions
"""

# create a random 2D matrix
import random

print("\n".join(["".join([random.choice([".", "#"]) for _ in range(10)]) for _ in range(10)]))

# generator expression
g = (x ** 2 for x in range(1, 11))
next(g)
list(g)

# tuple unpacking works with generators
g = (x ** 2 for x in range(1, 11))
a, *b, c = g

# set comprehension
{x ** 2 for x in range(-10, 11)}

# dict comprehension
{x: x ** 2 for x in range(1, 11) if x % 3 == 0}

# there is no explicit tuple comprehension
tuple(x ** 2 for x in range(1, 11))
