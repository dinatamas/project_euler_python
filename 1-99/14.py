from math import floor, ceil, log
import timeit

"""
# only powers of 2 decay to 1
def ispowerof(n, base):
    return floor(log(n, base)) == ceil(log(n, base))
# use B+ trees to memoize results
"""

codetotest = """
top, toplen = 1, 1

# x < 500000 implies 500000 < 2 * x < 1000000
for i in range(500000,999999):
    counter, n = 0, i
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            counter += 1
        else:
            n = (3 * n + 1) / 2
            counter += 2
    if counter > toplen:
        top = i
        toplen = counter
        print(top, "->", toplen)
"""

speed = timeit.timeit(codetotest, number=10)/10
print(speed)

# print(top)