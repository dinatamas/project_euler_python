big = 10 ** 999

i = 2
a = 1
b = 1
while b // big == 0:
    a, b = b, a+b
    i += 1

print(i)