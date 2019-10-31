from math import floor, sqrt

def isprime(n):
    for i in range(2, floor(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in range(1, 600851475143):
    if 600851475143 % i == 0:
        if isprime(600851475143 / i):
            print(600851475143 / i)
            exit()