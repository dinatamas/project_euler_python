f = open("11.dat", "r")
grid = [[0 for x in range(20)] for y in range(20)]
for i in range(0,20):
    line = f.readline().split()
    for j in range(0,20):
        grid[i][j] = int(line[j])

maxprod = 0
for i in range(0,20):
    horprod = grid[i][0] * grid[i][1] * grid[i][2] * grid[i][3]
    verprod = grid[0][i] * grid[1][i] * grid[2][i] * grid[3][i]
    maxprod = max(maxprod, horprod, verprod)
    for j in range(4,20):
        if grid[i][j-4] == 0:
            horprod = 1
            for k in range(j-3,j+1):
                horprod *= grid[i][k]
        else:
            horprod = horprod / grid[i][j-4] * grid[i][j]
        if grid[j-4][i] == 0:
            verprod = 1
            for k in range(j-3,j+1):
                verprod *= grid[k][i]
        else:
            verprod = verprod / grid[j-4][i] * grid[j][i]
        if i+3 < 20 and j-3 > 0:
            ldiagprod = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
        if i+3 < 20 and j+3 < 20:
            rdiagprod = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
        maxprod = max(maxprod, horprod, verprod, ldiagprod, rdiagprod)

print(maxprod)