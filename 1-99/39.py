from math import log, ceil, sqrt

counts = [ 0 for x in range(0, 1001) ]
maxcount, maxindex = 1, 0
for a in range(1, 1000):
    for b in range(1, a + 1):
        p = a + b + sqrt(a ** 2 + b ** 2)
        if p == int(p) and p < 1001:
            p = int(p)
            print(a, b, p)
            counts[p] += 1
            if counts[p] > maxcount:
                maxcount = counts[p]
                maxindex = p
        else:
            continue
print(maxindex, maxcount)