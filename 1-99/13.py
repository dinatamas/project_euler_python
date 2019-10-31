f = open("13.dat", "r")
res = 0
for i in range(0,100):
    res += int(f.readline())

print(res)