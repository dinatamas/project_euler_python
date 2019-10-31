def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def lcm(array):
    res = array[0]
    for n in array[1:]:
        res = res * n / gcd(res, n)
    return res

print(lcm(range(1,20)))