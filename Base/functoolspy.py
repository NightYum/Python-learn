import functools

my_func = functools.reduce(lambda x, y: x + y, [1, 2, 3])

print(my_func)

