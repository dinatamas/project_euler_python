# https://www.geeksforgeeks.org/space-and-time-efficient-binomial-coefficient/

def binom(n, k):
    if (k > n - k):
        k = n - k
    res = 1
    for i in range(k):
        res = res * (n - i) / (i + 1)
    return res

print(binom(40, 20))