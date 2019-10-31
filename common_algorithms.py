from math import floor, sqrt, log

# factorial
def fact(n):
    res = 1
    for i in range(2,n):
        res *= i
    return res

# nth fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# fibonacci series

# greatest common divisor
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def gcd(array):
    res = gcd(array[0], array[1])
    for n in array[2:]:
        res = gcd(res, n)
    return res

# lowest common multiple
def lcm(x, y):
    return (x*y)//gcd(x,y)

def lcm(array):
    res = array[0]
    for n in array[1:]:
        res = res * n / gcd(res, n)
    return res

# primality test
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

# sieve of Eratosthenes
# prime factorization

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

# def divisors(n):

# palindrome test
def ispalindrome(n):
    return str(n) == str(n)[::-1]
"""
def index(n, i):
    return (n % 10 ** (i+1)) // 10 ** i

def ispalindrome(n):
    length = int(log(n, 10))
    for i in range(length):
        if index(n, i) != index(n, length-i):
            return False
    return True

def ispalindrome(n, b):
    reversed = 0
    k = n
    while k > 0:
        reversed = b * reversed + k % b
        k = k // b
    return (n == reversed)
"""
# sum of nth powers, arithmetic & geometric progressions

# https://en.wikipedia.org/wiki/Binary_search_algorithm#Implementation_issues
def binsearch(arr, n):
    first = 0
    last = len(arr)-1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == n:
            return True
        else:
            if n > arr[mid]:
                first = mid + 1
            else:
                last = mid - 1
    return False

