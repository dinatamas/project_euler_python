# implement: conversion without base 10, + - * / in different bases

from math import log

"""
n = 2
bn = bin(n)
on = oct(n)
hn = hex(n)
"""

def encode(n):
    return "0123456789abcdefghijklmnopqrstuvwxyz"[n]

def decode(n):
    for i in range(36):
        if "0123456789abcdefghijklmnopqrstuvwxyz"[i] == n:
            return i

def convertto10(n, b):
    res = 0
    for i in range(len(n)):
        res += decode(n[len(n) - i - 1]) * b ** i
    return res

def convertfrom10(n, b):
    res = ""
    while n != 0:
        res = encode(n % b) + res
        n = n // b
    return res

def convert(n, b1, b2):
    return convertfrom10(convertto10(n, b1), b2)

def ispalindrome(n):
    return n == n[::-1]

res = 0
for i in range(1,1000000):
    if ispalindrome(str(i)) and ispalindrome(convert(str(i), 10, 2)):
        res += i

print(res)