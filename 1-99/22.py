arr = []

with open("22.dat", "r") as f:
    arr = f.read().split('","')

arr[0] = arr[0][1:]
arr[5162] = arr[5162][:-1]

arr.sort()

res = 0
for i in range(0, 5163):
    curr = 0
    for j in arr[i]:
        curr += ord(j) - 64
    res += curr * (i+1)

print(res)