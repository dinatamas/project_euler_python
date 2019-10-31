arr = [int(x) for x in str(2 ** 1000)]

res = 0 
for n in arr:
    res += n

print(res)

"""
res = 0
for n in str(2**1000):
	res += int(n)
print(res)
"""