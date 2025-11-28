# l = [9, 36, 4, 16, 25]
# map, reduce, filter
# l = [3, 6, 2, 4, 5]

# for index in range(len(l)):
#     l[index] = l[index]**2

# print(l)

# l = [3, 6, 2, 4, 5]

# l = list(map(lambda x: x**2, l))

# # [9, 36, 4, 16, 25]
# print(l)

# numbers = [3, 6, 2, 4, 5]

# def oddFilter(x):
#     return x % 2 != 0

# print(list(filter(oddFilter, numbers)))
# print(list(filter(lambda x: x % 2 != 0, numbers)))

from math import factorial
from math import log2
from functools import reduce

numbers = [3, 6, 2, 4, 5]

print(reduce(lambda p, c: p * c, numbers))

# def red(func, iter):
#     if len(iter) == 0:
#         return 0

#     previous = iter[0]
#     current = 1

#     while current < len(numbers):
#         previous = func(previous, iter[current])
#         current = current + 1

#     return previous


# numbers = []

# print(red(lambda p, c: p * c, numbers))


# print(factorial(4))
print(log2(5))
