def itoa(n):
    while n != 0:
        r = n % 10
        n = n / 10

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def index(n, i):
    return (n % 10 ** (i+1)) // 10 ** i

def pluck(n, i):
    d = n // 10 ** (i+1)
    r = n % 10 ** i
    return d * 10 ** i + r

fractions = []

for b in range(10,100):
    for a in range(10,b):
        for i in range(2):
            for j in range(2):
                pa, pb = pluck(a, i), pluck(b, j)
                if index(a, i) == index(b, j) and pb != 0 and a / b == pa / pb:
                    if a % 10 != 0 or b % 10 != 0:
                        fractions.append([a, b])

nom, denom = 1, 1
for i in fractions:
    nom *= i[0]
    denom *= i[1]
g = gcd(nom, denom)
nom = nom / g
denom = denom / g

print(nom, denom)

"""
frac=1.0
for b in range(1,10):
    for a in range(1,b):
        for c in range(1,10):
            if (a*10+b)/(b*10+c)==a/c:
                frac*=(a/c)
print(1/frac)
"""