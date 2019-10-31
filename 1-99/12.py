from math import floor, sqrt

def leastfactor(n):
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3
    if n % 5 == 0: return 5
    for i in range(7, floor(sqrt(n))+1, 30):
        if n % i == 0:        return i
        if n % (i + 4) == 0:  return i+4
        if n % (i + 6) == 0:  return i+6
        if n % (i + 10) == 0: return i+10
        if n % (i + 12) == 0: return i+12
        if n % (i + 16) == 0: return i+16
        if n % (i + 22) == 0: return i+22
        if n % (i + 24) == 0: return i+24
    return n

def isprime(n):
    return n == leastfactor(n)

def factor(n):
    factors = {}
    while n != 1:
        lf = int(leastfactor(n))
        factors[lf] = 0
        while n % lf == 0:
            n = n / lf
            factors[lf] += 1
    return factors

def divisorcount(n):
    counter = 1
    factors = factor(n)
    for f in factors.values():
        counter *= f+1
    return counter

i, res = 1, 0
while(True):
    res += i
    if divisorcount(res) > 500:
        print(res)
        exit()
    i += 1