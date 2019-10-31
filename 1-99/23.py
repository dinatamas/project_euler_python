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

abundants = []

for i in range(12,28124):
    if properdivisorsum(i) > i:
        abundants.append(i)

sums = [True for y in range(0,28124)]

for a in abundants:
    for b in abundants:
        if a + b < 28124:
            sums[a+b] = False

res = 0
for i in range(1,28124):
    if sums[i]:
        res += i

print(res)

"""
sums:
0 1 2 ... 28123
  1 2 ... 28123
"""