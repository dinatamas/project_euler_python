res = 0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if str(i*j) == str(i*j)[::-1] and i*j > res:
            res = i*j

print(res)