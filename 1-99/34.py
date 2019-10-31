# a rough upper limit:
# 9! is 362,880‬
# 2_540_160 = 7 * 9!

fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

res = 0
for i in range(3, 2540160):
    n = i
    curr = 0
    while n != 0:
        curr += fact[int(n % 10)]
        n = n // 10
    if curr == i:
        res += i

print(res)