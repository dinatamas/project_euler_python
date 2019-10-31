# explicit mathematical formula?

# 1 digit * 9
# 2 digits * 90
# 3 digits * 900
# ...

# 1, 2, 3, 4, 5, 6, 7, 8, 9
# 10, 11, 12, ...
# 20, 21, 22, ...
# ...
# 100, 101, 102, ...

from math import floor, ceil

def index(n, i):
    return (n % 10 ** (i+1)) // 10 ** i

def champernowne_digit(pos, debug):
    digits = 1
    count = 9 * 10 ** (digits - 1)
    digitsum = digits * count
    while digitsum < pos:
        digits += 1
        count = 9 * 10 ** (digits - 1)
        digitsum += digits * count
    digitsum -= digits * count
    if debug:
        print(pos, digits, digitsum, end=" -- ")
    lastnumber = 10 ** (digits - 1) - 1
    x = ceil((pos - digitsum) / digits)
    num = lastnumber + x
    y = (pos - digitsum) % digits
    z = digits - y
    if debug:
        print(num, x, pos-digitsum, y, z, end=" -- ")
    digit = index(num, y)
    if debug:
        print(digit)
    return digit

for i in range(1,16):
    champernowne_digit(i, True)

champernowne_digit(189, True)
champernowne_digit(190, True)
champernowne_digit(191, True)
champernowne_digit(192, True)
champernowne_digit(193, True)

"""
res = 1
pos = 100
while pos <= 1000000:
    digit = champernowne_digit(pos)
    res *= digit

    pos *= 10

print(res)
"""