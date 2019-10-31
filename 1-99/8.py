f = open("8.dat", "r")
bigstr = f.read()

bigarr = [int(x) for x in bigstr]

maxprod = 1
for i in bigarr[0:13]:
    maxprod *= i
currprod = maxprod
for i in range(13,len(bigarr)):
    if bigarr[i-13] == 0:
        currprod = 1
        for j in bigarr[i-12:i+1]:
            currprod *= j
    else:
        currprod = currprod / bigarr[i-13] * bigarr[i]
    if currprod > maxprod:
        maxprod = currprod

print(maxprod)