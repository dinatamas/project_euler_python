from math import floor, sqrt

def isprime(n):
    if n == 1:
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

i, res = 2, 0
for i in range(2,2000001):
    if isprime(i):
        res += i

print(res)