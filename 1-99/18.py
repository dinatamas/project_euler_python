f = open("18.dat", "r")
triangle = [[] for y in range(0,15)]
route = [[] for y in range(0,15)]
for i in range(0,15):
    line = f.readline().split()
    for j in range(0,i+1):
        triangle[i].append(int(line[j]))
        route[i].append("")

# 0 is left, 1 is right

for i in range(13,-1,-1):
    for j in range(0,i+1):
        if triangle[i+1][j] > triangle[i+1][j+1]:
            triangle[i][j] += triangle[i+1][j]
            route[i][j] += route[i+1][j] + "0"
        else:
            triangle[i][j] += triangle[i+1][j+1]
            route[i][j] += route[i+1][j+1] + "1"

print(triangle[0][0])