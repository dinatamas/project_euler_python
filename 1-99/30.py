# a rough upper limit:
# (9 ** 5) is 59'049
# 354_294 = 6 * (9 ** 5)

res = 0
for i in range(2, 354294):
    currsum = 0
    for j in [int(x) for x in str(i)]:
        currsum += j ** 5
    if i == currsum:
        res += currsum

print(res)