res = 0
n, m = 0, 1
while m < 4000000:
    n, m = m, n+m
    if m % 2 == 0:
        res += m

print(res)