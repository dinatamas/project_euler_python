from math import floor, sqrt, log10, ceil

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

def number_to_array(num):
    array = [0 for x in range(floor(log10(num))+1)]
    i = len(array)-1
    while i >= 0:
        array[i] = num % 10
        num = num // 10
        i -= 1
    return array

def array_to_number(array):
    i = 0
    num = 0
    while i <= len(array)-1:
        num = num * 10 + array[i]
        i += 1
    return num

def ispalindrome(num, n):
    return sorted(number_to_array(num)) == [x for x in range(1,n+1)]

def number_of_digits(num):
    return int(log10(num)) + 1

"""
for num in range(10**9-1, 1, -2):
    if ispalindrome(num, number_of_digits(num)) and isprime(num):
        print(num)
        break
"""

# use the sieve of eratosthenes
# use the special properties of palindrome numbers so that you don't
    # have to check every number