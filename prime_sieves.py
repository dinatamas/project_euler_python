# https://github.com/kimwalisch/primesieve
# https://en.wikipedia.org/wiki/Generation_of_primes#Complexity
# https://stackoverflow.com/questions/16004407/a-fast-prime-number-sieve-in-python

"""
- sieve of Eratosthenes
- sieve of Sundaram
- sieve of Atkin
- wheel factorization

- segmented sieves
- incremental sieves
- multithreading
"""

from math import ceil, floor, sqrt

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def sieve_of_eratosthenes(n):
    primes = []
    A = [ True for i in range(n) ]
    for i in range(2, ceil(sqrt(n))):
        if A[i]:
            for j in range(i**2, n, i):
                A[j] = False
    for i in range(2, n):
        if A[i]:
            primes.append(i)
    return primes

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
            primes.append(i)
    return primes

# https://en.wikipedia.org/wiki/Sieve_of_Sundaram

# https://en.wikipedia.org/wiki/Sieve_of_Atkin#Pseudocode

# https://en.wikipedia.org/wiki/Wheel_factorization

# http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.94.1737

"""
Use sets and hash data structures, and instead of True/False
remove the composites? This will save the last n operations
of iterating through the array, but the removal will require
more steps than the random access of array elements.
"""