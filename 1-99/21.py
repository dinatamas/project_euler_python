# brute force algorithm

from math import floor, sqrt

# is factorisation faster? https://stackoverflow.com/a/36035209
def properdivisorsum(n):
    res = 1
    for i in range(2,floor(sqrt(n))+1):
        if n % i == 0:
            if i * i == n:
                res += i
            else:
                res += i + n / i
    return res

amicables = []

res = 0
for i in range(1,10000):
    if i in amicables:
        continue
    pdc = properdivisorsum(i)
    if pdc < i and properdivisorsum(pdc) == i:
        amicables.append(pdc)
        amicables.append(i)
        res += i + pdc

print(res)

# https://oeis.org/A259180
# print(31626)

    