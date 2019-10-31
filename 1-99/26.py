def division(a, b):
    rems = []
    r = a % b
    if a > b:
        a = r
    while r != 0:
        for i in range(len(rems)):
            if r == rems[i]:
                return len(rems)-i+1
        rems.append(r)
        a = r * 10
        r = a % b
    return 0

top, toplen = 1, 0
for i in range(1,1000):
    curr = division(1, i)
    if curr > toplen:
        top = i
        toplen = curr

print(top)