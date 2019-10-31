def fact(n):
    res = 1
    for i in range(2,n):
        res *= i
    return res

arr = [int(x) for x in str(fact(100))]

res = 0
for n in arr:
    res += n

print(res)

"""
from math import factorial as fact

i = int(0)
for j in str(fact(100)):
    i += int(j)
print(i)
"""