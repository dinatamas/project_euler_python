# THIS PROBLEM HAS NOT BEEN SOLVED!

def ackermann(m, n):
    if m == 0:
        return n+1 % 14**8
    if m == 1:
        return n+2 % 14**8
    if m == 2:
        return 2*n+3 % 14**8
    if m == 3:
        return 2**(n+3)-3 % 14**8
    if m == 4:
        return (2**(2**(n+3))-3) % 14**8
    if n == 0:
        return ackermann(m-1, 1) % 14**8
    return ackermann(m-1, ackermann(m, n-1)) % 14**8