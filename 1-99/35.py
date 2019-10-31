from math import floor, sqrt

"""
def firstndigits(num, n):
    return num // 10 ** (int(log(num, 10)) - n + 1)
"""

from math import log

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

def rotate(n):
    m, res = n, [n]
    arealldigitssame = True
    for i in range(int(log(m,10))):
        first = m // 10 ** (int(log(m, 10)))
        m = (m % 10 ** int(log(m,10))) * 10 + first
        if int(log(m,10)) < int(log(n,10)):
            return []
        res.append(m)
        if first != n % 10:
            arealldigitssame = False
    if arealldigitssame:
        return [n]
    else:
        return res

# generate the numbers, rotate them and check primality

res = set(())
for i in range (1,1000000):
    nums = rotate(i)
    iscircularprime = True
    for a in nums:
        if not isprime(a):
            iscircularprime = False
            break
    if iscircularprime:
        res.update(nums)

res = sorted(list(res))

print(len(res))
print(res)

"""
Variable number of for loops: (Recursion also works!)

ranges=((1,4),(0,3),(3,6))
operations = 1
for p in ranges:
    operations *= p[1]-p[0]
operations -= 1
result=[i[0] for i in ranges]
pos=len(ranges)-1
increments=0
print result
while increments < operations:
    if result[pos]==ranges[pos][1]-1:
        result[pos]=ranges[pos][0]
        pos-=1
    else:
        result[pos]+=1
        increments+=1
        pos=len(ranges)-1
        print result
"""