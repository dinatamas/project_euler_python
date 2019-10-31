from math import floor, sqrt

def isprime(n):
    if n <= 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    for i in range(5, floor(sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

top, toplen = 0, 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while isprime(n**2 + a*n + b):
            n += 1
        if n > toplen:
            top = a * b
            toplen = n
            print(a, b, top, toplen)

print(top)