from functools import reduce
from math import log10, ceil

def is_pandigital(n):
    arr = [False for x in range(9)]
    while ( n != 0 ):
        arr[n % 10 - 1] = True
        n = n // 10
    return reduce(lambda a, b: a and b, arr)

res = 0
for n in range(2, 9):
    # n > 1
    # n == 9: i = 1, s = 123456789: NOT MAX
    for i in range(1, 10 ** (9 // n)):
        s = 0
        for j in range(n, 0, -1):
            s += i * j * (1 if s == 0 else 10 ** ceil(log10( s )))
        if ceil(log10( s )) == 9 and is_pandigital( s ) and s > res:
            res = s

print(res)

# log10 is the problem?