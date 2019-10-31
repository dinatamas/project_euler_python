# https://stackoverflow.com/questions/30214531/basics-of-recursion-in-python

from math import ceil, floor, sqrt, log

def remove_from_left(n):
    
    def remove_from_left_aux(n, d):
        if n == 0 or floor(log(n, 10)) == 0:
            d.add(n)
            return d
        d.add(n)
        return remove_from_left_aux(n % 10 ** floor(log(n, 10)), d)

    return remove_from_left_aux(n, set())

def remove_from_right(n):

    def remove_from_right_aux(n, d):
        if floor(log(n, 10)) == 0:
            d.add(n)
            return d
        d.add(n)
        return remove_from_right_aux(n // 10, d)

    return remove_from_right_aux(n, set())

def incremental_sieve_of_eratosthenes(primes, m, n):
    A = [ True for i in range(m, n) ]
    for p in primes:
        for i in range(ceil(m / p) * p, n, p):
            A[i - m] = False
    for i in range(m, ceil(sqrt(n))):
        if A[i - m]:
            for j in range(i**2, n, i):
                A[j - m] = False
    for i in range(m, n):
        if A[i - m]:
            primes.add(i)
    return primes

primes = incremental_sieve_of_eratosthenes(set(), 2, 1000)

res = 0
i, n, counter = 2, 1000, 0
while counter < 15:
    is_good = True
    for x in remove_from_left(i).union(remove_from_right(i)):
        if x not in primes:
            is_good = False
            break
    if is_good:
        print(i)
        res += i
        counter += 1
    if i == n:
        primes = incremental_sieve_of_eratosthenes(primes, n, 2*n)
        n = n * 2
    i += 1

res = res - 17 # 2,3,5,7 are not considered truncatable
print(res)